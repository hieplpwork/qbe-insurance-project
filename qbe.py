from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load data
with open('data.json') as f:
    data = json.load(f)["data"]

# Endpoint to validate data
@app.route('/validate', methods=['POST'])
def validate():
    input_data = request.json
    errors = []

    for item in input_data["data"]:
        if item["var_name"] not in ["country", "age_group"]:
            errors.append(f"Invalid var_name: {item['var_name']}")
        elif not any(d["category"] == item["category"] and d["var_name"] == item["var_name"] for d in data):
            errors.append(f"Invalid category for {item['var_name']}: {item['category']}")

    if errors:
        return jsonify({"errors": errors}), 400
    return jsonify({"message": "Validation successful"}), 200

# Endpoint to get factors mapping
@app.route('/get_factors', methods=['POST'])
def get_factors():
    input_data = request.json
    results = []

    for item in input_data["data"]:
        factor = next((d["factor"] for d in data if d["category"] == item["category"] and d["var_name"] == item["var_name"]), None)
        if factor is not None:
            results.append({
                "var_name": item["var_name"],
                "category": item["category"],
                "factor": factor
            })

    return jsonify({"results": results}), 200

# Main run
if __name__ == '__main__':
    app.run(debug=True)
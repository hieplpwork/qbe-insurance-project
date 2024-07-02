import json

def validate_json(json_obj, schema):
    for key, type_val in schema.items():
        if key not in json_obj:
            return False
        
        if not isinstance(json_obj[key], type_val):
            return False
        
    return True

json_obj = {"name": "John", "age": 30}

schema = {"name": str, "age": int}

print(validate_json(json_obj, schema))
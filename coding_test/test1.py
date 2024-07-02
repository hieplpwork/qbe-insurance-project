import json

def swap_json_keys_and_vals(json_str):
    data = json.loads(json_str)
    print("data: ", data)

    # swap_data = {}
    # for key, val in data.items():
    #     # key = item.key
    #     # val = str(item.val)
    #     swap_data [str(val)] = key
    
    swap_data = {value: key for key, value in data.items()}
    print("swap_data: ", swap_data)
    return json.dumps(swap_data)

input = """{"1": "a", "2": "b"}"""
print(swap_json_keys_and_vals(input))

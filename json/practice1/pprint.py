import json
data = {"z": 1, "b": 2, "a": 3}

value = json.dumps(data, indent=4)
print(value)
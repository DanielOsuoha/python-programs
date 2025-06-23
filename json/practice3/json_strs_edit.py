import json

def modify_jsonstrs(json_str):
    python_obj = json.loads(json_str)
    python_obj["completed"] = True
    return json.dumps(python_obj)

if __name__ == "__main__":
    json_str = '{"task": "submit resume", "completed": false}'
    print(modify_jsonstrs(json_str))
import json

def main():
    file = "student.json"
    file = open(file, "r")
    student = {
        "name": "Daniel",
        "age": 21,
        "courses": ["Math", "CS", "Physics"]
    }
    json.dump(student, file, indent=4)
    file.close()
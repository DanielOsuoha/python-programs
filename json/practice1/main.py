import json

def main():
    file = "student.json"
    student = {
        "name": "Daniel",
        "age": 21,
        "courses": ["Math", "CS", "Physics"]
    }
    with open("student.json", "w") as file:
        json.dump(student, file, indent=4)

if __name__ == "__main__":
    main()
    print("JSON file created successfully.")
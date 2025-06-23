import json

def main():
    file = "student.json"
    file = open(file, "w")
    student = {
        "name": "Daniel",
        "age": 21,
        "courses": ["Math", "CS", "Physics"]
    }
    json.dump(student, file, indent=4)
    file.close()

if __name__ == "__main__":
    main()
    print("JSON file created successfully.")
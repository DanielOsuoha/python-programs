import json

def main():
    with open("student.json", "r") as file:
        values = json.load(file)
    print(values)


if __name__ == "__main__":
    main()
    print("Loaded values")
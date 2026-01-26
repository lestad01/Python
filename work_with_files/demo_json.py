import json

# константа
JSON_FILE_PATH = "file.json"
JSON_LINES_FILE_PATH = "file.jl"



def demo_json_dump_to_str():
    data = {
        "users": [
            {
                "id": 42,
                "username": "John",
            },
            {
                "id": 12,
                "username": "Sam",
            },
        ],
    }
    print(data)
    print(type(data))
    print(data["users"])

    data_str = json.dumps(data)

    print(type(data_str))
    print(data_str)

def demo_json_load_to_str():
    data_str = ('{"users":[{"id": 42, "username": "John"}, '
                '{"id": 12, "username": "Sam"}]}' 
                )
    print(type(data_str))
    print(data_str)

    data = json.loads(data_str)
    print(data)
    print(type(data))
    print(data["users"])

def demo_json_dump_and_load_to_file():
    data = {
        "users": [
            {
                "id": 42,
                "username": "John",
            },
            {
                "id": 12,
                "username": "Sam",
            },
        ],
    }

    # indent параметр устанавливающий количество пробелов
    # data_string = json.dumps(data, indent=2) 

    # создаем файл JSON
    with open(JSON_FILE_PATH, "w") as f:
        json.dump(data,f)
        # f.write(data_string)
    
    with open(JSON_FILE_PATH, "r") as f:
        data_from_path = json.load(f)
    
    print(data_from_path)
    print(type(data_from_path))

def demo_json_lines():
    user1 = {"id": 1, "name": "John", "friends": [2, 3]}
    user2 = {"id": 2, "name": "Sam", "friends": [1]}
    user3 = {"id": 3, "name": "Nick", "friends": [1]}

    # with open(JSON_LINES_FILE_PATH, "a") as f: a дописываем
    with open(JSON_LINES_FILE_PATH, "w") as f:
        for user_data in [user1, user2, user3]: 
            json.dump(user_data, f)
            f.write("\n")
    with open(JSON_LINES_FILE_PATH, "r") as f:
        for line in f:
            if not line:
                continue
            user_data = json.loads(line)
            print("user data:" , user_data)
            print("id:", user_data["id"], "name:", user_data["name"])
        

def main():
    # demo_json_dump_to_str()
    # demo_json_load_to_str()
    # demo_json_dump_and_load_to_file()
    demo_json_lines()


if __name__ == '__main__':
    main()
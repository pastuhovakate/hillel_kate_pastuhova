from pprint import pprint
from re import U

tiesto = {
    "name": "Tiesto",
    "age": 55,
    "equipment": "Pioneer",
    "discography": 20,
    "salary": 30_000,
    "genre": "lite-house",
}
avicci = {
    "name": "Avicci",
    "age": 22,
    "equipment": "Pioneer",
    "discography": 40,
    "salary": 0,
    "genre": "adm",
}
anna = {
    "name": "Anna",
    "age": 24,
    "equipment": "Synth",
    "discography": 3,
    "salary": 3_000,
    "genre": "techno",
}


def validate_dj_data(data):
    if len(data) != 6:
        print("The number of arguments is not correct!")
        return None

    if data[0].isdigit():
        print(f"{data[0]} is digit")
        return None

    for element in [data[1], data[3], data[4]]:
        index = data.index(element)
        if element.isdigit():
            data[index] = int(element)
        else:
            print(f"{element} is not a digit")
            return None

    if not data[5].isalnum():
        print(f"{data[5]} is not an alnum")
        return None

    return data


def add_dj(data):
    user_input = input("Enter new DJ's data: ")
    dj_data = user_input.split(",")
    validated_data = validate_dj_data(dj_data)

    if validated_data is not None:
        new_dj_data = {
            "name": validated_data[0],
            "age": validated_data[1],
            "equipment": validated_data[2],
            "discography": validated_data[3],
            "salary": validated_data[4],
            "genre": validated_data[5],
        }
        data.append(new_dj_data)
        return new_dj_data

def remove_by_name_dj(data):
    user_input_for_del = input("Enter DJ's name to remove from the data: ")
    new_data = []
    for name in data:
        if name["name"] != user_input_for_del:
            new_data.append (name)
    return new_data

def update_dj(data):
    dj_name = input("Enter DJ's name to update: ")
    user_input =input("DJ input format: name,age,equipment,discography,salary,genre: ")
    dj_data = user_input.split(",")
    validated_data = validate_dj_data(dj_data)

    if validated_data is None:
        return None
    new_data = []
    for name in data:
        if name ["name"] == dj_name:
            new_dj_data = {
                "name": validated_data[0],
                "age": validated_data[1],
                "equipment": validated_data[2],
                "discography": validated_data[3],
                "salary": validated_data[4],
                "genre": validated_data[5],
             }
            new_data.append(new_dj_data)
        else: 
            new_data.append(name)
    return new_data

if __name__ == "__main__":
    djs = [tiesto, avicci, anna]
    allowed_options = "[add/list/names/update/remove/exit]"

    while True:
        desision = input(f"What should I do?{allowed_options}: ")
        if desision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre")
            new_dj = add_dj(djs)
            if new_dj:
                print(f"DJ {new_dj['name']} is added!")
        elif desision == "list":
            pprint(djs)
        elif desision == "names":
            data = [dj["name"] for dj in djs]
            pprint(data)
        elif desision == "update":
            new_djs = update_dj(djs)
            print(f"New Dj saved to list! Update list is:" ,new_djs)
        elif desision == "remove":
            new_djs = remove_by_name_dj(djs)
            data = [dj["name"] for dj in new_djs]
            print(f"Dj removed from the list! New list is:",data)

        elif desision == "exit":
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")

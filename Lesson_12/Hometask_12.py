import csv


class Dj:
    djs_csv = []

    def __init__(self, name, age, equipment, discography, salary, genre, male):
        self.name = name
        self.age = age
        self.equipment = equipment
        self.discography = discography
        self.salary = salary
        self.genre = genre
        self.male = male

    @property
    def as_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "equipment": self.equipment,
            "discography": self.discography,
            "salary": self.salary,
            "genre": self.genre,
            "male": self.male,
        }

    @classmethod
    def csv_add(cls):
        print("Update DJ's data by format: name,age,equipment,discography,salary,genre,male: ")
        Dj.djs_csv.append(cls.validate(input("Enter new DJ's data : ").split(",")).as_dict)
        if Dj.djs_csv:
            return f'Dj name: {Dj.djs_csv[-1]["name"]} is added'

    @classmethod
    def csv_delete(cls, name):
        for dj in cls.djs_csv:
            if dj["name"] == name:
                index = cls.djs_csv.index(dj)
                del cls.djs_csv[index]
                return True
        return False

    @classmethod
    def csv_update(cls, name):
        for dj in cls.djs_csv:
            if dj["name"] == name:
                print("Update DJ's data by format: name,age,equipment,discography,salary,genre,male: ")
                data_for_update = cls.validate(input("Enter new DJ's data: ").split(",")).as_dict
                for new_data in dj:
                    dj[new_data] = data_for_update[new_data]
                return dj

    @classmethod
    def csv_list(cls):
        for dj in Dj.djs_csv:
            print(f'He is: {dj["name"]}, {dj["age"]} years old' if dj["male"] == "True"
                  else f'She is: {dj["name"]}, {dj["age"]} years old')

    @classmethod
    def csv_names(cls):
        print([dj["name"] for dj in Dj.djs_csv])

    @classmethod
    def validate(cls, data):
        if len(data) != 7:
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

        return cls(*data)

    @classmethod
    def read_from_csv(cls):
        FILENAME = "djs_old.csv"
        with open(FILENAME) as csv_file:
            reader = csv.DictReader(csv_file)
            djs_csv = [dj for dj in reader]
        return djs_csv

    @classmethod
    def update_file_csv(cls):
        FILENAME = "djs.csv"
        with open(FILENAME, "w", newline="") as file_csv:
            header = ["name", "age", "equipment", "discography", "salary", "genre", "male"]
            writer_dict = csv.DictWriter(file_csv, fieldnames=header)
            writer_dict.writeheader()
            writer_dict.writerows(Dj.djs_csv)


if __name__ == "__main__":
    extracted_djs_csv: list = Dj.read_from_csv()
    Dj.djs_csv = extracted_djs_csv

    allowed_options = "[add/list/names/delete/update/exit/]"

    while True:
        decision = input(f"What should I do?{allowed_options}: ")

        if decision == "list":
            Dj.csv_list()
        elif decision == "names":
            Dj.csv_names()
        elif decision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre,male")
            new_dj = Dj.csv_add()
            print(new_dj)
        elif decision == "update":
            print([dj["name"] for dj in Dj.djs_csv])
            name = input("Input DJ's name for update: ")
            updated_dj = Dj.csv_update(name)
            if updated_dj:
                print(f"DJ {name} updated to: {updated_dj['name']}")
        elif decision == "delete":
            delete_name = input("Input DJ's name for delete: ")
            deleted = Dj.csv_delete(delete_name)
            if deleted is True:
                print(f"DJ {delete_name} is deleted!")
        elif decision == "exit":
            print("Updating the file...")
            Dj.update_file_csv()
            print("File saved ✅ ")
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")


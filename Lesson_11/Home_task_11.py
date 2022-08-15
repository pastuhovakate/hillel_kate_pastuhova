from pathlib import Path
from pprint import pprint

print(sorted(Path('.').glob('*.*')))


class File:
    @staticmethod
    def read_last_10_lines():
        print(*(file.read().split("\n")[-10:]), sep='\n')
        

    @staticmethod
    def read_first_10_lines():
        print(*(file.read().split("\n")[:11]), sep='\n')

    @staticmethod
    def read_all_file():
        return file.read()

    @staticmethod
    def find_longest_word():
        longest_word = file.read()
        longest_word = longest_word.replace(",", "")
        max_longest_word = longest_word.split()
        return f"Maximal len of word in '{filename}' is: {max(max_longest_word, key=len)}"

    @staticmethod
    def lines_number():
        count = 0
        for line in file:
            count += 1
        return f"Number of lines in file are: {count}"


    @staticmethod
    def return_to_start():
        file.seek(0)


if __name__ == "__main__":
    filename = input(f"Please enter file name to open: ")
    allowed_options = f" \n[1 - read_last_10_lines \n 2 - read_first_10_lines \n 3 - read_all_file \n" \
         f" 4 - find_longest_word \n 5 - lines_number \n 6 - exit]"

    if Path(filename).exists():
        with open(filename, mode="r", encoding="utf-8") as file:
            print(f'Opening file: {filename} ...')
            while True:
                decision = input(f"Select action with text: {allowed_options}: ")
                if decision == "1": 
                    File.read_last_10_lines()
                    File.return_to_start()
                elif decision == "2": 
                    File.read_first_10_lines()
                    File.return_to_start()
                elif decision == "3": 
                    print(File.read_all_file())
                    File.return_to_start()
                elif decision == "4": 
                    print(File.find_longest_word())
                    File.return_to_start()
                elif decision == "5": 
                    print(File.lines_number())
                    File.return_to_start()
                elif decision == "6":
                    print(f"Bye")
                    break
    else:
        print(f"File not found!")
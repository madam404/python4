try:
    with open("sample.txt", "r") as file:
        line_number = 1
        for line in file:
            print(f"line {line_number} : {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print("error : the file sample.txt was not found.")

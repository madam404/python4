# python4

task1.py 

🔹 try:

Begins a block of code that may cause an error.

Helps prevent the program from crashing when an error (like missing file) occurs.



---

🔹 with open("sample.txt", "r") as file:

Attempts to open a file named sample.txt in read mode ("r").

with ensures the file is safely closed after reading, even if errors happen.

file is the file object that refers to sample.txt.



---

🔹 line_number = 1

Initializes a counter to track and display line numbers.

Starts at 1 (instead of 0) to represent natural line numbering.



---

🔹 for line in file:

Loops through the file line by line.

Each line is a string containing text from a line in the file, including the newline character (\n).



---

🔹 print(f"line {line_number} : {line.strip()}")

Prints each line in the format:
line 1 : <line content>

line.strip() removes any leading/trailing whitespace, including newline characters (\n).



---

🔹 line_number += 1

Increments the line number after each iteration so that the next line gets the correct number.



---

🔹 except FileNotFoundError:

Catches the specific error raised if the file sample.txt does not exist in the same directory.

Without this, the program would crash with a traceback.



---

🔹 print("error : the file sample.txt was not found.")

Displays a friendly error message to the user if the file is missing.







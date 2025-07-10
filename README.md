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



task2.py



🔹 user_input = input("Enter text to write to the file: ")

Prompts the user to enter some text.

The input is stored in the variable user_input.

Example: If user types Hello, user_input = "Hello".



---

🔹 with open("output.txt", "w") as file:

Opens or creates the file output.txt in write mode ("w").

Write mode erases existing content, if the file already exists.

Uses the with statement to automatically close the file after writing.



---

🔹 file.write(user_input + "\n")

Writes the user's input to the file followed by a newline character (\n).

This ensures that the text appears on a new line.

Example written to file:

Hello



---

🔹 print("Data successfully written to output.txt.\n")

Confirms that the data was successfully written to the file.

\n adds an empty line after the message.



---

🔹 more_data = input("Enter additional text to append: ")

Prompts the user for more text.

Stores the new input in more_data.



---

🔹 with open("output.txt", "a") as file:

Opens output.txt in append mode ("a").

In this mode, the new data is added to the end of the file without erasing previous content.



---

🔹 file.write(more_data + "\n")

Adds the new input at the end of the file, again followed by a newline.

Example file content now:

Hello
World



---

🔹 print("Data successfully appended.\n")

Notifies the user that appending was successful.



---

🔹 print("Final content of output.txt:")

Prints a heading to indicate that the final file content is about to be displayed.



---

🔹 with open("output.txt", "r") as file:

Opens the file in read mode ("r").

Used to read the entire content of the file line by line.



---

🔹 for line in file:

Loops through each line in the file.

Each line is a string containing the content and the newline (\n) character.



---

🔹 print(line.strip())

strip() removes extra whitespace, including the trailing newline character.

The cleaned line is then printed to the screen.



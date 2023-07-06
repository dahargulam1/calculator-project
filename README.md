# Calculator-Project
Simplified interface for easy calculations. Built with the goal of providing users with a calculator featuring a straightforward layout and the ability to perform basic arithmetic operations.

# Motivation
The project was built so that, i may reenforce my learning of the following programming concepts.

File Handling: The code includes functions for reading from and writing to files. It demonstrates how to open and manipulate files, check for specific patterns within the file, and perform operations based on the file content.

Regular Expressions (Regex): The code utilizes regular expressions (regex) to match and validate equations and results. It employs regex patterns to identify equations with results and equations without results, and it uses the re module to perform pattern matching operations.

Error Handling: The code implements exception handling using try, except, and finally blocks to catch and handle potential errors. It includes different exception types such as FileNotFoundError, UnicodeDecodeError, and custom exceptions to provide informative error messages to the user.

User Input: The code prompts the user for input, such as file names and operator choices, and validates the input for correctness.

String Manipulation: The code manipulates strings to format and display equations and results. It uses string interpolation (f"...") to format the result and equation for displaying and writing to files.

Control Flow: The code utilizes loops (while) and conditional statements (if, elif, else) to control the flow of execution. It repeats operations until certain conditions are met, checks for valid operators, and handles different file-related scenarios.

Overall, this project demonstrates my understanding of file handling, regex, error handling, user input, string manipulation, and control flow concepts in programming.


# Installation

**Mac OS X**: A version of Python is already installed.  
**Linux**: A version of python is already installed.  
**Windows**: You will need to install one of the 3.x versions available at [python.org](http://www.python.org/getit/).

# General usage information

 * Download Calculator.py 
 * To run the scipts simply type `python` followed by the file name, `Calculator.py`
 * If the script is in a different directory from which you are trying to run it, you will need to provide the full path to the script’s file, e.g. `python /Users/document/foldername/Calculator.py`.

# Instructions
1) when you run the script you should see the following menu
```
Menu

1) calculator - solve a equation based on the inputed numbers
2) calculation history - read from a file, previous calculation
3) exit

Please choose a option (1 - 3): 
```
2) If you choose option one then the calculator function will run and will prompt you to enter any number, followed by a operator and lastly another number. Using this information it will perform a calculation and display the result to you, as well as save it to a text file. The following example demonstrate this

This is how the program will look like, after user enters their value

```
Calculator -

Please enter the first number: 2
Please enter what operation you would like to perform (+, -, *, /): +
Please enter your second number: 4
The result is, 6.0

Do you wanna do another calculation(y/n):
```
This is how the text file should look like

```
2.0 + 4.0 = 6.0
```
3) If you choose option two you would be prompt to enter a file name. This is a usefull function as you are able to calculate muliple equaions or to display historic calculation. So for example, if you edit the calculation_history.txt file and add a equation*, the program will read the the first equation and display it normally but for the second one it will calculate the result and then display it to the user. As shown below

This is the modified text file

```
2.0 + 4.0 = 6.0
4.0 * 4.0 =
```
This is how the program would look like, after user enters their value

```
Calculation history -

please enter the name of the file you would like to view: temp

File found, equations and results displayed below:

2.0 + 4.0 = 6.0
4.0 * 4.0 = 16.0

Do you wanna load another file(y/n): 
```
4) choose 3 to exist the program

\* Please ensure that you enter the equation in the correct format otherwise it will cause an error. The format is     d.d [+-*/] d.d = 

# This programs acts as either -
# 1)    A calculator getting the user to input two numbers along with a operator. It then 
#       does a operation using the provided number and display the result to the user,  
#       along with writing the equation and result to a file.
# 2)    Read a existing file, that the user specify and display all the equations and 
#       results (if the equation has no result, the program will calculate it for the user) from it. 

import re

# function check files for any equation with or without the calculated result

def check_equation(line):

    # check if the line from file has either a equation with a result or just a equation by using regex
    
    pattern_results = r'^(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*=\s*(-?\d+(?:\.\d+)?)$'    # used https://chat.openai.com/ to create the regex as i am unfamilier with re function and regex attributes 
    pattern_no_results = r'^(-?\d+(?:\.\d+)?)\s([+\-*/])\s(-?\d+(?:\.\d+)?)\s=\s*$'                     # modified a bit to ensure that spaces are required in equation, for split function, used later on for calculation 

    if re.match(pattern_results, line):                                                                 # learnt this function from  https://chat.openai.com/
        return(line) # return the line as it matchs a equation with a result

    # If line is just an equation, it split the line into it's component, convent the number 
    # into float and send it to the calculator function to work out the result 
    
    elif re.match(pattern_no_results, line):                                                            # learnt this funtion from https://chat.openai.com/
        
        number1, operator, number2, equal = line.split()
        number1 = float(number1)
        number2 = float(number2)

        return(calculator("computer", number1, operator, number2)) # return the equation with the calculated result 
          
    else:
        return ""

# function is used to write to file using a certain format and read a file, which will only 
# return lines if it's the correct format 

def calculator_file(file_name, file_mode, equation = ""): # function is called to read file which does not need equation, therefore to avoid error, it has a default value

    try:
    
        # write to file using the equation var that was passed on to functon. The format of the var is used for reading from the file later on.

        if file_mode == "a":
            
            with open(file_name, file_mode, encoding = "utf-8") as cal_file:
                cal_file.write(equation)

        # read files and check for any equation using the check_equation function

        if file_mode == "r":
            
            equ_and_result = ""

            with open(file_name, file_mode) as cal_file:

                for line in cal_file:
                    
                    file_equation = check_equation(line)
                    
                    if file_equation != "": # if the return value is not empty then an equation was found in the file and added to var to display
                         equ_and_result += file_equation

                if equ_and_result == "": # any text file can be read, so this was added to allow the user to be informed that the text file had no equations
                    raise Exception("Error: The file does not contain any equation or the file is not formated correctly")    
                
                return equ_and_result
                    
    except FileNotFoundError: 
        print("\nError: The file does not exist")
        
    except UnicodeDecodeError: # stop user from loading any file that not a text file
        print("\nError: The file is a type that cannot be read. Please try another file")

    except Exception as error: # to create a exception for custom error and for any others
        print("\n" + str(error))    

# function will calculate the result from an equation either entered from the user or from a file

def calculator(mode, number1 = 0, operator = "+", number2 = 0):

    while True:
        
        try:

            if mode == "user": # allow user to enter input when function is called by user
                
                print("\nCalculator -\n")
                
                # Gather the input required for the calculation

                number1 = float(input("Please enter the first number: "))
                
                operator = input("Please enter what operation you would like to perform (+, -, *, /): ")

                if not (operator == "+" or operator == "-" or operator == "*" or operator == "/"): # custom error to insure user enter only viable operators
                    raise Exception("Error: Invalid operator. Please enter one of these operators, +, -, *, /") 
                
                number2 = float(input("Please enter your second number: "))

            # calculate the result from the users or parameter variables

            if operator == "+":
                result = number1 + number2 
            
            elif operator == "-":
                result = number1 - number2 
            
            elif operator == "*":
                result = number1 * number2 
            
            elif operator == "/":
                result = number1 / number2 
            
            resultDisplayed = f"{number1} {operator} {number2} = {result}\n" # this is for displaying and formating, for writing to file
            
            if mode == "user": # this will only show if the user called the function otherwise skipped if called from the program for working out equations from file       
                
                print (f"\nThe result is, {result}")
            
                calculator_file("./calculation_history", "a", resultDisplayed) # call function to write to file
            
            if mode == "computer": # will return the equation read from a file with the calculated result 
                return resultDisplayed
                
        except ValueError: 
            print("\nError: Invalid input. Please enter numeric values")
    
        except ZeroDivisionError: # display error. displayed differently for clarity for user
            
            if mode == "user":
                print("\nError: Cannot divide by zero") 

            if mode == "computer": # allow the user to know what equation from file is causing an error
                return f"{number1} {operator} {number2} = Error: cannot divide by zero\n"
             
        except Exception as error: # allow exception for custom error and any other
            print("\n" + str(error))
            
        finally:
            
            if mode == "user": # if user called function allow them, the option to do another calculation
                another_cal = input("\nDo you wanna do another calculation(y/n): ")

                if another_cal != "y":
                    break           

# function will read from a file and display any equation that it finds

def calculation_history():
    
    while True:
        
        print("\nCalculation history -\n")

        # ask the user what file they would like to read from and attempt to load the file

        file_name = input("please enter the name of the file you would like to view: ")
        cal_history = calculator_file(file_name, "r")
        
        # if a text file is called successfully and has equation then it will be displayed to the user

        if cal_history is not None:
            
            print("\nFile found, equations and results displayed below:\n")
            print(cal_history)

        # give the user the option to read another file, 

        another_file = input("\nDo you wanna load another file(y/n): ")

        if another_file != "y":
            break  

# a simple menu option that loops until the user is done using the program, they can either 
# do a calculation, read equation from a file or quit the program

def menu():

    exit = False
    
    while exit == False:
        
        print("\nMenu\n")
        print("1) calculator - solve a equation based on the inputed numbers")
        print("2) calculation history - read from a file, previous calculation") 
        print("3) exit") 


        options = input ("\nPlease choose a option (1 - 3): ")

        if options == "1":
            calculator("user")
        
        elif options == "2":
            calculation_history()
        
        elif options == "3":
            print("\nExiting")
            exit = True
        
        else:
            print("\nError: Invalid option. Please choose between 1 to 3")

menu()
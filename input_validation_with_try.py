'''
Program: input_validation_with_try.py
Author: Joshua M. McGinley
Last date modified: 09/21/2022

 Input Validation with Try Assignment
You can now update your average test scores code from a previous assignment with added input validation using
try/except.
Details:

    Update your previous assignment code to include try/except for each of the user inputs.
    If the user enters negative numbers or a string for their number inputs, the except path should print an
    error message.

'''

import constants  #Import the module constants.py

#Taking and storing input
#Try and except has been added
try:
    first_name = str(input('What is your first name? '))  #Take input and store it as first_name
except:
    print('Evil input!')
try:
    last_name = str(input('What is your last name? '))  #Take input and store it as last_name
except:
    print('Evil input')
try:
    age = int(input('What is your age? '))  #Take input and store it as age
except:
    print('Evil input!')

try:
    score_1 = float(input('Now enter score: '))  #Take input and store as float in score_1
except:
    print('Evil input!')
try:
    score_2 = float(input('Now enter score: '))  #Take input and store as float in score_2
except:
    print('Evil input!')
try:
    score_3 = float(input('Now enter score: '))  #Take input and store as float in score_3
except:
    print('Evil input!')

#Finding and storing average of three scores#
average_grade = (score_1 + score_2 + score_3) / constants.NUMBER_OF_SCORES  #Add score_1, score_2, score_3, and#
                                                                            #divide by the constant NUMBER_OF_SCORES#
#Printing output to screen#
print(last_name, end='')  #Print last_name to screen append next line
print(',', first_name, 'age: ', end='')  #Print , first_name age: append next line
print(age, 'average grade:', end='')  #Print age average grade: append next line
print(f'{average_grade: 5.2f}')  #Print average_grade formated as decimal totla of five digits with only two digits#
                                 #after the decimal#

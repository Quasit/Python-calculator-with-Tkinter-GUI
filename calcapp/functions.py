import calcapp.globals as gl


def click(label, string):
    # Main function which identifies button clicked, checks conditions, and calls proper helper functions
    string = str(string)
    numbers = '0123456789'
    signs = ['AC', '⌫', '%', '÷', '×', '-', '+', '.', '=']
    string = convert(string)
    
    if gl.solved:
        delete_output(label)
        gl.solved = False

    if string in numbers: # Numbers section
        if string == '0': # 0 cases
            if len(gl.output) == 1 and gl.output[-1] != '0': # If first number is already in output, but it's not 0 -> can add 0
                add_to_output(label, string)
            elif len(gl.output) == 0: # If output is empty -> can add 0
                add_to_output(label, string)
            elif len(gl.output) > 1 and not front_zero_check(): # If there is at least 1 number in output and there will be no double 0 at front:
                add_to_output(label, string)
        else: # other numbers
            if len(gl.output) == 1 and gl.output[0] == '0': # if there is 0 as first number in the output -> replace it
                replace_output(label, string, 0)
            elif front_zero_check():  # if there is 0 as first number after a sign -> replace it
                replace_output(label, string, len(gl.output)-1)
            else:
                add_to_output(label, string) # numbers other than 0 can be added without additional conditions
    elif string in signs: # Signs section
        if string == 'AC': # Delete whole output
            delete_output(label)
        elif string == '⌫': # Remove one last character
            backspace_output(label)
        elif string == '%': # Percentage
            # checks if helper function will return True - meaning it's possible to calculate percentage
            if is_percentage_possible():
                # calls helper function to change output for percentage
                percentage_calculate(label)
        elif string == '÷':
            # if there is already some sign as last character -> replace it
            if gl.output[-1] not in numbers: 
                replace_output(label, string, len(gl.output)-1)
            else:
                add_to_output(label, string)
        elif string == '×':
            # if there is already some sign as last character -> replace it
            if gl.output[-1] not in numbers: 
                replace_output(label, string, len(gl.output)-1)
            else:
                add_to_output(label, string)
        elif string == '-':
            # if there is already some sign as last character -> replace it
            if gl.output[-1] not in numbers and len(gl.output) > 0:
                replace_output(label, string, len(gl.output)-1)
            else:
                add_to_output(label, string)
        elif string == '+':
            # if there is already some sign as last character -> replace it
            if gl.output[-1] not in numbers:
                replace_output(label, string, len(gl.output)-1)
            else:
                add_to_output(label, string)
        elif string == '.':
            # if there is nothing in output add 0 before '.'
            if len(gl.output) == 0:
                add_to_output(label, '0.')
            # if last character isn't already a '.'
            elif gl.output[-1] != '.':
                # if last character in output is some sign add 0 before '.'
                if gl.output[-1] in signs:
                    add_to_output(label, '0.')
                elif not double_dot_check(): # otherwise, check for double dot and just add '.'
                    add_to_output(label, string)
        elif string == '=' or string == 'Return':
            if gl.output[-1] in signs:
                backspace_output(label)
            splitted = split_output(gl.output)
            solution = calculate(splitted)
            gl.solved = True
            delete_output(label)
            add_to_output(label, str(solution))

def convert(string):
    # Helper function to convert keyboard keys pressed into needed symbols
    if string == 'slash':
        string = '÷'
    elif string == 'asterisk':
        string = '×'
    elif string == 'comma':
        string = '.'
    elif string == 'plus':
        string = '+'
    elif string == 'minus':
        string = '-'
    elif string == 'BackSpace':
        string = '⌫'
    elif string == 'Delete':
        string = 'AC'
    elif string == 'equal':
        string = '='
    elif string == 'percent':
        string = '%'
    return string


def add_to_output(label, string):
    # Helper function responsible for adding characters to output and updating label
    gl.output = gl.output + string
    label.config(text=gl.output)

def replace_output(label, string, index):
    # Helper function responsible for replacing characters in output and updating label
    gl.output = gl.output[:index] + string + gl.output[index+1:]
    label.config(text=gl.output)

def delete_output(label):
    # Helper function responsible for deleting all characters in output and updating label
    gl.output = ''
    label.config(text=gl.output)

def backspace_output(label):
    # Helper function responsible for deleting only last character in output and updating label
    gl.output = gl.output[:len(gl.output)-1]
    label.config(text=gl.output)

def double_dot_check():
    '''
    Checks if current number already got a dot
    True there is dot already, False there is no dot
    '''
    index = len(gl.output)-1
    signs = ['÷', '×', '-', '+']
    while index > 0 and gl.output[index] not in signs:
        if gl.output[index] == '.':
            return True
        index = index - 1
    return False

def front_zero_check():
    '''
    Checks if there would be double 0 at front
    True - zero at front, False - no zero at front
    '''
    index = len(gl.output)-1
    signs = ['÷', '×', '-', '+']
    if index > 0:
        if gl.output[index] == '0' and gl.output[index-1] in signs:
            return True
    return False

def is_percentage_possible():
    '''
    Function checks if there is more than one number in the input and sign between them
    True - can do percentage, False - cannot
    '''
    index = len(gl.output)-1
    numbers = '0123456789'
    signs = ['÷', '×', '-', '+']
    if gl.output[index] in numbers:
        while index > 1:
            if gl.output[index] in signs and gl.output[index-1] in numbers:
                return True
            index = index - 1
    return False

def percentage_calculate(label):
    '''
    Function that calculates percentage
    If add or subtract, it will calculate and replace percentage in the output with calculated number
    If multiply, or divide, it will divide percentage number by 100, and replace output with fraction number
    '''
    index = len(gl.output)-1
    signs = ['÷', '×', '-', '+']
    while index > 0 and gl.output[index] not in signs: # first need to locate our sign
        index = index - 1
    output_copy = gl.output[:index] # copy output before sign
    sign = gl.output[index] # get the sign
    percentage_number = gl.output[index+1:] # get the percentage number
    percentage_number = float(percentage_number) # convert percentage number into float
    if sign in '-+':
        # for addition and subtraction need to calculate everything before, to get right percentage
        splitted_before_percentage = split_output(output_copy) # split output before sign into separate numbers and signs
        solution_before_percentage = calculate(splitted_before_percentage) # calculate everything before percentage
        solution_after_percentage = solution_before_percentage * (percentage_number / 100) # get percentage number
    elif sign in '÷×':
        # for multiply and division just need to divide percentage number by 100
        solution_after_percentage = percentage_number / 100
    if solution_after_percentage.is_integer(): solution_after_percentage = int(solution_after_percentage) # if can, convert percentage solution number to int
    output_copy = output_copy + sign + str(solution_after_percentage) # now just combine new output
    gl.output = output_copy # replace output with new one
    label.config(text=gl.output) # and update label

def split_output(output):
    # Helper function which goes through output and splits it into numbers and signs
    signs = ['÷', '×', '-', '+', '*', '/']  # helper list containing operation signs
    splitted = [] # empty array to store splitted items
    index = 0 # Current index for while loop
    last_add = 0 # Index for lastly added item, so next added item wouldn't start from index 0
    while index < len(output): # Repeat until reach end of output
        if output[index] in signs:  # If it finds sign gets each char until sign index and appends it into 'splitted' array and also appends sign as separate item
            number = ''
            for i in range(last_add ,index):
                number += output[i]
            splitted.append(number)
            if output[index] == '÷':
                splitted.append('/')
            elif output[index] == '×':
                splitted.append('*')
            else:
                splitted.append(output[index])
            last_add = index + 1 # already added item, so it needs to set last_add index
        elif index == len(output)-1: # Repeats same as above, but for last number, so there is no sign at the end to add
            number = ''
            for i in range(last_add ,index+1):
                number += output[i]
            splitted.append(number)
        index += 1
    for index, item in enumerate(splitted): # loop to check splitted numbers and convert them from strings to either integers or floats
        if item not in signs:
            splitted[index] = float(item) if '.' in item else int(item)
    return splitted

def calculate(list):
    '''
    Main function for calculation, which goes through list and does calculations depending on mathematical order
    '''
    initial_list = list.copy() # Copy list, just to not change the original one
    temp_list = [] # Helper list
    index = 0 # Starting index
    while ('*' or '/' in initial_list) and (index < len(initial_list)-1): # Loop for solving until there is no more Multiplication or division
        if initial_list[index] == '*': # Multiplication
            solution = initial_list[index-1] * initial_list[index+1] # calculation itself
            for i in range(0, index-1): # adding items *before multiplication* to temporary list
                temp_list.append(initial_list[i])
            temp_list.append(solution) # adding multiplication solution
            for i in range(index+2, len(initial_list)): # adding items *after multiplication* to temporary list
                temp_list.append(initial_list[i])
            initial_list = temp_list.copy() # replace initial_list so we could go to another solution
            temp_list = [] # empty temp_list for next solution
            index = -1 # since index is incremented at the end of loop, need to set it to -1 so we could start from index 0 next time
        elif initial_list[index] == '/': # Division
            solution = initial_list[index-1] / initial_list[index+1] # calculation itself
            for i in range(0, index-1): # adding items *before division* to temporary list
                temp_list.append(initial_list[i])
            temp_list.append(solution) # adding division solution
            for i in range(index+2, len(initial_list)): # adding items *after division* to temporary list
                temp_list.append(initial_list[i])
            initial_list = temp_list.copy() # replace initial_list so we could go to another solution
            temp_list = []  # empty temp_list for next solution
            index = -1  # since index is incremented at the end of loop, need to set it to -1 so we could start from index 0 next time
        index += 1 # it's while loop, so need to increment index manually

    index = 0 # Setting index at 0 for new loop
    while ('+' or '-' in initial_list) and (index < len(initial_list)-1): # Loop for solving until there is no more addition or subtraction
        if initial_list[index] == '+': # Addition
            solution = initial_list[index-1] + initial_list[index+1] # calculation itself
            for i in range(0, index-1):  # adding items *before addition* to temporary list
                temp_list.append(initial_list[i])
            temp_list.append(solution)  # adding addition solution
            for i in range(index+2, len(initial_list)): # adding items *after addition* to temporary list
                temp_list.append(initial_list[i])
            initial_list = temp_list.copy() # replace initial_list so we could go to another solution
            temp_list = []  # empty temp_list for next solution
            index = -1  # since index is incremented at the end of loop, need to set it to -1 so we could start from index 0 next time
        elif initial_list[index] == '-': # Subtraction
            solution = initial_list[index-1] - initial_list[index+1] # calculation itself
            for i in range(0, index-1):  # adding items *before subtraction* to temporary list
                temp_list.append(initial_list[i])
            temp_list.append(solution)  # adding subtraction solution
            for i in range(index+2, len(initial_list)): # adding items *after subtraction* to temporary list
                temp_list.append(initial_list[i])
            initial_list = temp_list.copy() # replace initial_list so we could go to another solution
            temp_list = []  # empty temp_list for next solution
            index = -1  # since index is incremented at the end of loop, need to set it to -1 so we could start from index 0 next time
        index += 1  # it's while loop, so need to increment index manually
    
    if type(initial_list[0]) is int: # Check if our solution is Integer type, if so just assign it to solution variable
        solution = initial_list[0]
    else: # if not it's probably float (mostly because of division), need to check if it can be converted to integer, if so do it, if not, just assign as float
        solution = int(initial_list[0]) if initial_list[0].is_integer() else initial_list[0]
    return solution
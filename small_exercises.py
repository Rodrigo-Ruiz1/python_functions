def madlib_prompt(name, subject):
    return("%s's favorite subject is %s" % (name, subject))

def madlib_input():
    name = input("Type a name ")
    subject = input("Type a subject ")

    print(madlib_prompt(name, subject))

# madlib_input()


def temp_conversion(c):
    return c * 9/5 + 32

def temperature_c():
    celsius = int(input("Enter a temperature in celsius "))
    print(temp_conversion(celsius))
#temperature_c()

def temp_conversion_two(f):
    return (f - 32) * 5/9

def temperature_f():
    fahrenheit = int(input("Enter a temperature in fahrenheit "))
    print(temp_conversion_two(fahrenheit))
#temperature_f()

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# number = int(input("Choose a number to see if it is even: "))
#print(is_even(number))



def is_odd(number):
    number = int(input("Enter a number to see if it is odd: "))
    



def only_evens(number):
    if number in list % 2:
        
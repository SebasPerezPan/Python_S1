## Complete Search

print('first argument: Value\nSecond Argument: function.\n 1.Prime Check.\n 2.Basic search for square.\n3. Check by Binary search')

def choose_algorithm(value, option):
    if option == 1:
        answer = (prime_check(value))
    elif option == 2:
        answer = (square_aproximity(value))
    else:
        answer = (binary_search(value))
    return answer

def prime_check(prime):
    '''
    Check if a number is prime or don't.
    prime int or float.
    returns true if is a prime number. Else if don't.
    '''
    counter = 2
    while prime % counter != 0: 
            counter += 1
    if counter == prime:
        return True
    else:
        return False

## Aproximity. Epsilon is how precise u wanna be.

def square_aproximity(square):
    epsilon = 0.01
    step = epsilon **2
    answer = 0.0
    while abs(answer**2 - square) >= epsilon and answer <= square:
        answer += step
    if abs(answer**2-square) >= epsilon:
        return False
    else:
        return answer

## Binary search

def binary_search(number_tosearch):
    epsilon = 0.01
    low = 0.0
    top = max(1.0 , number_tosearch)
    answer = (low + top) / 2
    while abs(answer**2 -number_tosearch) >= epsilon:
        if answer **2 < number_tosearch:
            low = answer
        elif answer**2 > number_tosearch: 
            top = answer
        answer = (low +top) /2
    return answer

print(choose_algorithm(12312412123123123312312, 3))
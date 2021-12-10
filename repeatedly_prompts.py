# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        value = int(num)
        if largest is None or largest < value:
            largest = value
        elif smallest is None or smallest > value:
            smallest = value
    except:
        print('invalid')
        continue
    
print('maximum is', largest)
print('munimum is', smallest)
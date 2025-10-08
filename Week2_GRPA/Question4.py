''' GrPA 4 - Conditionals - Applications - GRADED
Problem Type: Standard Output - Standard Output
# Question
You are tasked with creating a multi-purpose application that performs various operations based on user input. The application should take the operation name from the input and execute the corresponding task.

The operations your application should support are as follows:

Odd number checker: Check whether the input number is odd.
Name: odd_num_check
Inputs: number:int
Output: "yes" if the number is odd, "no" otherwise.
Perfect square checker: Check whether the input number is a perfect square.
Name: perfect_square_check
Inputs: number:int
Output: "yes" if the number is a perfect square, "no" otherwise.
Vowel checker: Check if a string has a vowel in it.
Name: vowel_check
Inputs: text:str
Output: "yes" if the string contains a vowel, "no" otherwise.
Divisibility checker: Check if a number is divisible by 2 or 3.
Name: divisibility_check
Inputs: number:int
Output: "divisible by 2" if the number is divisible by 2, "divisible by 3" if divisible by 3, "divisible by 2 and 3" if divisible by both, "not divisible by 2 and 3" otherwise.
Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
Name: palindrominator
Inputs: text:str
Output: string representing the input string joined with its reverse(the last characte should not be repeated twice)
Simple interest calculator with inputs with a higher interest rate if long term.
Name: simple_interest
Inputs: principal_amount:int, n_years:int (number of years)
Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
If the operation name is not any of the above print "Invalid Operation". '''
# Answer
operation = input()

if operation == "odd_num_check":
    number = int(input())
    if number % 2 != 0:
        print("yes")
    else:
        print("no")
elif operation == "perfect_square_check":
    number = int(input())
    import math
    if math.sqrt(number) == int(math.sqrt(number)):
        print("yes")
    else:
        print("no")
elif operation == "vowel_check":
    text = input()
    if any(char in "aeiouAEIOU" for char in text):
        print("yes")
    else:
        print("no")
elif operation == "divisibility_check":
    number = int(input())
    if number % 2 == 0 and number % 3 == 0:
        print("divisible by 2 and 3")
    elif number % 2 == 0:
        print("divisible by 2")
    elif number % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")
elif operation == "palindrominator":
    text = input()
    print(text + text[::-1][1:])
elif operation == "simple_interest":
    principal_amount = int(input())
    n_years = int(input())
    if n_years < 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.08
    simple_interest = (principal_amount * interest_rate * n_years)
    print(round(simple_interest))
else:
    print("Invalid Operation")
    
print(f"{total_cost:.02f}")

Problem Type: Standard Input - Standard Output

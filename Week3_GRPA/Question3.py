'''
GrPA 3 - Nested loops - GRADED
Question
Create a multi-functional program that performs different tasks based on the user input. The program should support the following tasks:

Permutation (permutation): Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.
Sorted Permutation (sorted_permutation): Given a string s, print all the possible two-letter permutations(without repetition) of the letters in the string where the first character comes before the second one in alphabetical order. The order in which the permutations are printed is same as the previous one (Type: Filtering).
Repeat the Repeat (repeat_the_repeat): Given a number n, print the numbers from 1 to n in the same line and repeat this n times.
Repeat Incrementally (repeat_incrementally): Given a number n, print a pattern where the k-th line contains the first k numbers and there are n lines in total. For example, if n is 4, the output should be:
1
12
123
1234
Increment and Decrement (increment_and_decrement): Given a number n, print a pattern where the k-th line should have the numbers from 1 to k and then back down to 1. For example, if n is 4, the output should be:
1
121
12321
1234321'''
#Answer
task = input()


if task == 'permutation':
    s = input()
    for i in s:
        for j in s:
            if (i != j):
                print(f'{i}{j}')

elif task == 'sorted_permutation':
    s = input()
    for i in s:
        for j in s:
            if ((i != j) and (i < j)):
                print(f'{i}{j}')

elif task == 'repeat_the_repeat':
    n = int(input())
    for i in range(1, n + 1):
        repeat_the_repeat = 0
        for j in range(1, n + 1):
            repeat_the_repeat = (repeat_the_repeat * 10) + j
        print(repeat_the_repeat)

elif task == 'repeat_incrementally':
    n = int(input())
    if (n > 0):
        repeat_incrementally = 0
        for i in range(1, n + 1):
            repeat_incrementally = (repeat_incrementally * 10) + i
            print(repeat_incrementally)

elif task == 'increment_and_decrement':
    n = int(input())
    if (n > 0):
        increment = ''
        for i in range(1, n + 1):
            increment = increment + str(i)
            decrement = increment[-2::-1]
            increment_and_decrement = increment + decrement
            print(increment_and_decrement) 

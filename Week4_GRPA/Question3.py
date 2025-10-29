'''
GrPA 3 - List and set application - GRADED
Question
Implement the following functions:

1.find_min: Find the minimum value in a list of integers.
Input: A list of integers.
Output: An integer, the minimum value in the list.
2.odd_increment_even_decrement_no_modify: Increment all the odd numbers in a list by 1 and decrement all the even numbers by 1, without modifying the original list.
Input: A list of integers.
Output: A new list of integers with the modified values.
3.odd_square_even_double_modify: Square all the odd numbers and double all the even numbers in a list, modifying the list in place.
Input: A list of integers.
Output: None (the input list is modified in place).
4.more_than_two_unique_vowels: Given a string of comma-separated words, return a set containing words that have more than two unique vowels.
Input: A string of comma-separated words.
Output: A set of words with more than two unique vowels.
5.sum_of_list_of_lists: Given a list of lists of integers, find the sum of all the integers in all the lists.
Input: A list of lists of integers.
Output: An integer, the sum of all the integers in the nested lists.
6.flatten: Flatten a list of lists into a single list.
Input: A list of lists.
Output: A single flattened list.
7.all_common: Find the common characters that are present in all strings in a list of strings and return them as a string in ascending order.
Input: A list of strings.
Output: A string containing common characters in ascending order.
8.vocabulary: Given a list of sentences (with only alphabets and spaces), find the vocabulary (list of unique words) and return it as a set. Convert all words to lowercase before adding to the vocabulary.
Input: A list of sentences.
Output: A set of unique words in lowercase.
'''
# Answer
min =  None

def find_min(items:list):
    if not items:
        return None
    minimum = items[0]
    for item in items[1:]:
        if item < minimum:
            minimum = item
    return minimum

def odd_increment_even_decrement_no_modify(items) -> list:
    return[(x + 1 if x % 2 != 0 else x - 1)for x in items]

def odd_square_even_double_modify(items:list) -> list:
    for i in range(len(items)):
        if items[i] % 2 != 0:
            items[i] = items[i] ** 2
        else:
            items[i] = items[i]*2

def more_than_two_unique_vowels(sentence):
    vowels = set('aeiou')
    result = set()
    words = sentence.split(',')
    for word in words:
        unique_vowels = set(char for char in word if char in vowels)
        if len(unique_vowels) > 2:
            result.add(word)
    return result

def sum_of_list_of_lists(lol):
    return sum(sum(lst) for lst in lol)

def flatten(lol):
     return [item for sublist in lol for item in sublist]

def all_common(strings):
    if not strings:
        return ''
    common_chars = set(strings[0])
    for s in strings[1:]:
        common_chars &= set(s)
    return ''.join(sorted(common_chars))

def vocabulary(sentences):
    vocab = set()
    for sentence in sentences:
        words = sentence.lower().split()
        vocab.update(words)
    return vocab

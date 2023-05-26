import os
import re
def reverse(string: str) -> str:
    reversed_string = ''
    i = 1
    for letter in string:
        reversed_string += string[-i]
        i=i+1
    return reversed_string

def is_palindrome(string: str) -> bool:
    if string == reverse(string):
        return True
    else:
        return False

def letter_frequency(string: str)->dict:
    letter_frequency_dict = {}
    for letter in string:
        if letter not in letter_frequency_dict.keys():
            letter_frequency_dict.update({letter: 1})
        else:
            letter_frequency_dict[letter]+=1
    return letter_frequency_dict


def is_anagram(string1: str , string2: str) -> bool:
    lfq1 = letter_frequency(string1)
    lfq2 = letter_frequency(string2)
    if sorted(lfq1.keys()) != sorted(lfq2.keys()):
        return False
    else:
        for key in lfq1.keys():
            if lfq1[key]!=lfq2[key]:
                return False
        return True
    
def starting_index_of_substring(string: str, sub_string: str) -> int|None:
    for start_index in range(len(string)):
        # making sure index is with in strings max index
        substring_window_max_index = start_index + len(sub_string) - 1
        max_string_index = len(string)-1
        if substring_window_max_index > max_string_index:
            return None
        window_sub_string = string[start_index:start_index + len(sub_string)]
        if window_sub_string == sub_string:
            return start_index
        
def word_with_first_letter_capital(string: str) -> str|None:
    space_pattern = "\s+"
    words = re.split(space_pattern, string)
    for word in words:
        if word[0].upper() == word[0]:
            return word




print(reverse('testing'))
print(is_palindrome("malayalam"))
print(letter_frequency('godd'))

print(is_anagram("malayalam", "malayaam"))

print(starting_index_of_substring('okiedokie' , 'edokie'))
print(word_with_first_letter_capital("all okie dokie Right?"))









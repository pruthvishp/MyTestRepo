class palindrome():
    def __init__(self, string: str):
        self.string = string
        self.is_palindrome()

    def string_reverse(self):
        reverse_string = ''
        i = 1
        for letter in self.string:
            reverse_string += self.string[-i]
            i = i+1
        print(f"reversed string is {reverse_string}")
        return reverse_string

    def is_palindrome(self):
        if self.string == self.string_reverse():
            print(f'{self.string} is a palindrome')
        else:
            print(f'{self.string} is Not a palindrome')

class anagram():
    def __init__(self, string1: str, string2: str):
        self.string1 = string1
        self.string2 = string2
        self.is_anagram()

    def letter_frequency_dict(self, string):
        letter_frequency = {}
        for letter in string:
            if letter not in letter_frequency:
                letter_frequency.update({letter: 1})
            else:
                letter_frequency[letter]+=1
        print(f'following is the letter frequency {letter_frequency}')
        return letter_frequency
    
    def is_anagram(self):
        lfq1 = self.letter_frequency_dict(self.string1)
        lfq2 = self.letter_frequency_dict(self.string2)
        if sorted(lfq1.keys()) == sorted(lfq2.keys()):
            for key,value in lfq1.items():
                if lfq2[key] != value:
                    print(f'{self.string1} and {self.string2} are not anagrams')
                    return False
            print(f'{self.string1} and {self.string2} are anagrams')
            return True            
        else:
            print(f'{self.string1} and {self.string2} are not anagrams')
            return False






obj_pal = palindrome("malayalama")
obj_ana = anagram("gode", "dog")





import re

class string_manip():
    def __init__(self, string):
        self.string = string

    def print_all_words_which_start_with_caps1(self):
        #works only if all words are made of alphabets only
        space_pattern = "\s+"
        words_of_string = re.split(space_pattern, self.string)
        caps_words_list = []
        for word in words_of_string:
            if word[0] == word[0].upper():
                caps_words_list.append(word)
        return caps_words_list
    
    def print_all_words_which_start_with_caps2(self):
        #works only if all words are made of alphabets only
        cap_word_pattern = "[A-Z]\S{0,}" #capital letter followed by non space character
        #words_of_string = re.split(space_pattern, self.string)
        caps_words_list = re.findall(cap_word_pattern, self.string)
        return caps_words_list

    


obj = string_manip("Whats your Name 0123 A")
print(obj.print_all_words_which_start_with_caps1())
obj1 = string_manip("Whats your Name    k0123 A   K0123 ")
print(obj1.print_all_words_which_start_with_caps2())

print(re.search("[A-Z]\S{0,}" , "Whats your Name    k0123 A   K0123"))
        

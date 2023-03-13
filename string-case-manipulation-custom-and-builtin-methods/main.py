#https://speakpython.codes/string-formatting/2023/03/12/string-case-manipulation-custom-and-builtin-methods.html#custom-text-case-conversion

class string:
    def __init__(self, given_string):
        self.given_string = given_string
    
    def uppercase(self):
        return self.given_string.upper()
    
    def lowercase(self):
        return self.given_string.lower()
    
    def titlecase(self):
        return self.given_string.title()
    
    def capitalcase(self):
        return self.given_string.capitalize()
    
    def swapcase(self):
        return self.given_string.swapcase()
    
    def sentencecase(self):
        split_chr = ['!', '?', '.']
        self.given_string = self.lowercase()
        for c in split_chr:
            after_dec = self.given_string.split(c)
            new_str = ""
            for a in range(len(after_dec)):
                if(len(after_dec[a]) > 0):
                    new_str += after_dec[a].strip()[0].upper() + after_dec[a].strip()[1:]
                    if (len(after_dec) != a + 1):
                        new_str += c + ' '
            self.given_string = new_str
        return self.given_string


#https://speakpython.codes/string-formatting/2023/03/12/string-case-manipulation-custom-and-builtin-methods.html#example-testing

text = string("hey There! hOW aRe yOU tOdaY? i hOPE yOU'rE dOING wELL.")
print(text.uppercase())
print(text.sentencecase())
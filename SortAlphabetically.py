#Works but not quite right
#Doesn't stop as soon as it's sorted
def alpha_bubble_sort(text):
    letter_codes = get_letter_codes(text)
    letter_codes = remove_spaces_punc(letter_codes)
    length = len(letter_codes)
    for z in range(0, length - 1):
        for i in range(0, length - 1):
            if letter_codes[i] > letter_codes[i+1]:
                hold = letter_codes[i+1]
                letter_codes[i+1] = letter_codes[i]
                letter_codes[i] = hold
    sorted_letters = letter_code_to_letters(letter_codes)
    return sorted_letters

#This works, uses ord to get the unicode code of each letter then puts them in a list.       
def get_letter_codes(text):
    text = text.lower()
    letter_codes = []
    for i in text:
        code = ord(i)
        letter_codes.append(code)
    return letter_codes

#Takes the sorted unicode code and uses chr to get corresponding letter.       
def letter_code_to_letters(letter_codes):
    sorted_letters = []
    for i in letter_codes:
        letter = chr(i)
        sorted_letters.append(letter)
    return sorted_letters

#Remove all non lowercase abc characters
def remove_spaces_punc(letter_codes):
    for i in letter_codes:
        if i < 97 or i > 122:
            letter_codes.remove(i)
    return letter_codes
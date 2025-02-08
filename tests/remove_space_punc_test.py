from SortAlphabetically import remove_spaces_punc

def test_remove_spaces_punc():
    letter_codes = [123, 100, 97, 122, 115]
    output = remove_spaces_punc(letter_codes)
    assert output == [100, 97, 122, 115]
    
def test_remove_spaces_punc_2():
    letter_codes = [123, 90, 95, 96, 97, 100]
    output = remove_spaces_punc(letter_codes)
    assert output == [97, 100]
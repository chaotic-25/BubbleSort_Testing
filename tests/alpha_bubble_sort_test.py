from SortAlphabetically import alpha_bubble_sort

def test_alpha_bubble_sort():
    text = 'cba'
    output = alpha_bubble_sort(text)
    assert output == ['a', 'b', 'c']
    
def test_with_punc():
    text = 'Hello!'
    output = alpha_bubble_sort(text)
    assert output == ['e', 'h', 'l', 'l', 'o']
    
def test_with_space():
    text = 'a f b c z k'
    output = alpha_bubble_sort(text)
    assert output == ['a', 'b', 'c', 'f', 'k', 'z']
    
def test_everything():
    text = '5673   !@£$%'
    output = alpha_bubble_sort(text)
    assert output == []
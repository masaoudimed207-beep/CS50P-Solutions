from plates import is_valid

def test_length():
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAAA") == True
    assert is_valid("AAAAA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_begins_with_letters():
    assert is_valid("AA123") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    
def test_zeros():
    assert is_valid("AA123") == True
    assert is_valid("AA012") == False
    assert is_valid("AA120") == True
    assert is_valid("AA120A") == False

def test_numbers():
    assert is_valid("AA123") == True
    assert is_valid("AA12A") == False
    assert is_valid("AA1A2") == False
    assert is_valid("AAA123") == True
    assert is_valid("AAA12A") == False
    assert is_valid("AAA1A2") == False

def test_ponctuation():
    assert is_valid("AA-123") == False
    assert is_valid("AA 123") == False
    assert is_valid("AA.123") == False
    assert is_valid("AA,123") == False
    assert is_valid("AA/123") == False
    assert is_valid("AA@123") == False
    assert is_valid("AA123!") == False
from numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.99.2.3") == True


def test_invalid_range():
    assert validate("256.1.1.1") == False
    assert validate("1.300.1.1") == False
    assert validate("1.1.1.512") == False

def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False

def test_non_numeric():
    assert validate("cat") == False
    assert validate("1.2.cat.4") == False
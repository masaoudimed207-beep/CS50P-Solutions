from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hi") == 20
    assert value("Hey") == 20
    assert value("Good morning") == 100
    assert value(" ") == 100
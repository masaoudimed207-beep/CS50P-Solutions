import pytest
from jar import Jar
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_custom = Jar(5)
    assert jar_custom.capacity == 5
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("invalid")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(7)  

# 4. Test dyal l-fkhakh d-withdraw
def test_withdraw():
    jar = Jar(10)
    jar.deposit(6)
    jar.withdraw(2)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(5)  
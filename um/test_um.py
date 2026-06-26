from um import count

def test_isolated_um():
    assert count("um") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um? Is this yummy um...") == 2

def test_inside_word():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
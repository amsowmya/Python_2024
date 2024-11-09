def add(a, b):
    return a+b


def test_add():
    assert add(2, 3) == 5
    assert add(10, 0) == 10

def test_add_big_number():
    assert add(200, 300) == 500
    assert add(10, 0) == 10
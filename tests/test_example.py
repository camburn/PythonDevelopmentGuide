import my_module.example as example

def test_fizzbuzz():
    """ Test the fizzbuzz function can return a standard result """
    expected = {
        1: '',
        2: '',
        3: 'fizz',
        4: '',
        5: 'buzz',
        6: 'fizz',
        7: '',
        8: '',
        9: 'fizz',
        10: 'buzz',
        11: '',
        12: 'fizz',
        13: '',
        14: '',
        15: 'fizzbuzz'
    }
    result = example.fizzbuzz(15)
    assert result == expected

def test_rectangle():
    expected_area = 10
    expected_perimeter = 14
    rect = example.Rectangle(2, 5)
    assert rect.area() == expected_area
    assert rect.perimeter() == expected_perimeter

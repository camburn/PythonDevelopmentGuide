"""
An example python project with optional typing
"""
import typing


class Rectangle:
    """ A Rectangle

    This rectangle has no defined units, ensure all provided values are of the
    same unit type.

    Attributes:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    """

    def __init__(self, length: float, width: float):
        """ Create a new Rectangle

        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """ Return the area of the rectangle

        Returns:
            float: The area of this rectangle
        """
        return self.length * self.width

    def perimeter(self) -> float:
        """ Return the permiter length of the rectangle

        Returns:
            float: The permiter of this rectangle
        """
        return 2 * (self.length + self.width)



def fizzbuzz(max_count: int) -> typing.Dict[int, str]:
    """ The classic programmer test!

    Generate a fizzbuzz dictionary with the results of the fizzbuzz test up to
    max_count items.

    Args:
        max_count (int): The maximum number of values to fizzbuzz against

    Returns:
        Dict[int, str]: A dictionary of values with the mapped string result.
            The result can take the form of; '', 'fizzbuzz', 'fizz', 'buzz'
    """
    data = {}
    for i in range(1, max_count+1):
        if i % 3 == 0 and i % 5 == 0:
            data[i] = 'fizzbuzz'
        elif i % 3 == 0 and i % 5 != 0:
            data[i] = 'fizz'
        elif i % 3 != 0 and i % 5 == 0:
            data[i] = 'buzz'
        else:
            data[i] = ''
    return data

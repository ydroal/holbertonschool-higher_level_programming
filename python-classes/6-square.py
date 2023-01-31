#!/usr/bin/python3
'''Module to define a square.'''


class Square:
    '''Define a square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize square with a given size.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square represented as a
                              tuple of 2 positive integers. Default is (0, 0).


        Raises:
            TypeError: If `size` is not an integer.
                       or if any element in `position` is not an integer.
            ValueError: If `size` is less than 0.
                        or if any element in `position` is less than 0.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        if not isinstance(position[0], int) or \
           not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        '''
        Instance method for calculate the current square area.

        Returns:
            int: the current square area.
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        Prints the square to stdout.
        The square is printed with the character '#' and
        is printed row by row. And spaces stands for its position.
        '''
        length = self.size
        space = self.position

        if length == 0:
            print()
            return
        else:
            for i in range(space[1]):
                print()
            for j in range(length):
                for k in range(space[0]):
                    print(' ', end='')
                for m in range(length):
                    print('#', end='')
                print()

    @property
    def size(self):
        '''
        Getter method for the value of the private attribute `__size`.

        Returns:
            int: The size of the object.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter method for the private attribute `__size`.
        It sets the size to the given value if it is an integer >= 0.

        Args:
            value (int): the new size to set

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        '''
        Getter method for the value of the private attribute `__position`.

        Returns:
            int: The value of position.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Setter method for the 'position' property.

        Raises:
            TypeError: If any element in the 'value' tuple is not an integer or
             if any element is negative.
        '''

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

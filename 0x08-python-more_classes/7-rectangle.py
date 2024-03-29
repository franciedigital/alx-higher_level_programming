#!/usr/bin/python3
"""
    This module contains a Rectangle class with
    width and height instance attribute and also
    a property and property setter
    The rectangle class has a public class method
    num_of_instances that increases when a new instance is
    created and reduces when an instanceis deleted
    It also has 2 public instance methods to get the area
    and perimeter of the rectangle and can be printed
    using print.
"""


class Rectangle:
    """
        A rectangle class with width and height properties
        and a perimeter and area methods and a class method
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a new instance """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ function to return the string representation """

        s = ""
        if self.perimeter() == 0:
            return s

        for i in range(self.__height):
            for j in range(self.__width):
                s += str(self.print_symbol)
            if i < self.__height - 1:
                s += "\n"

        return s

    def __repr__(self):
        """
            function to the return the string representation
            to be able to recreate a new instance
        """

        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

        return s

    def __del__(self):
        """ Calls when an instance is being deleted """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ Get the width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width property """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Get the height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height property """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Returns the area of the rectangle """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter of the rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
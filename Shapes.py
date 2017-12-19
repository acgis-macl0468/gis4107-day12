# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import math

def main():
    pass

def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass

class Circle(object):
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,radius):
        if radius <=0:
            raise ValueError, "Radius must be greater than 0!"
        else:
            self.__radius = radius

    @property
    def area(self):
        return (math.pi * self.__radius ** 2)
        return self.__area

    def __str__(self):
        return "Circle area with radius %s is %f." % (self.radius, self.area)

class Square(object):
    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self,side_length):
        if side_length <=0:
            raise ValueError, "Side must be greater than 0!"
        else:
            self.__side_length = side_length

    @property
    def area(self):
        return (self.side_length ** 2)
        return self.__area

    def __str__(self):
        return "Square area with side length %s is %f." % (self.side_length, self.area)

class Rectangle(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        if width <=0:
            raise ValueError, "Width must be greater than 0!"
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        if height <=0:
            raise ValueError, "Height must be greater than 0!"
        else:
            self.__height = height

    @property
    def area(self):
        return (self.__height * self.__width)
        return self.__area

    def __str__(self):
        return "Rectangle area with width %s and height %s is %f." % (self.width, self.height, self.area)

if __name__ == '__main__':
    main()
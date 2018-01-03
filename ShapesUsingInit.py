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
    def __init__(self):
        self.radius = 0



    @property
    def area(self):
        return (math.pi * self.radius ** 2)
        return self.__area

    def __str__(self):
        return "Circle area with radius %s is %f." % (self.radius, self.area)

class Square(object):
    def __init__(self):
        self.side_length = 0


    @property
    def area(self):
        return (self.side_length ** 2)
        return self.__area

    def __str__(self):
        return "Square area with side length %s is %f." % (self.side_length, self.area)

class Rectangle(object):
    def __init(self):
        self.height = 0
        self.width = 0



    @property
    def area(self):
        return (self.height * self.width)
        return self.__area

    def __str__(self):
        return "Rectangle area with width %s and height %s is %f." % (self.width, self.height, self.area)

if __name__ == '__main__':
    main()
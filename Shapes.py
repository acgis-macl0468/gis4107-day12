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
        #return self.__area

class Square:
    pass

class Rectangle:
    pass


if __name__ == '__main__':
    main()
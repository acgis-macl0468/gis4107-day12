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

def main():
    pass

def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass

class Point(object):
    def __init__(self, x, y):
        self.x = 1
        self.y = 1

class Line(object):
    def __init__(self, fromPoint, toPoint):
        self.fromPoint = fromPoint
        self.toPoint = toPoint

    @property
    def length(self):
        x1 = self.fromPoint.x
        y1 = self.fromPoint.y
        x2 = self.toPoint.x
        y2 = self.toPoint.y
        dist = (((x2-x1)**2 + (y2-y1)**2)**0.5)
        return dist

class Polyline(object):
    pass

if __name__ == '__main__':
    main()
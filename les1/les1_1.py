#!/usr/bin/env python3
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#while column < len(digits):  # 0 < 3                 1 < 3
#    number = int(digits[column])  # number = 1       number = 2
#    digit = Digits[number]  # digit = One          digit = Two
#    line += digit[row] + "   "  # line = " *    "   line = " ***    "
#    column += 1
import sys


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1] #123
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):  # 0 < 3                 1 < 3              while column < len(digits): # 0 < 3
            number = int(digits[column])  # number = 1       number = 2             number = int(digits[column]) #1
            digit = Digits[number]  # digit = One          digit = Two              digit = Digits[number] #One
            for Digit in digit[row]:  #   for Digit in digit[row]: #Digit в " * "
                if Digit == "*":      #   if Digit равен *
                    Digit = str(number)         # Digit = 1
                line += Digit                   # line = " 1 "
            line += "   "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: les1_1.py <number>")
except ValueError as err:
    print(err, "in", digits)

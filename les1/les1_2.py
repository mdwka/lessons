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

import random


def get_int(msg, minimum, default):
    while True:    #пока удовлетворяет условию
        try:       #попробовать
            line = input(msg)   #вводим соощение  #row 2
            if not line and default is not None:    #если значение нет сообщения и умолчание не None / если "" (True)
                                                    #и default(3) это не None (True) / True and True==True (1 и 1) == 1
                return default                      #вернуть значение по умолчанию в противном случаи  строка = 1
                                                    #row 2 / not 2 = False and None is not None = False (0 and 0) = 0
            i = int(line)                           #i = int(2) = 2 иначе идет на блок except и показывает ошибку
            if i < minimum:                         #если 2 < 1
                print("must be >=", minimum)        #написать что число должно быть больше 1
            else:
                return i                            #вернуть из функции 2
        except ValueError as err: #исключение ошибки
            print(err)


rows = get_int("rows: ", 1, None)                   #2
columns = get_int("columns: ", 1, None)             #2
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0)    #Enter по умолчанию 0

default = 1000
if default < minimum:   #если 1000 < 0
    default = 2 * minimum   #то умножаем максимум на два
maximum = get_int("maximum (or Enter for " + str(default) + "): ",
                  minimum, default)     #maximum (or Enter for 1000): 0, 1000
#row 2 column 2 mix-default(0) max-default(1000)
#        93        920
#       817        249
row = 0   #2
while row < rows:    #0-1
    line = ""
    column = 0
    while column < columns:         #0-1       #0                       #1
        i = random.randint(minimum, maximum)   #0 #1000 (93)            #(920)
        s = str(i)  #перевод в строку
        while len(s) < 10:                     #2 < 10                  #3 < 10
            s = " " + s      #" " + 93 = " 93"  #"  93" #"   93"        #"      920"
        line += s                              #"        93"            #       920"
        column += 1
    print(line)                                #"        93       920"
    row += 1                                   #        93       920
                                               #       817       249
#! /usr/bin/env python

num = 5

print (num)

while True:

    print ("in if {}".format(num))

    if (num % 2 == 0):
        num = num / 2
    else:
        num = num * 3 + 1

    if num == 1:
        break

print (num)

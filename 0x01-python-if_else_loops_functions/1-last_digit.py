#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
  reamin = number % -10
else:
  reamin = number % 10
if reamin > 5:
  print("Last digit of {:d} is {:d} and is greather than 5".format(number, reamin))
elif reamin == 0:
  print("Last digit of {:d} is {:d} and is 0".format(number, reamin))
else:
  print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, reamin))


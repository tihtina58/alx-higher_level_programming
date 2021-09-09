#!/usr/bin/python3
if __name__ == "__main__":
  from sys import argv
  sum = 0
  length = len(argv)
  if length == 1:
     print("0")
  else:
     for i in argv[1:]:
       sum = sum + int(i)
     print("{}".format(sum))

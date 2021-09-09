#!/usr/bin/python3
if __name__ == "__main__":
  import sys
  sum = 0
  length = len(sys.argv) - 1
  if length == 0:
     print("0")
  else:
     for i in sys.argv[1:]:
       sum = sum + int(i)
     print("{}".format(sum))

#!/usr/bin/python3
def uppercase(str):
    for T in str:
        print("{}".format(chr(ord(T) - 32)
                          if (ord(T) >= ord("a") and
                              ord(T) <= ord("z")) else l), end="")
    print()

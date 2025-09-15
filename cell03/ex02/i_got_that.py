#!/usr/bin/env python3

msg = input("What you gotta say? : ")

while True:
    print("I got that!", end=" ")
    if msg == "STOP":
        break
    msg = input("Anything else? : ")

#!/usr/bin/env python3

# ให้ผู้ใช้กรอกคำ (คั่นด้วย space)
text = input("Enter words separated by space: ").strip()

if not text:
    print("none")
else:
    words = text.split()
    printed = False
    for word in words:
        if not word.endswith("ism"):
            print(word + "ism")
            printed = True
    if not printed:
        print("none")

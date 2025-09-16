text = input("Enter words separated by space: ").strip()

if not text:
    print("none")
else:
    words = text.split()
    print(f"parameters: {len(words)}")
    for word in words:
        print(f"{word}: {len(word)}")

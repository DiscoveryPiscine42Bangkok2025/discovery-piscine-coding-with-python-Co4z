text = input("Enter your Text:")
words = text.split()      
word_count = len(words)
if word_count >=1:
    print(text.lower())
else:
    print("none")

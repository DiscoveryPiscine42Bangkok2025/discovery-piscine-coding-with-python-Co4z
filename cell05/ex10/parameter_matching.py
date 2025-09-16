params = input("Enter parameter(s): ").strip().split()

if len(params) != 1:
    print("none")
else:
    param = params[0]
    word = input("Enter a word: ").strip()

    if word == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

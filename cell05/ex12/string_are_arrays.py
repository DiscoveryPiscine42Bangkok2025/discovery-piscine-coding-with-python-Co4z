text = input("Enter a string: ").strip()

if not text:
    print("none")
else:
    zs = [ch for ch in text if ch.lower() == "z"]

    if zs:
        print("z" * len(zs))
    else:
        print("none")

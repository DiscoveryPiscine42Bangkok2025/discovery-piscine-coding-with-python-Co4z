words = input("ใส่ข้อความ (หลายคำได้): ").split()

if not words:
    print("none")
else:
    for word in words:
        if len(word) > 8:
            print(word[:8])  
        elif len(word) < 8:
            print(word + "Z" * (8 - len(word))) 
        else:
            print(word) 

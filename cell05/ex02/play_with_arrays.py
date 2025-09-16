# play_with_arrays.py

arr = [2, 8, 9, 48, 8, 22, -12, 2]

# filter เอาค่าที่มากกว่า 5
filtered = [x for x in arr if x > 5]

# แสดงผล
print(arr)
print([x + 2 for x in filtered])

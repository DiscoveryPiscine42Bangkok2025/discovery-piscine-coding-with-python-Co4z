nums = input("Enter two numbers separated by space: ").strip().split()

if len(nums) != 2:
    print("none")
else:
    try:
        start, end = map(int, nums)
        arr = list(range(start, end + 1))
        print(arr)
    except ValueError:
        print("none")

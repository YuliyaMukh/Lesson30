first = [1, 4,8,9,12,13,345,68,78]
second = [1,0,6,4,0,7,6,3]
for i in range(len(first)):
    try:
        print(f"{first[i]} / {second[i]} = {first[i]} / {second[i]}")
    except Exception as exc:
        print(repr(exc))

num = int(input("Sequence: "))

a, b = 0, 1
count = 0

if num <= 0:
    print("vali num ")
elif num == 1:
    print(a)
else:
    while count < num:
        print(a)
        total = a + b
        a = b
        b = total
        count += 1
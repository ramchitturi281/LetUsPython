num = int(input("Enter num: "))

if num > 1:
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            print(num ,"Not a prime")
            break
    else:
        print(num, "Is prime")
else:
    print("Not a prime number")
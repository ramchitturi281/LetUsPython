num = int(input("Enter new number: "))

for i in range(0,num):
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
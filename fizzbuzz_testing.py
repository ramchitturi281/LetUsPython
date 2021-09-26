num = int(input("Enter range :"))
for x in range(1,num + 1):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        #continue
    else:
        if x % 3 == 0:
            print("Fizz")
            #continue
        elif x % 5 == 0:
            print("BuZZ")
            #continue
    print(x)
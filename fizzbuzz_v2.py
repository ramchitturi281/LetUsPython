number = int(input("Enter a Number: "))

for i in range(1, number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        #continue
    elif i % 3 == 0:
        print("Fizz")
        #continue
    elif i % 5 == 0:
        print("Buzz")
        #continue
    else:
        print(i)
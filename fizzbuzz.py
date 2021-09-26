num = int(input("Enter Your Number : "))

def fizzbuzz(stdin):
    for i in range(1,stdin + 1):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
        else :
            print(str(i))
            
print(fizzbuzz(num))

""" Note: None appearing at the end we should use return 
https://stackoverflow.com/questions/16974901/python-script-returns-unintended-none-after-execution-of-a-function
"""
"""
#https://k3no.medium.com/fizz-buzz-in-python-2edea331d715#:~:text=The%20Fizz%20Buzz%20Coding%20Challenge,five%20print%20%E2%80%9CFizzBuzz%E2%80%9D.%E2%80%9D	
"""
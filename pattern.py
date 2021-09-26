# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
n = int(input("No of rows : "))
def pypart(n):

        # outer loop to handle number of rows
        # n in this case
        for i in range(0, n):

                # inner loop to handle number of columns
                # values changing acc. to outer loop
                for j in range(0, i+1):
                #for j in range(n, n-i):

                        # printing stars
                        print ("* ",end="")
                        #print( str(j + 1) + " " ,end="") # Working
                        #print( str(j + 1) + " ") #notworking
                        #print("\n") # not working

                # ending line after each row
                print("\r")

# Driver Code
#n = 5
pypart(n)
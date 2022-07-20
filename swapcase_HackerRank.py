def swap_case(s):
    s = str(s.swapcase())
    return s

if __name__ == '__main__':
    


string = 'HackerRank.com presents "Pythonist 2".'
#print(str(string))

#newstr=str(string.swapcase())

#print(newstr)

def swap_case(string):
    swapped = []

    for char in string:
        if char.islower():
            swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)

    return ''.join(swapped)
    
print(swap_case(string))
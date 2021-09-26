#https://stackoverflow.com/questions/16974901/python-script-returns-unintended-none-after-execution-of-a-function
def split_and_join(line):
    splits = line.split(" ")
    joins = "-".join(splits)
    return joins

line = "this is a string"
#split_and_join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
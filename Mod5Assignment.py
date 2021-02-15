
# 1. Write a Python program to execute a string containing Python code.

def outfun(x):
    def infun(y):
        x = 8
        return x * y
    return infun

test = outfun(4)

print(test(5))



# 2. Write a Python function to insert a string in the middle of a string

def update(str, str2):
    return str[:10] + str2 + str[-3:]

print(update('Python is fun', 'lots of '))
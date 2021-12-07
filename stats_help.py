import math

# square of a number
def numberSquare(num):
    """ Returns square of a number.
    Argument num must be int or float types"""
    try:
        return num ** 2
    except:
        return "num argument must be float or integer type."
    
# cube of a number
def numberCube(num):
    """ Returns cube of a number.
    Argument num must be int or float types"""
    try:
        return num ** 3
    except:
        return "num argument must be float or integer type."

# absolute value of a number
def numberAbsolute(num):
    """ Returns absolute value of a number.
    Argument num must be int or float types"""
    try:
        if num < 0:
            return num - (num *2)
        else:
            return num
    except:
        return "num argument must be float or integer type."

# factorial of a number
def numberFactorial(num):
    """ Returns factorial value of a number.
    Argument num must be int or float types"""
    try:
        multiple = num
        factorial = 1
        for x in range(num):
            factorial *= multiple
            multiple -= 1
        return factorial
    except:
        return "num argument must be float or integer type."

# mode of a list of numbers
def listMode(li):
    """ Returns Mode of a list numbers"""
    try:
        # print(li)
        result = [0, 0]
        for x in li:
            count_val = li.count(x)
            if count_val > result[1]:
                result[1] = count_val
                result[0] = x
        if result[1] == 1:
            return None
        else:
            return result[0]
    except:
        return "Liste objects must be float or integer types."
        
# average of a list of numbers
def listAverage(li):
    """ Returns average of a list of numbers """
    try:
        totalLen = len(li)
        return sum(li)/totalLen
    except:
        return "Liste objects must be float or integer types."

# minimum from a list of numbers
def listMinimum(li):
    """ Returns minimum value of a list of numbers """
    try:
        # print(li)
        minimum = li[0]
        for x in li:
            if minimum > x:
                minimum = x
        return minimum
    except:
        return "Liste objects must be float or integer types."
    
# maximum from a list of numbers
def listMaximum(li):
    """ Returns maximum value of a list of numbers """
    try:
        # print(li)
        maximum = li[0]
        for x in li:
            if maximum < x:
                maximum= x
        return maximum
    except:
        return "Liste objects must be float or integer types."

if __name__ == "__main__":
    numberSquare(5)
    numberCube(5)
    numberAbsolute(5)
    numberFactorial(5)
    listMode([1, 7, 13, 25])
    listAverage([1, 7, 13, 25])
    listMinimum([1, 7, 13, 25])
    listMaximum([1, 7, 13, 25])
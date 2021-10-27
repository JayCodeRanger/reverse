#To reverse an integer
def reverseInt(num):
    rev = 0
    while num != 0:
        rev = rev * 10 + num % 10
        num=int(num/10)
    return rev

#To reverse a string
def reverseStr(val):
    rev = ''
    for c in range(len(val)-1,-1,-1):
        rev += val[c]
    return rev


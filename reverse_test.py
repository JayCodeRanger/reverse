from reverse import *


number = int(input("Enter the number: "))
reverse_int = reverseInt(number)
print("Reversed integer: %d"% reverse_int)

value = input("Enter a string: ")
reverse_string = reverseStr(value)
print("Reversed string: %s"% reverse_string)
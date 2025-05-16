# greatest number of passed values

def Greatest(a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
    
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

print(Greatest (a, b, c))
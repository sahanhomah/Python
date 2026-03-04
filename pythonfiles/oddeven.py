def check(x):
    if x % 2 == 0:
        return "Even"       
    else:
        return "Odd"
n=int(input("Enter a number: "))
print(check(n))
try:

 number=int(input("Enter a number: "))
 result=10/number
 print("Result is:", result)
 file = open("data.txt", "r")
 print(file.read())
except (ZeroDivisionError, FileNotFoundError) :
    print("error found")
finally:
    print("Program finished")
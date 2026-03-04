# importing the module  
from calculator import add, subtract ,multiply, divide  
  
# initializing some variables  
num_1 = 16  
num_2 = 7  
  
# calling the functions of the module  
total = add(num_1, num_2)  
diff = subtract(num_1, num_2)   
prod = multiply(num_1, num_2)  
quot = divide(num_1, num_2)  
  
# printing results  
print(num_1, '+', num_2, '=', total)  
print(num_1, '-', num_2, '=', diff)  
print(num_1, '*', num_2, '=', prod)  
print(num_1, '/', num_2, '=', quot)  
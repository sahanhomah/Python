#without lambda
def add(x, y):
    return x + y
print(add(5, 3))

#with lambda
add = lambda x, y: x + y
print(add(5, 3))
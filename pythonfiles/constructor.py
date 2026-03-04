class student:
    def __init__(self,name="default"):
        
           self.name=name
     
s1=student("sahan")
print(s1.name)


class defaultconstructor:
 def __init__(self):
    print("here default constructor was called")

d1=defaultconstructor()
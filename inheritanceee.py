class vechile:
    def display(self):
        print("this is a vechile")

class vcar(vechile):
    def display(self):
        print("this is a vcar")


class car(vcar):

   def display(self):
        print("this is a car")
c1=car()
c1.display()
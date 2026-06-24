#single inheritence
'''class parent():
    def show(self):
        print("wel")
    
class child1(parent):
    def show1(self):
        print("not wel")
        
q = child1()
q.show() 
q.show1()'''

#multiple inheritence
'''class child1():
    def show1(self):
            print("child1")
            
class bro(child1):
    def show2(self):
            print("bro")
            
class grnd(bro , child1):
    def show3(self):
        print("grnd")
            
q = grnd()
q.show1()
q.show2()
q.show3()'''


#multi level 
'''
class parent():
    def show(self):
        print("parent")
class child(parent):
    def show1(self):
        print("child")
class child1(child):
    def show2(self):
        print("child1")
        
q = child1()
q.show()
q.show1()
q.show2()'''
    
#Hierarchical Inheritance

'''class parent():
    def show(self):
        print("parent")
class child(parent):
    def show1(self):
        print("child")
class child1(parent):
    def show2(self):
        print("child1")

c = child()
c1 = child1()
c.show()
c.show1()
c1.show()
c1.show2()'''

'''class Vehicle:
    def fuel(self):
        print("Runs on fuel")

class Car(Vehicle):
    def drive(self):
        print("Driving on 4 wheels")

class Truck(Vehicle):
    def haul(self):
        print("Hauling heavy cargo")

class Motorcycle(Vehicle):
    def wheelie(self):
        print("Riding on 2 wheels")
        
c = Car()
t = Truck()
m = Motorcycle()
c.drive()
c.fuel()
'''


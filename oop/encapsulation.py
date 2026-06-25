class parent():
    def __init__(self, name, age,school):
        self.name = name#public
        self._age = age#protected
        self.__school = school
        print("parent")
    
    def get_school(self):
        return self.__school
class child(parent):
    def __init__(self, name, age , school):
        super().__init__(name,age, school)        
        print("child bro")

#parant      
p = parent("rwf",34,"ec")
print(p.name)
print(p._age)
p = parent("hnm", 47,"ew")
print(p.name)
print(p._age)
print(p.get_school())
#child
c =child("dw", 93,"we")
print(c.name)
print(c._age)
print(c.get_school())

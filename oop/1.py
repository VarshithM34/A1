'''
class is a blueprint for creating objects.
constructor - all cls have fn called __init_(), which is always executed when cls is being initiated.
'''

'''#create class
class stu:
    name = "sri ram"
    age = "98"

#create object(instance)
s1 = stu()
print(s1.name)
print(s1.age)
'''
'''#__init__ constructor
class st2:
    name = "krishna"
    def __init__(self, age , time):#self parameter is a reference to current instance of cls, and is used to access variables that belongs to cls
        self.age = age
        self.time = time
        print(self)
        print("crete")
        
        
s2 = st2(2 , "three")
print(s2.age)
print(s2.name)
print(s2.time)
        '''
    
    
    
        
'''class st2:
    def __init__(self):#default constructors - it contain only one  parameter
        print("crete")#python create it automatically and it won't print
    date = 7 #will be same for s2 and s3 #cls attr
    
    def __init__(self, age , time):#parameterized constructors -  contains tow or more parameter
        self.age = age#obj attr
        self.time = time#obj attr > cls attr
        print(self)

        
        
s2 = st2(2 , "three")
print(s2.age)
print(s2.time)
s3 = st2(2, "two")
print(s3.age)
print(s3.time)
print(s2.date)'''

#methods
# it is functions that belongs to objects
'''class stu:
    def __init__(self , fullname , marks):
        self.name = fullname
        self.marks = marks

    
    def welcome(self):
        print("welcome ,", self.name)
        
    def get_marks(self):
        return self.marks
    
s1 = stu("king" , 10)
s1.welcome()  
print(s1.get_marks())'''

#static methods
#methods that don't use self parameter
'''class stu:
    @staticmethod
    def coll():
        print("abc")
        
stu.coll()'''
        
#abstraction - means hidden
# hiding implementation details of a cls and only showing essential features to user.
'''class car:
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = True
        
    def start(self):
        self.clutch = True
        self.accelerator = True
        print("car started")
        
        
car1 = car()
car1.start()
        '''
        
#encapsulation - wrapping data and functions in to a single unit(obj)

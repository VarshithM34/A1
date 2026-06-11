def user():
    print("hell no ")
user()

def user(name , age):
    print(f"my name is{  name} and age is {age}")
    
user("leo",19)

def cal_tax(prize):
    tax = prize + 100
    return tax

tol_tax = cal_tax(20)
print(tol_tax)

def make_moive(genor = "action" , hit = True):
    hit = "hit" if hit else "flop"
    print(f"it is a { genor} moive and it is {hit}")
    
make_moive("drama",True)

def test_func():
    pass

#print(dir(test_func))
#['__annotate__', '__annotations__', '__builtins__', '__call__', '__class__', '__closure__',  
#'__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__','__lt__', '__module__',
# '__name__', '__ne__', '__new__', '__qualname__', '__reduce__','__reduce_ex__', '__repr__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__']

def job(name, age ,role):
    return f"Name : {name}, Age : {age}, Role : {role}"

print(job("varshit",21,"director"))

def num(a,b,c):
    return f"A:{a},B:{b},C:{c}"
print(num("app","le","apple"))

def num(a, b, c):
    return a + b + c
   
print(num(a=10, b=34, c=90)) 

def num1(key1 = 10 , key2 = "rai" , key3 = "jai"):
    return f"key1: {key1}, key2 : {key2}, key3 : {key3}"
print(num1())

    
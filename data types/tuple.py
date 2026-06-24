#print(dir(tuple))
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', 'count', 'index']

name = ('John', 'Doe', 30, 'Engineer', 'Doe')
print(name.count('Doe'))
print(name.index('Doe'))

city = ('New York', 'Los Angeles','Chicago', 'Houston', 'Phoenix')
usa, canada, mexico, brazil, argentina = city
print(f"USA: {usa}, Canada: {canada}, Mexico: {mexico}, Brazil: {brazil}, Argentina: {argentina}")
#print(dir({}))
#['__class__', '__class_getitem__', '__contains__', '__delattr__', 
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__'
# , '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__',
# '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__',
# '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', 
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 
# 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
# 'setdefault', 'update', 'values']

car = {"brand": "Tesla", "model": "Model 3", "year": 2024}
print(car["brand"])
print(car.pop("model")) 
print(car.items())
print(car.keys())
print(car.values())

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"My name is {person['name']} and my age is {person['age']}")
print(person.popitem())

car.update(person)
print(car)
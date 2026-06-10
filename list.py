#print(dir(list))
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__'
# , '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append',
# 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list1 = ["peach", "grape"]
print(list.pop())
print(list.insert(2, "watermelon"))
print(list.remove("banana"))
print(list.append("strawberry"))
print(list.extend(list1))
list.sort()

print(list)
list2 = list.copy()
print(list2)
list3 = list1 + list2
print(list3)

#formatting list


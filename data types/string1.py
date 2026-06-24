name = "ming"

print(name[0])
name = "h" + name[1:]
print(name)

job = "programmer at google  !  "
print(job.upper())
print(job.lower())
print(job.title())
print(job.strip())
#print(dir(job))
print("hello\nworld")


place = "tenali"
place_1 = place.replace("tenali", "hyderabad")
print(place_1)

friut = "apple, banana, orange"
drinks = ["coke ", " pepsi", " sprite"]
friut1 = friut.split(", ")
print(friut1)

drinks1 = " water ".join(drinks)
print(drinks1)

num = "123"
print(num.isdigit())

name3 = "alicejohnson"
print(name3.isalpha())
print(name3.removeprefix("ali"))
print(name3.removesuffix("son"))


#formatting

name = "Alice"
age = "30"
print(f"my name is {name.upper()} and i am {age} years old")
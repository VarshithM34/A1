'''def app():
    print("ooh ya")
app()

def app(name, toll):
    print(f"hey {name}, {toll}")
app("atul","mg")

def cal_tax(price):
    tax = price * 0.05
    return tax
tol_tax = cal_tax(100)
print(tol_tax)


def cal_age(age):
    age = age + 5
    return age
tol_age = cal_age(10)
print(tol_age)



def tea(size, sugar = True):
    sugar = "with sugar" if sugar else "without sugar"
    print(f"this is a {size} tea and {sugar}")

tea("large", False)



def profile(name , age , city):
    return {name} , {age} , {city}
print(profile("atul", 19 , "tenali"))



def profile(name , age , city):
    return f"name {name} age {age} city {city}"
print(profile("atul", 19 , "tenali")) 



def num(a , b , c):
    return a + b + c
print(num(10 , 20 , 30)) 



def person(fav_num , age , year_born):
    lucy_num = fav_num - age + year_born
    return lucy_num
print(person(18, 21 , 2004))


#keyword argument
def person(fav_num , age , year_born):
    lucy_num = fav_num - age + year_born
    return lucy_num
print(person(age = 18,fav_num= 21 ,year_born = 2004))



#lambda

pit = lambda x: x+ x
print(pit(1))




products = [("Laptop", 1200), ("Mouse", 25), ("Monitor", 300)]

products.sort(key=lambda item: item[1])

print(products)


#map
rupe = [1000, 50000, 20]
yun = list(map(lambda x : x * 0.92 , rupe))
print(yun)

#filter
age = [1,18,31,15]

major = list(filter(lambda x : x >= 18 , age))
minor = list(filter(lambda x : x <18 , age ))
print(major)
print(f"minors  {minor}")


def convert_currency(amount , exchange_rate):
    return amount * exchange_rate
print(convert_currency(100 , 20))


prices = [10, 25, 50, 100]
total_cost = list(map(lambda x : x + 5 , prices))
print(total_cost)

def clean_text(raw_data):
    return raw_data.strip().lower()
print(clean_text("  Varshith"))
    



transactions = [("Keyboard", 120), ("Mouse", 20), ("Monitor", 350), ("Cable", 8)]
expensive_items = list(filter(lambda x : x[1] > 50 , transactions))
print(expensive_items)


def tol_sales(sales_lists):
    
    total = 0 
    for i in sales_lists:
        total += i
    return total
    
print(tol_sales([100,250,50,400]))
'''

def clean_database(dirty_list):
    dirty_list = dirty_list.strip().lower()
    return dirty_list
messy_names = ["  ALICE ", " bob   ", "  ChArLiE  "]
print(clean_database(messy_names))
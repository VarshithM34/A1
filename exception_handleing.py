'''
def divion(num1 ,num2):
    try:
        div = num1 / num2
        return div
    except ZeroDivisionError:
        print("waring")
        return 0
print(divion(100, 0))


def age(age):
    try:
        per = int(age)
        return age
    except ValueError:
        return "invaild"
print(age("ten "))


try :
    file = open("data.csv")
except FileNotFoundError:
    print("file not found")
finally :
    print("closing fike")
  '''
  
def get_price(item_prices, item_name):
    try:
        return item_prices[item_name]
    except KeyError:
        return "Item not found in menu!"
    except NameError:
        return " item not in"

menu = {"coffee": 3.5, "tea": 2.5}

print(get_price(menu, "coffee"))
print(get_price(menu, "sandwich"))
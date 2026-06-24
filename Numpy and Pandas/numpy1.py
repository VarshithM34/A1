import numpy as np
'''
add1 = np.array([10 ,20 , 30, 50 ,70])
add1 = add1 + 1
print(add1)
print(np.mean(add1))
print(np.max(add1))
print(np.std(add1)) # std = standard deviation

major = add1 >= 18
print(add1[major])
print(major)
print(add1[1:3])
print(add1[-2:])


store_sales = np.array([
    [10, 15, 20],
    [30, 35, 40],
    [50, 55, 60]
])
print(store_sales[: , 2])
print(store_sales[1:2])
print(store_sales[2])
print(store_sales[ : , 1])
print(store_sales[1,2])
print(np.mean(store_sales , axis = 0))
print(np.sum(store_sales, axis = 1))


traffic = np.array([1200, 2500, 1800, 3100, 2800, 1500, 900])
print(np.max(traffic))
dd = traffic > 2000
print(traffic[dd])

print(traffic[traffic > 2000])
print(traffic[traffic <= 1500])


#mising values

ratings = np.array([4.5, 5.0, np.nan, 3.8])
print(np.nanmean(ratings))
print(np.nansum(ratings))
print(np.nanmax(ratings))
print(np.nanmin(ratings))



flat_data = np.array([10, 20, 30, 40, 50, 60])
data = flat_data.reshape(2,3)
print(data)
'''

temps = np.array([32, 34, np.nan, 28, 30, 31, np.nan, 33])
print(np.nanmin(temps))


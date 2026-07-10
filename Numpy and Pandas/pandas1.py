# pandas - panel data structure
#used for data analysis and manipulation , data cleaning
#we pandas to work series and dataframes
#series - 1D array with index - single column in spreadsheet
#dataframe - 2D array with index and columns

import pandas as pd
'''data = [100 , 102 ,103]
series = pd.Series(data)
series1 = pd.Series(data, index = ["a","b","c"])
series2 = pd.Series(data, index = ["atul","biksu","corn"])
print(series)
print(series1)
print(series2)
print(series1.loc["c"])
series1.loc["c"] = 200
print(series1)
print(series.iloc[1])'''

'''data = [100,102,103,104,105,106]
series = pd.Series(data)
print(series[series <= 200])'''

'''calories = {"day1" : 1750 , "day2" : 1800 , "day3" : 1500}
series = pd.Series(calories)
print(series)
print(series.loc["day3"])
series.loc["day3"] += 500
print(series.loc["day3"])
print(series[series >= 2000])'''


#Dataframes

'''data  = {"name" : ["varshith","leo","munavath"],
         "age" : [21,19,60]}
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data , index = ["Student","Moster","intelletuval"])
print(df)
print(df.loc["Moster"])
print(df.iloc[2])

#add a new column
df["job"] = ["student" , "leader", "ubermuch"]
print(df)

#add a new row
new_row = pd.DataFrame([{"name":"MVV", "Age":35,"job" : "king"}], index = ["king"])
df = pd.concat([df , new_row])
print(df)

#add a new rows
mew_rows = pd.DataFrame([{"name":"Arjuna","age":40,"job":"follow"},{"name" : "krishna", "age" : 100 ,"job" : "uphold dharama"}],index = ["warrior", "protector"])
df = pd.concat([df , mew_rows])
print(df)
'''

df = pd.read_csv(r"C:\Users\len 25in\Documents\A1\Datasets\titanic.csv")
#print(df.to_string())#to print all values
'''print(df)
#selection By column
print(df["Survived"])
#print(df["Survived"].to_string())#to print all values
'''
#selection by rows
#print(df.loc[1])
#print(df.iloc[0:11])#firsr 10 rows
#print(df.iloc[0:11:2])#first 10 and skipping 2
print(df.iloc[0:11:2,0:3])#in first 10 and even from 0 to 3

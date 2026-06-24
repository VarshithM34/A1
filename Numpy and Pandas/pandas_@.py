import pandas as pd
data = {
    "prod" : ["lap" , "mos" , "dis"],
    "price" : [1200, 22 , 12],
    "unnits" : [5, 3, 7]
}
df = pd.DataFrame(data)
df["tol"] = df["price"] * df["unnits"]
'''
print(df)
print(df.head(1))
df.info()
print(df.describe())
'''
print(df[["price" , "tol"]])

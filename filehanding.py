with open("sample.txt","w") as file:
    file.write("data.\n")#creates txt file
    file.write("rows.\n")
with open("sample.txt", "a") as file:
    file.write("apple.\n")

'''with open("sample.txt","r") as file:
    lines = file.readlines()#creates list for data
    print(lines)'''
'''with open("sample.txt","w+") as file:
    file.write("hello pot")
    print(file.read())# over write everything
    file.seek(0)
    print(file.read())'''
with open("sample.txt", "r+") as file:
    file.seek(6)
    file.write("123")
    print(file.tell())
    file.seek(0)
    print(file.tell())
    file.write("0at")
    print(file.seek(0,1))# 1 = current position
    file.seek(0)
    print(file.seek(0,2))#0 = start  2 = end of data
    file.seek(14)
    file.write("APP")

    
    
    
with open("sample.txt","r") as file:
    print(file.read())#prints data

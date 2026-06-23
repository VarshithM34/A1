#create stu cls that takes name and marks of 3 sub as arguments in constructor.then create a method to print avg.

'''class stu:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi" , self.name , "avg is " , sum/3)

s1 = stu("king" , [99,98,97])
s1.get_avg()
s1.name = "joe"
s1.get_avg()'''
            
        
#create amount cls with 2 attributes - balance and account no.
#create methods for debit, credit and print balance

class account:
    def __init__(self , bal , acc):
        self.balance = bal
        self.account = acc
        
    def debit(self,amount):
        self.balance -= amount
        print("rs ", amount , "is debited")
        
    def credit(self , amount):
        self.balance += amount
        print(amount ," is credited")
        
    def get_balance(self):
        return self.balance
        
        
        
acc1 = account(100,198)
print(acc1.balance)
print(acc1.account)
acc1.debit(10)
print(acc1.get_balance())
acc1.credit(5)
print(acc1.get_balance())
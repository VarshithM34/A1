print("welcome to our Bank")
print("1.Login")
print("2.Register")
data = []
option =int(input("Enter your option: "))
current_user = None

if option == 1:
    print("Login")
    UserName = input("Enter your username: ").lower()
    Password = input("Enter your password: ").strip()

    for user in data:
        if user[username] == Username and user[password] == Password:
            print("loged in")
            current_user = user
elif option == 2:
    print("register")
    UserName = input("Enter your username: ")
    email = input("enter your email id:")
    deposit = float(input("enter amount to deposit:"))
    Password = input("Enter your password: ")
    user.append({'username':UserName,'email':email,'deposit':deposit,'password':Password})
    
    UserName = input("Enter your username: ")
    Password = input("Enter your password: ")

    for user in data:
        if user["username"] == UserName and user["password"] == Password:
            current_user = user
            print("Login successful")
            break

    if current_user is None:
        print("Invalid username or password")
        raise SystemExit

while True:
    print("Select an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    option = int(input("Enter your option: "))
    
    if option == 1:
        print(f"your balence is {current_user['deposit']}")
        
    elif option == 2:
        print("enter amount to Deposit")
        Deposit = float(input("Enter your deposit: "))
        current_user["deposit"] =+ deposit
        
    elif option == 3:
        print("enter amount to withdraw: ")
        withdraw = float(input("eneter amount: "))
        current_user["deposit"] -= withdraw
        
    else :
        break
        
     



    
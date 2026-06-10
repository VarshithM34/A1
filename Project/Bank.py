print("welcome to our Bank")
print("1.Login")
print("2.Register")
print("3.Exit")
data = []
option =int(input("Enter your option: "))
current_user = None

if option == 1:
    print("Login")
    UserName = input("Enter your username: ").lower()
    Password = input("Enter your password: ").strip()

    for user in data:
        if user["username"] == UserName and user["password"] == Password:
            current_user = user
            print("Loged in")
            break

    if current_user is None:
        print("Invalid username or password")

elif option == 2:
    print("Register")
    UserName = input("Enter your username: ").lower()
    Password = input("Enter your password: ").strip()
    Email = input("Enter your email: ")
    initial_deposit = float(input("Enter your deposit: "))
    data.append({"username": UserName, "password": Password, "email": Email, "deposit": initial_deposit})
    print("Registration successful")
    print("Now you can login!")

    UserName = input("Enter your username: ").lower()
    Password = input("Enter your password: ").strip()

    for user in data:
        if user["username"] == UserName and user["password"] == Password:
            current_user = user
            print("Login successful")
            break

    if current_user is None:
        print("Invalid username or password")
        raise SystemExit

elif option == 3:
    print("Thank you")
    exit()
    
    
while True:
    print("Select an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        print(f"Your balance is : {current_user['deposit']}")

    elif option == 2:
        print("enter amount to Deposit")
        Deposit = float(input("Enter your deposit: "))
        current_user["deposit"] += Deposit
        print(f"Deposit successful. New balance: {current_user['deposit']}")

    elif option == 3:
        print("Enter amount to Withdraw")
        Withdraw = float(input("Enter your withdraw amount: "))

        if Withdraw > current_user["deposit"]:
            print("Insufficient balance")
        else:
            current_user["deposit"] -= Withdraw
            print(f"Withdraw successful. New balance: {current_user['deposit']}")

    elif option == 4:
        break
    
    else :
        print("invail option")


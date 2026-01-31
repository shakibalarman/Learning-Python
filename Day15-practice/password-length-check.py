password = input ("Enter your password ")
if not password:
    print("Error: Your entered wrong password ")
elif len(password) < 8:
    print("Weak password: Password must be at least 8 characters long ")
else: 
    print ("Strong password : accepted ")
    
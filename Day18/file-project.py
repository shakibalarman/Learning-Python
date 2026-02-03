try:
    massage = input("Enter a massage for file ")
    if not massage:
        raise ValueError("Empty massage")
    with open("log.txt","a") as file:
        file.write(massage )
except ValueError:
    print("Error: massage cannot be empty ")
except PermissionError:
    print("Error: You don't have permission to write this file")

else:
    print("massage saved successfully")

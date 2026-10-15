correct_password = "cloud123"

password = ""  

while password != correct_password:
    password = input("Enter the password: ")
    if password != "cloud123":
        print("Incorrect password. Please try again.")  

print("Login successful!")
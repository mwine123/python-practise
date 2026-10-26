failed_attempts = 0

for attempts in range(1, 6):
    status = input(f"Enter login result {attempts}: ") 
    while status != "successful" and status != "failed":
        print("ERROR: Enter 'successful' or 'failed'")
        status = input(f"Enter login result {attempts}: ")    
    if status == 'failed':
        failed_attempts += 1

if failed_attempts >= 3:
    print("WARNING: Multiple failed login attempts detected!")
else:
    print("Login activity is normal.")
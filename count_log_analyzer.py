error_count = 0

for error in range(1, 6):
    log = input(f"Enter log message {error}: ")
    if log == "ERROR":
        error_count += 1

print(f"Total errors: {error_count}")
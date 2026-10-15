cpu_usage = input("Enter CPU usage %: ")

if int (cpu_usage) > 80:
    print("High CPU usage alert!")
else:
    print("CPU usage is normal.")
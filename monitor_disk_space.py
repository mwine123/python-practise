disk_usage = int(input("Enter disk usage %: "))

if disk_usage >= 90:
    print("CRITICAL: Disk usage is almost full!")
elif disk_usage >= 70:
    print("WARNING: Disk usage is high.")
else:
    print("Disk usage is healthy.")


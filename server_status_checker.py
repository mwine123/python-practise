server_status = input("Enter server status: ")

if server_status == "running":
    print("Server is healthy")
elif server_status == "stopped":
    print("Server is down")
else:
    print("Unknown server status")
    
for server in range(1, 4):
    status = input(f"Enter status for server {server}: ")
    if status == "running":
        print("Server is healthy")
    elif status == "stopped":
        print("Server is down")
    else:
        print("Unknown server status")
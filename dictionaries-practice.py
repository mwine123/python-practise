servers = {
    "web-server1": {
        "status": "running",
        "ip": "10.0.1.10",
        "cpu": 45
    },
    "web-server2": {
        "status": "stopped",
        "ip": "10.0.1.11",
        "cpu": 0
    },
    "database-server": {
        "status": "running",
        "ip": "10.0.1.12",
        "cpu": 68
    }
}


# I use the server name to access its status from the nested dictionary
for server in servers:
    print(f"{server}: {servers[server]['status']}")


# I use .items() because I need both the server name and its information
for server, details in servers.items():
    print(f"{server}: {details['status']}, IP: {details['ip']}, CPU Usage: {details['cpu']}%")


# I use .values() because I only need the information stored for each server
running_servers = 0

for details in servers.values():
    if details["status"] == "running":
        running_servers += 1

print(f"Number of running servers: {running_servers}")


# I use 'in' to check if a server exists before trying to access it
if "database-server" in servers:
    print("database-server exists")


# I add a new server by creating a new key and giving it its own dictionary of information
servers["app-server"] = {
    "status": "running",
    "ip": "10.0.1.13",
    "cpu": 32
}

print("\nAfter adding app-server:")

for server, details in servers.items():
    print(f"{server}: {details['status']}, IP: {details['ip']}, CPU Usage: {details['cpu']}%")


# I update the values of a server by accessing its key and changing the information
servers["web-server2"]["status"] = "running"
servers["web-server2"]["cpu"] = 25

print("\nAfter updating web-server2:")
print(servers["web-server2"])


# I use .get() to safely access a server without getting a KeyError if it does not exist
server = servers.get("backup-server")

if server:
    print(f"\nBackup server: {server}")
else:
    print("\nBackup server not found")


# I use .keys() when I only need the names of the servers
print("\nServer names:")

for server in servers.keys():
    print(server)


# I use .pop() when I want to remove a server from the dictionary
removed_server = servers.pop("app-server")

print(f"\nRemoved server: {removed_server}")


# I use .values() to check the CPU information for every server
highest_cpu = 0

for details in servers.values():
    if details["cpu"] > highest_cpu:
        highest_cpu = details["cpu"]

print(f"\nHighest CPU usage: {highest_cpu}%")
servers = {
    "web-server1": "running",
    "web-server2": "stopped",
    "database-server": "running"
}

running_servers = 0

for value in servers.values():
    if value == "running":
        running_servers += 1

print(f"Total running servers: {running_servers}")
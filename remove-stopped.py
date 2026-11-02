servers = {
    "web-server1": "running",
    "web-server2": "stopped",
    "database-server": "running"
}

for status in servers.values():
    if status == "stopped":
        del servers[status]

for item in servers.items():
    print(f"{item}")
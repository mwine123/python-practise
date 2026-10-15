failed_servers = 0

for server in range(1, 6):
    status = input(f"Enter status for server {server}: ")
    if status == "stopped":
        failed_servers += 1

print(f"Total failed servers: {failed_servers}")

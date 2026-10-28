server_statuses = ["running", "stopped", "running", "running", "stopped", "stopped", "running"]

running_servers = 0
stopped_servers = 0

for status in server_statuses:
    if status == "running":
        running_servers += 1
    elif status == "stopped":
        stopped_servers += 1

print(f"Total running servers: {running_servers}")
print(f"Total stopped servers: {stopped_servers}")
#!/usr/bin/env python3

while True:
    status = input("Enter service status (running/stopped/exit): ")
    if status == "exit":
        break
    elif status == "running":
        print("Service is healthy.")
    elif status == "stopped":
        print("Service is down.")
    else:
        print("Unknown service status.")

print("Monitoring stopped.")
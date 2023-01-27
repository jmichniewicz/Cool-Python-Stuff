import socket

# Get the hostname
hostname = socket.gethostname()

# Get the IP address
ip_address = socket.gethostbyname(hostname)

# Print the IP address
print(f"Your IP address is {ip_address}")

# Save the IP address to a file
with open("ip_address.txt", "w") as f:
    f.write(ip_address)

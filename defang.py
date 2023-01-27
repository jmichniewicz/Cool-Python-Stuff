import socket

host = socket.gethostname()
ip = socket.gethostbyname(host)

#print(ip)






#ip = input("Enter IP Address:  ")
defanged = ip.replace(".", "[.]")

print("The IP of this PC is: "+ip)
print("The Defanged IP of this PC is: "+defanged)
print("The hostname for this PC is: "+host)
import socket

# Create a socket object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
mysock.connect(('picoctf.org', 443))

# Send the HTTP GET request
request = "GET /resources.html HTTP/1.1\r\nHost: picoctf.org\r\n\r\n"
mysock.send(request.encode())

# Receive and print the response
while True:
    data = mysock.recv(512)
    if not data:
        break
    print(data.decode(), end='')

# Close the socket
mysock.close()




# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('picoctf.org', 443))
# mysock.send(b'GET https://picoctf.org/resources.html HTTP/1.0\n\n')
# #this is the same as cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0'.encode(); mysock.send(cmd) 
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()
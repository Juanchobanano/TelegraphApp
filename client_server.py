# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:51:50 2020

@author: Juan Esteban Cepeda
"""

import socket 

HOST = "127.0.0.1" # Symbolic name, meaning all available interfaces.
PORT = 9500

# Initializa socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client socket initialized!")

# Connect to host-port.
s.connect((HOST, PORT))
print("Socket client connected to port!")

# Send message.
message = "hello"
print("Sending message...")
s.sendall(bytes(message, "utf-8"))

# Close socket.
print("Closing socket...")
s.close()

print("All done!")

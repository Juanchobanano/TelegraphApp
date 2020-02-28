# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:51:50 2020

@author: Juan Esteban Cepeda
"""

import socket 


def sendMessage(morse_code):
    print("Sending message...")
    s.sendall(bytes(morse_code, "utf-8"))


HOST = "192.168.0.16" # Symbolic name, meaning all available interfaces.
PORT = 9500

# Initializa socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client socket initialized!")

# Connect to host-port.
s.connect((HOST, PORT))
print("Socket client connected to port!")

# Send message.
sendMessage("10102")
sendMessage("012")
sendMessage("0102")
sendMessage("0102")
sendMessage("1112")
sendMessage("3")

# Close socket.
print("Closing socket...")
s.close()

print("All done!")
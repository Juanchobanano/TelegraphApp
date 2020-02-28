# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:46:50 2020

@author: Juan Esteban Cepeda
"""

import socket
import morse_translator 
import sys

# Define host and port.
HOST = "192.168.0.16" # Symbolic name, meaning all available interfaces.
PORT = 9500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket & Translator created succesfully")

# Bind socket to local host and port.
try: 
    s.bind((HOST, PORT))
    print("Socket bind completed")
    
    # Start listening on socket (5 clients).
    s.listen(1)
    print("Socket now listening!")

except socket.error:
    print("Bind failed. Closing program...")
    s.close()
    exit
    
except:
    s.close()

# Accept connection.
conn, addr = s.accept()

# Initialize msg variable.
#msg = ""

while True: #contador < 100: #True: 
    
    try: 
        data = conn.recvfrom(1024)
        msg = data[0].decode("utf-8")
        morse_translator.processWord(msg)
        
        
    except KeyError:
        
        conn.send(str.encode("-1"))
        morse_translator.reset()
        
        pass
    
    except:
        
        e = sys.exc_info()[0]
        print(e)
        
        print("Client has disconnected...closing conn socket.")
        conn.close()
        break
    
# Close socket server.
s.close()
print("Socket server shut down!")
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:54:57 2020

@author: Juan Esteban Cepeda
"""

message = ""

MORSE_CODE = {
    "01":"A",
    "1000":"B",
    "1010":"C",
    "100":"D",
    "0":"E",
    "0010":"F",
    "110":"G",
    "0000":"H",
    "00":"I",
    "0111":"J",
    "101":"K",
    "0100":"L",
    "11":"M",
    "10":"N",
    "111":"O",
    "0110":"P",
    "1101":"Q",
    "010":"R",
    "000":"S",
    "1":"T",
    "001":"U",
    "0001":"V",
    "011":"W",
    "1001":"X",
    "1011":"Y",
    "1100":"Z",
    "01111":"1",
    "00111":"2",
    "00011":"3",
    "00001":"4",
    "00000":"5",
    "10000":"6",
    "11000":"7",
    "11100":"8",
    "11110":"9",
    "11111":"0",
    "000111000":"SOS", 
    "3": " "  # Espacio entre palabras.
}

def helloWorld():
    print("Hello world")
    
def translate(info):
    
    l = len(message)
    if message[l] == "2":
        message += MORSE_CODE[info[0: l - 1]]
        return True
    
    if message[l] == "3": 
        print(message)
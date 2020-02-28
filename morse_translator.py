# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:54:57 2020

@author: Juan Esteban Cepeda
"""

import speech

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
            "3": "_"  # Espacio entre palabras.
        }        


info = ""
message = ""
list_of_words = list()

def processWord(msg):
    
    global info 
    global message
    global list_of_words
        
    info += msg
    print(info)
    #print(message)
    
    if info[len(info) - 1] == "2": 
        
        if info == "2":
            info = ""
            pass
        
        else:
            message += MORSE_CODE[info[0: len(info) - 1]]
            info = ""
            print("Letra Detectada")
            print(message)
        
        
    elif info[len(info) - 1] == "3":
        
        if info == "3":
            info = ""
            pass
        else:
            print("Palabra Detectada")
            message += MORSE_CODE[info[0: len(info) - 1]]
            list_of_words.append(message)
            print(list_of_words)
            speech.talk(message)
            info = ""
            message = ""
            
def reset():
    
    global info 
    global message
    
    info = ""
       
def translateWordToMorse(word):
    
    morse_code = ""
    
    for i in range(0, len(word)):
        
        for mo, letter in MORSE_CODE.items():
            if letter == word[i]:
                if i == len(word) - 1:
                    morse_code += mo + "_3"
                else:
                    morse_code += mo + "2__"
    return morse_code


"""

CARRO
processWord("10102")        
processWord("012")  
processWord("0102")  
processWord("0102")  
processWord("1113")  

CAMINAR
processWord("10102")        
processWord("012")  
processWord("112")  
processWord("002")  
processWord("102")
processWord("012")        
processWord("0102")  

SOS
processWord("0001110003")  

DAVID
processWord("1002")        
processWord("012")  
processWord("00012")  
processWord("002")  
processWord("1003")

UBICADO
processWord("0012")        
processWord("10002")  
processWord("002")  
processWord("10102")  
processWord("012")
processWord("1002")  
processWord("1113")
"""

#print(translateWordToMorse("DAVIDCITO"))
#print(translateWordToMorse("DEBEN"))
print(translateWordToMorse("CECILIA"))

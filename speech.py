# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:00:39 2020

@author: Juan Esteban Cepeda
"""

from gtts import gTTS
import time
import os

language = "es"

def talk(myText):

    ouput = gTTS(text = myText, lang = language, slow = False)
    ouput.save("./output.mp3")
    os.system("start ./output.mp3")
    time.sleep(3)
    os.remove("./output.mp3")
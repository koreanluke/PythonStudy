from gtts import gTTS
from playsound import playsound
import os

text = '顏㣷㗿贳凹'
tts = gTTS(text = text , lang = 'ko')
#tts.save("./tovoice.mp3")

filename = "tovoice"
fileExtension = "mp3"
fillpath:str = fr"{os. getcwd()}{filename}.{fileExtension}".replace("\\","/")

tts.save(fillpath)
playsound(fillpath)

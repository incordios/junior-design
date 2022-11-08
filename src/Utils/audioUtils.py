from gtts import gTTS
from tempfile import NamedTemporaryFile
import pygame

# Functions
def speak(txt, lang='en'):
    gTTS(text=txt,lang=lang).write_to_fp(voice := NamedTemporaryFile())
    pygame.mixer.init()
    pygame.mixer.music.load(voice.name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    voice.close()

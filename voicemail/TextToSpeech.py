import hashlib
import os
import tempfile
import time

import pyglet
import pyttsx3
from gtts import gTTS

from config import LanguageConfig


class TextToSpeech:
    def __init__(self, text, language=LanguageConfig.text_to_speech_english) -> None:
        self.text = text
        self.lang = language
        self.file_address = self.__build_file_address()
        self.tts = gTTS(text=self.text, lang=self.lang)
        self.__save_to_file()
        speech = self.__to_speech()
        speech.play()
        time.sleep(speech.duration)

        # # self.tts.setProperty('voice', self.voices[1].id)
        # self.tts = pyttsx3.init()
        # # self.voices = self.tts.getProperty('voices')  # getting details of current voice
        # self.tts.say(self.text)
        # self.tts.runAndWait()

    def __build_file_address(self):
        return os.path.join(
            tempfile.gettempdir(),
            hashlib.md5(self.text.encode()).hexdigest() + '.mp3'
        )

    def __to_speech(self):
        return pyglet.media.load(self.file_address, streaming=False)

    def speak_out_loud(self):

        pass

    def __save_to_file(self):
        if not os.path.exists(self.file_address):
            self.tts.save(self.file_address)

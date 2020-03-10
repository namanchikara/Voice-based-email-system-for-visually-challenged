import time
import tempfile
import pyglet
import hashlib
import os
from gtts import gTTS
from voicemail.config import TextToSpeechConfig


class TextToSpeech:
    def __init__(self, text) -> None:
        self.text = text
        self.lang = TextToSpeechConfig.lang
        self.file_address = self.__build_file_address()
        self.tts = gTTS(text=self.text, lang=self.lang)
        self.__save_to_file()

    def __build_file_address(self):
        return os.path.join(
            tempfile.gettempdir(),
            hashlib.md5(self.text.encode()).hexdigest() + '.mp3'
        )

    def __to_speech(self):
        return pyglet.media.load(self.file_address, streaming=False)

    def speak_out_loud(self):
        speech = self.__to_speech()
        speech.play()
        time.sleep(speech.duration)

    def __save_to_file(self):
        if not os.path.exists(self.file_address):
            self.tts.save(self.file_address)

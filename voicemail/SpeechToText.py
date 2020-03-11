import speech_recognition as sr
from enum import Enum

from config import LanguageConfig
from TextToSpeech import TextToSpeech


class SpeechToText:
    def __init__(self, audio, language=LanguageConfig.speech_to_text_english):
        self.r = sr.Recognizer()
        self.audio = audio
        self.message = None
        self.language = language

    def convert_to_text(self):
        try:
            self.message = self.r.recognize_google(self.audio, language=self.language)
            return self.message + ' '
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said, Please say again.")
            TextToSpeech("Sorry, I didn't understand what you said, Please say again.").speak_out_loud()
            return SpeechError.UNKNOWN_VALUE_ERROR
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            TextToSpeech("Could not request results from Google Speech Recognition service; {0}".format(e)).speak_out_loud()
            return SpeechError.REQUEST_ERROR


class SpeechError(Enum):
    UNKNOWN_VALUE_ERROR = 1
    REQUEST_ERROR = 2

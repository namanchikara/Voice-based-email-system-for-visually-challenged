import speech_recognition as sr

from TextToSpeech import TextToSpeech


class Audio:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None

    def record(self):
        with sr.Microphone() as source:
            print("I'm listening, Go on")
            TextToSpeech("I'm listening, Go on").speak_out_loud()
            self.audio = self.r.listen(source)
            return self.audio

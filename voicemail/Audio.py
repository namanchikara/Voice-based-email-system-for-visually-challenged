import speech_recognition as sr


class Audio:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None

    def record(self):
        with sr.Microphone() as source:
            print("I'm listening, Go on")
            self.audio = self.r.listen(source)
            print("Done")
            return self.audio
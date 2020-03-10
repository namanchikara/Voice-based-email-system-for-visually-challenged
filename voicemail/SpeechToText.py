import speech_recognition as sr


class SpeechToText:
    def __init__(self, audio):
        self.r = sr.Recognizer()
        self.audio = audio
        self.msg = None

    def translate_to_text(self):
        try:
            self.msg = self.r.recognize_google(self.audio)
            return "You said : " + self.msg
        except sr.UnknownValueError:
            return "Sorry, I didn't understand what you said."
        except sr.RequestError as e:
            return "Could not request results from Google Speech Recognition service; {0}".format(e)

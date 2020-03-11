from TextToSpeech import TextToSpeech
from SpeechToText import SpeechToText
from Audio import Audio

from difflib import SequenceMatcher


class Recipient:
    def __init__(self):
        self.email_addresses = {
            "Naman": "singhnamanchikara@gmail.com",
            "Shantanu": "shantanublahblah@gmail.com",
            "exit": "exit"
        }

    def get_recipient(self):
        recipient_choice = self.__get_text_response_via_speech_recognition()
        if recipient_choice is None:
            self.get_recipient()
        print("Recipient " + recipient_choice)
        if self.similar(recipient_choice) is False:
            print("I didn't understand the name, Say again from one of the following names:" +
                  str(self.email_addresses.keys()))
            TextToSpeech("I didn't understand the name, Say again from one of the following names:" +
                         str(self.email_addresses.keys())).speak_out_loud()
            self.get_recipient()
        else:
            if self.similar(recipient_choice) == "exit":
                return None
            print("Do you want to send email to " + self.email_addresses[self.similar(recipient_choice)] +
                  " Say yes or no")
            TextToSpeech("Do you want to send email to " + self.email_addresses[self.similar(recipient_choice)] +
                         " Say yes or no").speak_out_loud()
            boolean_response = self.__get_boolean_response()
            if boolean_response.lower() == "yes":
                return self.email_addresses[self.similar(recipient_choice)]
            self.get_recipient()

    def __get_text_response_via_speech_recognition(self):
        response = SpeechToText(Audio().record()).convert_to_text()
        if isinstance(response, str) and not None:
            return response.strip()
        print("Something went wrong, retrying.")
        return self.__get_text_response_via_speech_recognition()

    def similar(self, choice):
        if choice is None:
            return False
        for option in self.email_addresses.keys():
            if SequenceMatcher(None, choice.strip().lower(), option.lower()).ratio() > 0.6:
                return option
        return False

    def __get_boolean_response(self):
        response = self.__get_text_response_via_speech_recognition()
        if response.lower() in ["yes", "no"]:
            return response
        return self.__get_boolean_response()

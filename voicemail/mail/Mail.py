import smtplib

from TextToSpeech import TextToSpeech
from mail.Compose import Compose
from SpeechToText import SpeechToText
from Audio import Audio


class Mail:
    def __init__(self, email, password, to_mail):
        self.email_address = email
        self.password = password
        self.email = Compose()
        self.to_email_address = to_mail

    def send_mail(self):
        print("Do you want to send this email? Say yes or no")
        TextToSpeech("Do you want to send this email? Say yes or no")
        via_speech_recognition = self.__get_text_response_via_speech_recognition()
        if via_speech_recognition == "yes":
            print("Sending mail")
            TextToSpeech("Sending mail").speak_out_loud()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.email_address, self.password)
            msg = 'Subject: {}\n\n{}'.format(self.email.subject, self.email.body)
            mail.sendmail(self.email_address, self.to_email_address, msg)
            print("Your mail has been sent.")
            TextToSpeech("Your mail has been sent.").speak_out_loud()
            mail.close()
        else:
            print("Mail discarded.")
            TextToSpeech("Mail discarded.").speak_out_loud()

    def __get_text_response_via_speech_recognition(self):
        response = SpeechToText(Audio().record()).convert_to_text()
        if isinstance(response, str) and not None:
            return response.strip()
        print("Something went wrong, retrying.")
        return self.__get_text_response_via_speech_recognition()

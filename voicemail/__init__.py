import sys
from pathlib import Path

from config import MailConfig
from mail.Mail import Mail
from mail.Recipient import Recipient

sys.path.extend([str(Path(sys.argv[0]).parent), str(Path(sys.argv[0]).parent.parent)])

from voicemail.Audio import Audio
from voicemail.SpeechToText import SpeechToText
from voicemail.TextToSpeech import TextToSpeech

__all__ = [
    Audio,
    SpeechToText,
    TextToSpeech
]


def loop():
    print("Welcome to voice based email")
    TextToSpeech("Welcome to voice based email").speak_out_loud()

    print("To whom do you want to send an email?")
    TextToSpeech("To whom do you want to send an email?").speak_out_loud()
    recipient = Recipient().get_recipient()
    if recipient is not None:
        Mail(MailConfig.email, MailConfig.password, recipient).send_mail()
    else:
        loop()


if __name__ == '__main__':
    loop()

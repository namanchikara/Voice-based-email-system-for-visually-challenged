import sys
from pathlib import Path

from config import MailConfig
from mail.Mail import Mail

sys.path.extend([str(Path(sys.argv[0]).parent), str(Path(sys.argv[0]).parent.parent)])

from voicemail.Audio import Audio
from voicemail.SpeechToText import SpeechToText
from voicemail.TextToSpeech import TextToSpeech

__all__ = [
    Audio,
    SpeechToText,
    TextToSpeech
]

if __name__ == '__main__':
    TextToSpeech("Welcome to voice based email").speak_out_loud()
    Mail(MailConfig.email, MailConfig.password, 'singhnamanchikara@gmail.com').send_mail()


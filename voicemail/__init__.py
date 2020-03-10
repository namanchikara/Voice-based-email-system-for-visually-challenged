import sys
from pathlib import Path

sys.path.extend([str(Path(sys.argv[0]).parent), str(Path(sys.argv[0]).parent.parent)])

from voicemail.Audio import Audio
from voicemail.SpeechToText import SpeechToText
from voicemail.TextToSpeech import TextToSpeech

__all__ = [
]

if __name__ == '__main__':
    recorded_audio = Audio().record()
    response_to_recorded_audio = SpeechToText(recorded_audio).translate_to_text()
    print(response_to_recorded_audio)
    TextToSpeech(response_to_recorded_audio).speak_out_loud()
    pass

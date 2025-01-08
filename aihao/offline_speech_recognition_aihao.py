import time

from vosk import KaldiRecognizer
import pyaudio
import json
from aihao import vosk_model


class OfflineSpeechRecognition:
    def __init__(self):
        self.model = vosk_model  # Path to Vosk model directory
        self.recognizer = KaldiRecognizer(self.model, 16000)

    def record_audio(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
        stream.start_stream()
        print("Say something!")

        while True:
            data = b''  # Reset data to an empty byte string at the start of the loop
            data = stream.read(4096, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                print("You said:", result.get("text", ""))
                return result.get("text", "")
            # Optionally sleep briefly to reduce CPU usage
            time.sleep(0.01)


def main():
    offline_audio_recognizer = OfflineSpeechRecognition()
    offline_audio_recognizer.record_audio()


if __name__ == "__main__":
    main()
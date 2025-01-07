from vosk import Model, KaldiRecognizer
import pyaudio
import json
from aihao import vosk_model

class OfflineSpeechRecognition:
    def __init__(self):
        self.model = vosk_model  # Path to Vosk model directory
        self.recognizer = KaldiRecognizer(self.model, 16000)

    def record_audio(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()
        print("Say something!")

        while True:
            data = stream.read(8192, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                print("You said:", result.get("text", ""))
                return result.get("text", "")


def main():
    offline_audio_recognizer = OfflineSpeechRecognition()
    offline_audio_recognizer.record_audio()

if __name__ == "__main__":
    main()
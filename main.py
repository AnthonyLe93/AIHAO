from audio_engine import AudioEngine
from greeting import Greeting
from speech_recognition import SpeechRecognition


def main():
    audio_engine = AudioEngine()
    audio_engine.assistant_response("Hello Anthony, what can i do for you?")
    audio_regcognizer = SpeechRecognition()
    audio_regcognizer.record_audio()
    greeting = Greeting()
    while True:
        text = audio_regcognizer.record_audio()
        responses = ''

        if greeting.wake_word(text.lower()) == True:
            try:
                responses = responses + greeting(text)
            except Exception as e:
                responses = responses + ''


if __name__ == "__main__":
    main()
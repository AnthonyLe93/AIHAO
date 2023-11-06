import pyttsx3

class AudioEngine:
    """
        This class initialised audio engine and enable machine to
        output speech.
    """
    def __init__(self):
        self.engine = pyttsx3.init()

    def assistant_response(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


def main():
    audio_engine = AudioEngine()
    audio_engine.assistant_response("Hello Anthony, what can i do for you?")


if __name__ == "__main__":
    main()



import importlib
import signal
import pyttsx3

class AudioEngine:
    """
        This class initialised audio engine and enable machine to
        output speech.
    """
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.voiceFemales = filter(lambda v: v.gender == 'VoiceGenderFemale', self.voices)
        self.voices_id_list = []
        # Set up signal handler for SIGINT
        signal.signal(signal.SIGINT, self.handle_sigint)

    @staticmethod
    def handle_sigint(signum, frame):
        # Handle the SIGINT signal (Ctrl+C)
        print("Received SIGINT. Exiting...")
        # Add any cleanup code if needed
        exit()

    def get_voices(self, text='Hello Anthony'):
        try:
            for voice in self.voiceFemales:
                print("Voice Name:", voice.name)
                print("Voice ID:", voice.id)
                print("Age:", voice.age)
                print("Gender:", voice.gender)
                print("Languages Supported:", voice.languages)
                print("\n")
                self.engine.setProperty('voice', voice.id)
                self.engine.say(text)
                self.engine.runAndWait()
                self.voices_id_list.append(voice.id)
        except KeyboardInterrupt:
            # Handle KeyboardInterrupt (Ctrl+C)
            print("Received KeyboardInterrupt. Exiting...")
            # Add any cleanup code if needed
            exit()
        return self.voices_id_list

    def set_voice(self, voice_id=None):
        if voice_id:
            self.engine.setProperty('voice', voice_id)
            self.engine.setProperty('rate', 200)
            self.engine.setProperty('pitch', 0.8)
            print('new voice set!')
            return True
        else:
            self.engine.setProperty('rate', 220)
            self.engine.setProperty('pitch', 0.8)
            print('using default voice!')
            return False

    def assistant_response(self, text):
        importlib.reload(pyttsx3)
        self.engine.say(text)
        self.engine.runAndWait()


def main():
    audio_engine = AudioEngine()
    audio_engine.set_voice(voice_id='com.apple.voice.compact.pt-PT.Joana')
    audio_engine.assistant_response("Hello Anthony, what can I do for you?")


if __name__ == "__main__":
    main()



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

    def get_voices(self, text='Hello Anthony'):
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
        return self.voices_id_list

    def set_voice(self, voice_id='com.apple.voice.compact.ja-JP.Kyoko'):
        self.engine.setProperty('voice', voice_id)

    def assistant_response(self, text):
        self.set_voice()
        self.engine.say(text)
        self.engine.runAndWait()


def main():
    audio_engine = AudioEngine()
    audio_engine.assistant_response("Hello Anthony, what can I do for you?")


if __name__ == "__main__":
    main()



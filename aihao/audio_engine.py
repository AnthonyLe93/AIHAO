import importlib

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

    def set_voice(self, voice_id=None):
        if voice_id:
            id_ = voice_id
            self.engine.setProperty('voice', id_)
            self.engine.setProperty('rate', 200)
            self.engine.setProperty('pitch', 0.8)
        else:
            print('using default voice')
            self.engine.setProperty('rate', 220)
            self.engine.setProperty('pitch', 0.8)
    def assistant_response(self, text):
        importlib.reload(pyttsx3)
        self.set_voice()
        self.engine.say(text)
        self.engine.runAndWait()


def main():
    audio_engine = AudioEngine()
    audio_engine.assistant_response("Hello Anthony, what can I do for you?")


if __name__ == "__main__":
    main()



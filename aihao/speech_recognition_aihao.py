import speech_recognition as sr
from aihao.audio_engine import AudioEngine

class SpeechRecognition:
    """
        This class creates a speech recognizer object and opens the microphone.
        it then saves the recognized text or output appropriate exception.
    """
    def __init__(self):
        # Record The Audio
        self.recognizer = sr.Recognizer()  # Creating a recognizer object
        self.audio = None

    def record_audio(self):
        # Open the microphone and start recording
        with sr.Microphone() as source:
            print('Say something!')
            self.audio = self.recognizer.listen(source)

        # Use google's speech recognition
        data = ''
        try:
            data = self.recognizer.recognize_google(self.audio)
            print('You said: ' + data)
        except sr.UnknownValueError:  # Checking for unknown errors
            print('Google Speech Recognition could not understand the audio')
            machine_reponse = AudioEngine()
            machine_reponse.assistant_response('Sorry, i could not understand what you said, please repeat!')
        except sr.RequestError as c:
            print('Request results from Google Speech Recognition service error')
            machine_reponse = AudioEngine()
            machine_reponse.assistant_response('Sorry, my speech recognition function is not working at the moment,'
                                               'please try again later!')

        return data

def main():
    audio_regcognizer = SpeechRecognition()
    audio_regcognizer.record_audio()

if __name__ == "__main__":
    main()


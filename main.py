from audio_engine import AudioEngine
from greeting import Greeting
from speech_recognition_aihao import SpeechRecognition
from offline_speech_recognition_aihao import OfflineSpeechRecognition
from util_funtions.date_time_aihao import get_date
import time


greeting_prompts = 'data/greeting_prompts.txt'

def main():
    audio_engine = AudioEngine()
    audio_recognizer = SpeechRecognition()
    offline_audio_recognizer = OfflineSpeechRecognition()
    speak = Greeting()

    while True:
        text = offline_audio_recognizer.record_audio()
        # Process the recognized text and generate responses
        responses = ''
        if text:
            if speak.wake_word(text):
                speak.random_greetings(greeting_prompts)
                responses = responses + speak.greeting()
            if 'date' in text:
                today_date = get_date()
                responses = responses + ' ' + today_date
            if responses == '':
                responses = responses + "I'm Sorry I Can't Do That Yet"

            # Response
            audio_engine.assistant_response(responses)
            time.sleep(1)  # Check for audio every 1 second
        else:
            print("No audio input detected.")
            print("----------------------------")


if __name__ == "__main__":
    main()
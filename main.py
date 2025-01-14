from audio_engine import AudioEngine
from greeting import Greeting
from offline_speech_recognition_aihao import OfflineSpeechRecognition
from util_funtions.date_time_aihao import get_date
from util_funtions.llm_model_download import load_model_and_generate

def main():
    audio_engine = AudioEngine()
    offline_audio_recognizer = OfflineSpeechRecognition()
    speak = Greeting()
    speak.load_greetings()

    while True:
        text = offline_audio_recognizer.record_audio()
        # Process the recognized text and generate responses
        responses = ''
        if text:
            if speak.wake_word(text):
                speak.random_greetings()
                responses += speak.greeting()
            elif 'date' in text or 'day' in text:
                today_date = get_date()
                responses += today_date
            elif 'stop' in text or 'goodbye' in text:  # Check if the "stop" or "goodbye" keyword is present
                responses += speak.goodbye()
                audio_engine.assistant_response(responses)
                break
            else:
                responses += load_model_and_generate(text)
            # Response
            audio_engine.assistant_response(responses)
        else:
            print("No audio input detected.")

        print("----------------------------")

if __name__ == "__main__":
    main()
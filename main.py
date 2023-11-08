from audio_engine import AudioEngine
from greeting import Greeting
from speech_recognition_aihao import SpeechRecognition
from util_funtions.date_time_aihao import get_date


def main():
    audio_engine = AudioEngine()
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
        if 'date' in text:
            today_date = get_date()
            responses = responses + ' ' + today_date
        if responses == '':
            responses = responses + "I'm Sorry I Can't Do That Yet"

        # Response
        audio_engine.assistant_response(responses)


if __name__ == "__main__":
    main()
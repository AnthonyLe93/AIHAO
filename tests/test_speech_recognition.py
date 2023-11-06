import pytest
from aihao.speech_recognition import SpeechRecognition

@pytest.mark.speech_recognition
class TestSpeechRecognition:
    @pytest.fixture(scope='class')
    def speech_recognition_obj(self):
        speech_recognition = SpeechRecognition()
        return speech_recognition
    def test_speech_recognition(self, speech_recognition_obj):
        pass

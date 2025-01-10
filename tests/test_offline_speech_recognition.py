import pytest
from aihao.offline_speech_recognition_aihao import OfflineSpeechRecognition

@pytest.mark.speech_recognition
class TestOfflineSpeechRecognition:
    @pytest.fixture(scope='class')
    def offline_speech_recognition_obj(self):
        offline_speech_recognition = OfflineSpeechRecognition()
        return offline_speech_recognition

    def test_speech_recognition(self, offline_speech_recognition_obj):
        pass
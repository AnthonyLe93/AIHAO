import pytest
from aihao.audio_engine import AudioEngine


@pytest.mark.audio_engine
class TestAudioEngine:
    @pytest.fixture(scope='class')
    def audio_engine_obj(self):
        audio_engine = AudioEngine()
        return audio_engine
    def test_audio_engine(self, audio_engine_obj):
        pass
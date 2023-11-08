import pytest
from aihao.audio_engine import AudioEngine
from unittest.mock import Mock

@pytest.mark.audio_engine
class TestAudioEngine:
    @pytest.fixture(scope='class')
    def audio_engine_obj(self):
        audio_engine = AudioEngine()
        return audio_engine
    def test_get_voices(self, audio_engine_obj):
        # Mock the 'voiceFemales' attribute to return a list of mocked voice objects
        mocked_voice = Mock()
        mocked_voice.name = "Mocked Voice"
        mocked_voice.id = "mocked_id"
        mocked_voice.age = 30
        mocked_voice.gender = "VoiceGenderFemale"
        mocked_voice.languages = ["English"]
        audio_engine_obj.voiceFemales = [mocked_voice]
        # Mock the 'engine' attribute methods to check if they are called
        audio_engine_obj.engine.setProperty = Mock()
        audio_engine_obj.engine.say = Mock()
        audio_engine_obj.engine.runAndWait = Mock()

        # Call the method under test
        voices_id_list = audio_engine_obj.get_voices(text='Hello Anthony')

        # Assertions
        assert voices_id_list == ["mocked_id"]

        # Check if the 'engine' attribute methods were called as expected
        audio_engine_obj.engine.setProperty.assert_called_with('voice', 'mocked_id')
        audio_engine_obj.engine.say.assert_called_with('Hello Anthony')
        audio_engine_obj.engine.runAndWait.assert_called_once()
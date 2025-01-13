import pytest
from aihao.speech_recognition_aihao import SpeechRecognition
from unittest.mock import patch
from speech_recognition import Recognizer, UnknownValueError, RequestError
from aihao.audio_engine import AudioEngine


@pytest.mark.speech_recognition
class TestSpeechRecognition:
    # Fixtures for mocking objects
    @pytest.fixture
    def mock_audio_engine(self):
        with patch.object(AudioEngine, 'assistant_response') as mock_assistant_response:
            yield mock_assistant_response

    @pytest.fixture
    def mock_recognizer(self):
        with patch.object(Recognizer, 'recognize_google') as mock_recognize_google:
            yield mock_recognize_google

    @pytest.fixture
    def speech_recognition_obj(self, mock_audio_engine):
        return SpeechRecognition()

    def test_record_audio_success(self, speech_recognition_obj, mock_recognizer):
        """
        Cannot effectively mock microphone behaviour because the listen method expect an actual audio input not a simple
        mock object
        """
        # Test case where speech is successfully recognized
        mock_recognizer.return_value = 'Hello'  # Mocking recognize_google to return 'Hello'

        result = speech_recognition_obj.record_audio()

        assert result == 'Hello'
        mock_recognizer.assert_called_once()

    def test_record_audio_unknown_value_error(self, speech_recognition_obj, mock_recognizer, mock_audio_engine):
        # Test case where speech recognition fails with UnknownValueError
        mock_recognizer.side_effect = UnknownValueError  # Simulate UnknownValueError

        # Call the method
        speech_recognition_obj.record_audio()

        # Verify the assistant response was called for the error case
        mock_audio_engine.assert_called_once_with('Sorry, i could not understand what you said, please repeat!')

    def test_record_audio_request_error(self, speech_recognition_obj, mock_recognizer, mock_audio_engine):
        # Test case where speech recognition fails with RequestError
        mock_recognizer.side_effect = RequestError  # Simulate RequestError

        # Call the method
        speech_recognition_obj.record_audio()

        # Verify the assistant response was called for the error case
        mock_audio_engine.assert_called_once_with(
            'Sorry, my speech recognition function is not working at the moment, please try again later!')
import pyaudio
import pytest
from aihao.offline_speech_recognition_aihao import OfflineSpeechRecognition
from unittest.mock import patch, MagicMock

@pytest.mark.offline_speech_recognition
class TestOfflineSpeechRecognition:

    @pytest.fixture
    def mock_kaldi_recognizer(self):
        """Mock KaldiRecognizer."""
        with patch('aihao.offline_speech_recognition_aihao.KaldiRecognizer') as mock_recognizer:
            mock_instance = MagicMock()
            mock_instance.AcceptWaveform.side_effect = [False, False, True]  # Simulate processing before success
            mock_instance.Result.return_value = '{"text": "hello world"}'  # Simulated result
            mock_recognizer.return_value = mock_instance
            yield mock_instance

    @pytest.fixture
    def mock_pyaudio(self):
        """Mock PyAudio."""
        with patch('aihao.offline_speech_recognition_aihao.pyaudio.PyAudio') as mock_pyaudio:
            mock_pyaudio_instance = MagicMock()
            mock_stream = MagicMock()
            mock_stream.read.return_value = b'\x00\x00\x00\x00' * 1024  # Simulated audio data
            mock_pyaudio_instance.open.return_value = mock_stream
            mock_pyaudio.return_value = mock_pyaudio_instance
            yield mock_pyaudio_instance

    @pytest.fixture
    def offline_speech_recognition_obj(self, mock_kaldi_recognizer):
        """Fixture for OfflineSpeechRecognition object."""
        return OfflineSpeechRecognition()

    def test_record_audio_success(self, offline_speech_recognition_obj, mock_kaldi_recognizer, mock_pyaudio):
        """Test that the record_audio method successfully recognizes speech."""
        result = offline_speech_recognition_obj.record_audio()

        # Validate the recognition result
        assert result == "hello world"

        # Ensure AcceptWaveform was called multiple times
        assert mock_kaldi_recognizer.AcceptWaveform.call_count == 3

        # Ensure Result was called once after AcceptWaveform returned True
        mock_kaldi_recognizer.Result.assert_called_once()

        # Verify that PyAudio's methods were called correctly
        mock_pyaudio.open.assert_called_once_with(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=4096
        )
        mock_pyaudio.open.return_value.read.assert_called()
import random

import pytest
from unittest.mock import patch, Mock
from aihao.greeting import Greeting

@pytest.mark.greeting
class TestGreeting:
    @pytest.fixture(scope='class')
    def greeting_obj(self):
        greeting = Greeting()
        return greeting

    @patch('builtins.open', create=True)
    def test_random_greetings(self, mock_open, greeting_obj):
        # Mocking the open function
        greeting_prompts = "greetings.txt"
        mock_file = mock_open.return_value
        mock_file.read.return_value = ("Hello\n"
                                       "Hi\n"
                                       "Hey\n")

        # Mocking random.choice to always return "Hi"
        with patch('random.choice', lambda x: "Hi"):
            greeting_obj.random_greetings(greeting_prompts)

        # Assert that open was called with the correct file path
        mock_open.assert_called_once_with(greeting_prompts)

        # Assert that read was called on the file object
        mock_file.read.assert_called_once()

        # Assert that the greeting_response is set to "Hi"
        assert greeting_obj.greeting_response == "Hi"

    def test_greeting_with_response(self, greeting_obj):
        greeting_obj.activate = True
        assert greeting_obj.greeting() == 'Hello, how can i help you?'

    def test_greeting_no_response(self, greeting_obj):
        assert greeting_obj.greeting() == ''


    def test_wake_word_detected(self, greeting_obj):
        assert greeting_obj.wake_word('Hi David, how are you?') is True

    def test_wake_word_not_detected(self, greeting_obj):
        assert greeting_obj.wake_word('Hi, how are you?') is False


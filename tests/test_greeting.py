import pytest
from unittest.mock import patch, Mock, mock_open
from aihao.greeting import Greeting

@pytest.mark.greeting
class TestGreeting:
    @pytest.fixture(scope='function')
    def greeting_obj(self):
        greeting = Greeting()
        return greeting

    def test_initialization(self, greeting_obj):
        # Test if the object is initialized correctly
        assert greeting_obj.greeting_inputs == ['hi', 'hey', 'hola', 'bonjour', 'hello']
        assert greeting_obj.greeting_response == 'Hello, how can i help you?'
        assert greeting_obj.goodbye_response == "Goodbye! have a nice day!"
        assert not greeting_obj.activate
        assert greeting_obj.greeting_list == []

    def test_load_greetings_file_exists(self, greeting_obj):
        # Mocking the file reading
        mock_greetings = "hi\nhey\nhola\nbonjour\nhello"

        with patch("builtins.open", mock_open(read_data=mock_greetings)):
            greeting_obj.load_greetings()
            assert greeting_obj.greeting_list == ['hi', 'hey', 'hola', 'bonjour', 'hello']

    def test_load_greetings_file_not_found(self, greeting_obj):
        # Testing the case when the file doesn't exist
        with patch("os.path.exists", return_value=False):
            with patch("builtins.print") as mock_print:
                greeting_obj.load_greetings()
                mock_print.assert_called_with(f"File not found: {greeting_obj.greeting_prompts}")

    def test_random_greetings(self, greeting_obj):
        # Test when the greeting list is empty
        greeting_obj.random_greetings()  # Call the method
        assert greeting_obj.greeting_response == "Hello, how can I help you?"

        # Test when the greeting list is not empty
        greeting_obj.greeting_list = ['hi', 'hey', 'hola', 'bonjour', 'hello']

        with patch("random.choice") as mock_choice:
            mock_choice.return_value = 'hey'  # Mocking random.choice to return 'hey'

            greeting_obj.random_greetings()  # Call the method
            assert greeting_obj.greeting_response == 'hey'  # Check that the greeting response is set correctly

    def test_greeting_default_response(self, greeting_obj):
        assert greeting_obj.greeting() == 'Hello, how can i help you?'


    def test_wake_word_detected(self, greeting_obj):
        assert greeting_obj.wake_word('Hi David, how are you?') is True

    def test_wake_word_not_detected(self, greeting_obj):
        assert greeting_obj.wake_word('Hi, how are you?') is False


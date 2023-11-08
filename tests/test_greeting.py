import pytest
from aihao.greeting import Greeting

@pytest.mark.greeting
class TestGreeting:
    @pytest.fixture(scope='class')
    def greeting_obj(self):
        greeting = Greeting()
        return greeting

    def test_audio_engine(self, greeting_obj):
        pass


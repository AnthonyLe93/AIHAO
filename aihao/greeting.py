import random

class Greeting:
    def __init__(self):
        self.greeting_inputs = ['hi', 'hey', 'hola', 'bonjour', 'hello']
        self.greeting_response = ['hi', 'hey', 'hola', 'greetings', 'bonjour', 'hello']

    def greeting(self, text):
        for word in text.split():
            if word.lower() in self.greeting_inputs:
                return random.choice(self.greeting_response)
        return ''

    def wake_word(self, text):
        WAKE_WORD = ['AKARI', 'HEY AKARI', 'HI AKARI', 'HELLO AKARI']

        text = text.lower()

        for phrase in WAKE_WORD:
            if phrase in text:
                return True
        return False


def main():
    greeting = Greeting()
    greeting.greeting('hi')
    greeting.wake_word('akari')


if __name__ == "__main__":
    main()
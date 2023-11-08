import random


class Greeting:
    def __init__(self):
        self.greeting_inputs = ['hi', 'hey', 'hola', 'bonjour', 'hello']
        self.greeting_response = None
        self.activate = False

    def random_greetings(self, greeting_prompts: str):
        lines = open(greeting_prompts).read().splitlines()
        myline = random.choice(lines)
        self.greeting_response = myline

    def greeting(self):
        if self.activate:
            return self.greeting_response
        return ''

    def wake_word(self, text):
        WAKE_WORD = ['david', 'David', 'DAVID']

        for word in text.split():
            if word.lower() in [phrase for phrase in WAKE_WORD]:
                self.activate = True
                return True
        return False


def main():
    greeting = Greeting()
    greeting.wake_word('david')
    greeting.random_greetings()
    print(greeting.greeting_response)


if __name__ == "__main__":
    main()
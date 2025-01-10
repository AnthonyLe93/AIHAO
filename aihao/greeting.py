import random
from aihao.util_funtions.text_processor import replace_symbols_with_empty_string
import os
class Greeting:
    def __init__(self):
        self.greeting_inputs = ['hi', 'hey', 'hola', 'bonjour', 'hello']
        self.greeting_response = 'Hello, how can i help you?'
        self.goodbye_response = "Goodbye! have a nice day!"
        self.activate = False
        self.greeting_list = []  # This will store all greetings
        self.greeting_prompts = os.path.join(os.path.dirname(__file__), '..', 'data', 'greeting_prompts.txt')

    def load_greetings(self):
        """Load greetings from the file once."""
        if os.path.exists(self.greeting_prompts):
            with open(self.greeting_prompts, 'r') as file:
                self.greeting_list = file.read().splitlines()
        else:
            print(f"File not found: {self.greeting_prompts}")

    def random_greetings(self):
        """Select a random greeting from the pre-loaded list."""
        if self.greeting_list:
            self.greeting_response = random.choice(self.greeting_list)
        else:
            self.greeting_response = "Hello, how can I help you?"

    def greeting(self):
        return self.greeting_response

    def goodbye(self):
        return self.goodbye_response

    def wake_word(self, text):
        WAKE_WORD = ['david']  # Normalize all wake words to lowercase

        for word in text.split():
            # Normalize word by removing symbols and converting to lowercase
            normalized_word = replace_symbols_with_empty_string(word).lower()
            if normalized_word in WAKE_WORD:
                self.activate = True
                return True
        return False


def main():
    greeting = Greeting()
    greeting.wake_word('david')
    print(greeting.greeting_response)


if __name__ == "__main__":
    main()
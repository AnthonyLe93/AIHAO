import pyttsx3

def audio_engine():
    engine = pyttsx3.init()
    return engine

def assistantResponse(text):
    print(text)
    # init audio engine
    engine = audio_engine()
    engine.say(text)
    engine.runAndWait()


def main():
    assistantResponse("Hello Anthony")


if __name__ == "__main__":
    main()



import pyttsx3

def audio_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()
    return engine

def assistantResponse(text):
    print(text)
    # init audio engine
    engine = audio_engine()
    engine.say(text)
    engine.runAndWait()


def main():
    # assistantResponse("Hello Anthony")
    audio_engine()

if __name__ == "__main__":
    main()



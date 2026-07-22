!pip install deep-translator gTTS

from deep_translator import GoogleTranslator
from gtts import gTTS
from IPython.display import Audio, display

while True:

    text = input("Enter text (type exit to stop): ").strip()

    if text.lower() == "exit":
        print("Exiting Translator. Goodbye!")
        break

    if text == "":
        print("⚠️ Please enter some text to translate.\n")
        continue

    source = input("Source language code (e.g. en, ur, fr, ar, es, de, hi, zh-CN): ").strip().lower()
    target = input("Target language code (e.g. en, ur, fr, ar, es, de, hi, zh-CN): ").strip().lower()

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)

        print("\nTranslated Text:")
        print(translated)

        # Bonus: Text-to-Speech output
        speak = input("\nDo you want to hear the translation? (y/n): ").strip().lower()
        if speak == "y":
            try:
                tts = gTTS(text=translated, lang=target)
                tts.save("translated_audio.mp3")
                display(Audio("translated_audio.mp3", autoplay=True))
            except Exception as e:
                print(f"⚠️ Could not generate audio for this language: {e}")

        print("\n" + "-"*40 + "\n")

    except Exception as e:
        print(f"⚠️ Translation failed. Please check your language codes.\nError: {e}\n")

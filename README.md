# AI Language Translation Tool

A simple Python-based language translation application that uses an AI translation API to translate text between languages, with optional text-to-speech playback.

## Objective
Create a language translation application using an AI translation API, allowing users to input text, choose source/target languages, and view the translated output.

## Features
- Accepts free-form text input from the user
- Lets the user choose any source and target language (100+ languages supported, not limited to a fixed list)
- Displays the translated text
- Handles invalid language codes, empty input, and API errors gracefully
- Bonus: Converts the translated text to speech (audio playback) using gTTS

## 🛠️ Tech Stack
- Python
- [`deep-translator`](https://pypi.org/project/deep-translator/) — translation via Google Translate
- [`gTTS`](https://pypi.org/project/gTTS/) — Google Text-to-Speech

## ⚙️ Installation
```bash
pip install deep-translator gTTS
```

## How to Run
1. Open `translator.ipynb` in Jupyter Notebook or Google Colab.
2. Run all cells.
3. Follow the prompts:
   - Enter the text you want to translate
   - Enter the source language code (e.g. `en`, `ur`, `fr`, `ar`, `es`)
   - Enter the target language code
   - Optionally, choose to hear the translation read aloud

## Example
```
Enter text (type exit to stop): Hello, how are you?
Source language code (e.g. en, ur, fr, ar, es): en
Target language code (e.g. en, ur, fr, ar, es): ur

Translated Text:
ہیلو، آپ کیسے ہیں؟

Do you want to hear the translation? (y/n): y
```

## Requirements
- Python 3.8+
- Google Colab
- Internet connection (required for Google Translate / Text-to-Speech API calls)

## Future Improvements
- Add a web-based UI using Streamlit or Flask
- Add speech-to-text input (translate what you say, not just what you type)
- Add a dynamic dropdown of all supported languages instead of typing codes

## Author
Tayyaba Mangi

Electronics Engineering Student

Mehran University of Engineering and Technology (MUET)

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

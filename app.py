import gradio as gr
from deep_translator import GoogleTranslator

# Supported languages
languages = {
    'Telugu': 'te',
    'Tamil': 'ta',
    'Hindi': 'hi',
    'Marathi': 'mr'
}

# Function to translate input text into multiple languages
def translate_text(text):
    results = {}
    for lang_name, lang_code in languages.items():
        try:
            translated = GoogleTranslator(source='en', target=lang_code).translate(text)
            results[lang_name] = translated
        except Exception as e:
            results[lang_name] = f"Error: {str(e)}"
    return [results[lang] for lang in languages.keys()]

# Gradio interface
demo = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(label="Enter text to translate", placeholder="Type something..."),
    outputs=[gr.Textbox(label=f"{lang}") for lang in languages.keys()],
    title=" Multi-Language Translator",
    description="Translate English text into Telugu, Hindi, Tamil, and Marathi using Google Translator (via deep-translator)."
)

if __name__ == "__main__":
    demo.launch()
from googletrans import Translator

translator = Translator()

def translate_to_bengali(text):
    """
    ইংরেজি টেক্সট বাংলা ভাষায় অনুবাদ করা।
    """
    try:
        translation = translator.translate(text, dest='bn')
        return translation.text
    except Exception as e:
        print(f"Translation Error: {e}")
        return text  # সমস্যা হলে ইংরেজিতেই রেখে দেবে
from transformers import pipeline

def translate_and_summarize(text):
    
    translator_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
    translated_text = translator_to_en(text, max_length=512)[0]['translation_text']

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(translated_text, max_length=400, min_length=25, do_sample=False)

    translator_to_ru = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")
    translated_summary = translator_to_ru(summary[0]['summary_text'], max_length=512)[0]['translation_text']
    
    return translated_summary
from transformers import pipeline
import gradio as gr

# 1. Model translate (multi-bahasa → Inggris)
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

# 2. Model sentiment (khusus bahasa Inggris)
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Fungsi analisis dengan translasi
def analyze_translated_sentiment(text):
    # Translate dulu ke Inggris
    translation = translator(text, max_length=512)[0]["translation_text"]

    # Analisis sentimen pakai hasil translate
    result = sentiment_model(translation)[0]
    label = result['label']
    score = round(result['score'], 3)

    # Interpretasi label
    interpretation = {
        "NEGATIVE": "😡 Negatif",
        "POSITIVE": "🥰 Positif"
    }

    return f"Teks asli: {text}\n" + \
           f"Terjemahan: {translation}\n" + \
           f"Hasil: {label} ({score})\nInterpretasi: {interpretation.get(label, 'Tidak diketahui')}"

# UI Gradio
interface = gr.Interface(
    fn=analyze_translated_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Tulis teks Bahasa Indonesia atau lainnya..."),
    outputs="text",
    title="🌐 Sentiment Analysis (Translated)",
    description="Menganalisis sentimen teks multibahasa dengan menerjemahkannya terlebih dahulu ke Bahasa Inggris."
)

if __name__ == "__main__":
    interface.launch()

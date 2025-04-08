# 🌍 Sentiment Analyzer Translated

Multilingual Sentiment Analyzer by first translating any language to English before running the sentiment prediction.

> 🇮🇩 Bisa Bahasa Indonesia, 🇯🇵 日本語, 🇸🇦 العربية, 🇫🇷 Français, dan lainnya~ 💖  
> Powered by Hugging Face Transformers & Gradio ✨

---

## 🚀 Live Demo
👉 [Coba langsung di Hugging Face Spaces](https://huggingface.co/spaces/Ryurex/sentiment-translated)

---

## 🎯 Fitur

- ✨ Terima input dalam berbagai bahasa (multilingual)
- 🔄 Terjemahkan otomatis ke Bahasa Inggris
- 🔍 Prediksi sentimen: Positive, Neutral, atau Negative
- 🖼️ Antarmuka interaktif dengan Gradio

---

## 🧠 Model yang Digunakan

| Fungsi           | Model Hugging Face |
|------------------|---------------------|
| Translasi        | `Helsinki-NLP/opus-mt-mul-en` |
| Sentimen         | `cardiffnlp/twitter-roberta-base-sentiment` |

---

## 💻 Cara Menjalankan Lokal

### 1. Clone repositori ini
```bash
git clone https://github.com/Ryurex/Sentiment-Analyzer-Translated.git
cd sentiment-translated

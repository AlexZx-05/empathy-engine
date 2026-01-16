# 🧠 The Empathy Engine
### Emotion-Aware Text-to-Speech with Expressive Voice Output

---

## 📌 Overview

**The Empathy Engine** is an AI-powered Text-to-Speech (TTS) system that generates **emotionally expressive speech** from plain text.  
Unlike traditional monotonic TTS systems, this application dynamically modulates vocal characteristics based on the **detected emotional tone** of the input text.

The system bridges the gap between **text sentiment** and **human-like audio output**, enabling more natural and empathetic AI interactions.

---


## 🎥 Demo Video

A short demo showcasing the end-to-end flow of the Empathy Engine, including emotion detection, voice modulation, and audio playback.

▶️ Watch the demo here:  
https://drive.google.com/file/d/1rcthKYBE7ZaT2QkE9inbhHJymnsdNZGK/view

> Note: The demo video is hosted on Google Drive due to GitHub file size limitations.

---
## 🎯 Key Features

- Automatic emotion detection from text  
- Emotion-to-voice mapping (rate & volume modulation)  
- Emotion intensity scaling  
- Audio generation in `.wav` format  
- Web-based frontend with:
  - Emotion emoji (😄 😐 😔)
  - Emotion badge
  - In-browser audio playback  
- Clean, modular backend architecture  

---

## 🏗️ System Architecture
```
┌────────────┐
│  Frontend  │  (HTML via FastAPI)
│  (Browser) │
└─────┬──────┘
      │  POST /speak
      ▼
┌────────────────────┐
│   FastAPI Server   │
│     (api.py)       │
└─────┬──────────────┘
      │
      │ calls
      ▼
┌────────────────────┐
│ Emotion Detection  │
│   (emotion.py)     │
│  VADER Sentiment   │
└─────┬──────────────┘
      │
      ▼
┌────────────────────┐
│ Voice Modulation   │
│     (tts.py)       │
│ pyttsx3 TTS Engine │
└─────┬──────────────┘
      │
      ▼
┌────────────────────┐
│   Audio Output     │
│  output/speech.wav │
└────────────────────┘
```

---

## 📁 Project Structure

```
empathy-engine/
│
├── api.py # FastAPI app and frontend UI
├── app.py # CLI-based execution
├── emotion.py # Sentiment and emotion detection
├── tts.py # Text-to-Speech logic
├── requirements.txt
├── README.md
└── output/
└── speech.wav

```


---

## 🧠 Emotion Detection

Emotion is detected using **VADER Sentiment Analysis**.

The compound sentiment score is mapped to emotions using fixed thresholds:

| Sentiment Score | Emotion |
|-----------------|--------|
| ≥ 0.6           | Happy |
| ≤ -0.4          | Frustrated |
| Otherwise       | Neutral |

This avoids classifying neutral system messages as strongly positive.

---

## 🔊 Voice Modulation Logic

Based on detected emotion, speech parameters are adjusted:

| Emotion | Speech Rate | Volume |
|-------|-------------|--------|
| Happy | Increased   | Higher |
| Neutral | Default   | Default |
| Frustrated | Reduced | Lower |

The magnitude of the sentiment score slightly influences the degree of modulation.

---

## ▶️ Running the Application
### Install dependencies
bash
python -m pip install -r requirements.txt

### Run the web application

python -m uvicorn api:app --reload

### Open in browser:
http://127.0.0.1:8000
---

## Sample Test Inputs

### Positive
I am happy with the progress so far and everything seems to be going well.
### Neutral
The meeting is scheduled for tomorrow and the details have been shared.
### Negative
There have been some delays and the overall experience has been disappointing.





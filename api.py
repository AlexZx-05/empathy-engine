from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from emotion import detect_emotion
from tts import generate_speech
import base64

app = FastAPI()


def emotion_emoji(emotion):
    if emotion == "happy":
        return "😄"
    elif emotion == "frustrated":
        return "😔"
    else:
        return "😐"


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>The Empathy Engine</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                margin: 0;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e3a8a);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: #ffffff;
                width: 440px;
                padding: 28px;
                border-radius: 14px;
                box-shadow: 0 30px 50px rgba(0,0,0,0.35);
            }
            h1 {
                margin: 0;
                text-align: center;
                font-size: 22px;
                color: #0f172a;
            }
            p.subtitle {
                text-align: center;
                color: #475569;
                font-size: 14px;
                margin: 8px 0 18px;
            }
            textarea {
                width: 100%;
                height: 110px;
                padding: 12px;
                border-radius: 10px;
                border: 1px solid #cbd5f5;
                font-size: 14px;
                resize: none;
                outline: none;
            }
            textarea:focus {
                border-color: #2563eb;
            }
            button {
                margin-top: 16px;
                width: 100%;
                padding: 12px;
                border: none;
                border-radius: 10px;
                background: #2563eb;
                color: white;
                font-size: 15px;
                font-weight: 500;
                cursor: pointer;
            }
            button:hover {
                background: #1d4ed8;
            }
            .footer {
                margin-top: 14px;
                text-align: center;
                font-size: 12px;
                color: #94a3b8;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>The Empathy Engine</h1>
            <p class="subtitle">Emotion-aware voice synthesis for human-like AI interaction</p>
            <form action="/speak" method="post">
                <textarea name="text" placeholder="Type your message here..." required></textarea>
                <button type="submit">Generate Empathetic Speech</button>
            </form>
            <div class="footer">Enterprise demo • Built with FastAPI</div>
        </div>
    </body>
    </html>
    """


@app.post("/speak", response_class=HTMLResponse)
def speak(text: str = Form(...)):
    emotion, intensity = detect_emotion(text)
    audio_path = generate_speech(text, emotion, intensity)

    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    emoji = emotion_emoji(emotion)

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Empathy Engine Result</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                margin: 0;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e3a8a);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .container {{
                background: white;
                width: 440px;
                padding: 28px;
                border-radius: 14px;
                box-shadow: 0 30px 50px rgba(0,0,0,0.35);
                text-align: center;
            }}
            h1 {{
                margin-top: 0;
                font-size: 22px;
                color: #0f172a;
            }}
            .emotion {{
                font-size: 56px;
                margin: 10px 0;
            }}
            .label {{
                font-size: 14px;
                color: #475569;
                margin-bottom: 14px;
            }}
            audio {{
                width: 100%;
                margin-top: 10px;
            }}
            a {{
                display: inline-block;
                margin-top: 18px;
                font-size: 14px;
                text-decoration: none;
                color: #2563eb;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1> The Empathy Engine</h1>
            <div class="emotion">{emoji}</div>
            <div class="label">
                Detected Emotion: <b>{emotion.capitalize()}</b>
            </div>

            <audio controls autoplay>
                <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
            </audio>

            <a href="/">← Analyze another message</a>
        </div>
    </body>
    </html>
    """

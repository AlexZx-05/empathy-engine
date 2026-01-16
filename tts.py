import pyttsx3
import os


def generate_speech(text, emotion, intensity):
    engine = pyttsx3.init()

    # Base values
    rate = 150
    volume = 0.8

    # Emotion → Voice mapping
    if emotion == "happy":
        rate = 180 + int(intensity * 20)
        volume = 1.0

    elif emotion == "frustrated":
        rate = 120 - int(abs(intensity) * 20)
        volume = 0.6

    else:  # neutral
        rate = 150
        volume = 0.8

    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    engine.setProperty("voice", engine.getProperty("voices")[0].id)

    os.makedirs("output", exist_ok=True)
    output_path = "output/speech.wav"

    engine.save_to_file(text, output_path)
    engine.runAndWait()

    return output_path

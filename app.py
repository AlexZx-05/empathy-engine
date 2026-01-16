# FastAPI or CLI entry
from emotion import detect_emotion
from tts import generate_speech

def main():
    print("=== The Empathy Engine ===")
    text = input("Enter text: ")

    emotion, intensity = detect_emotion(text)

    print(f"Detected Emotion: {emotion}")
    print(f"Emotion Intensity Score: {intensity}")

    output_file = generate_speech(text, emotion, intensity)

    print(f"Audio generated successfully: {output_file}")

if __name__ == "__main__":
    main()

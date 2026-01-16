from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def detect_emotion(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.6:
        return "happy", compound

    elif compound <= -0.4:
        return "frustrated", compound

    else:
        return "neutral", compound

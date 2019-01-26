from django.shortcuts import render
from django.http import HttpResponse
from . import emotion, take_photo
import statistics

# Create your views here.

# Score of each emotion
emotion_scores = {
    "anger": -7,
    "contempt": -5,
    "disgust": -10,
    "fear": -4,
    "happiness": 10,
    "neutral": 0,
    "sadness": -2,
    "surprise": 6
}

def analysis(request):
    filenames = []

    scores = []

    # Takes 5 photos and get emotion, one every 10 sec
    for i in range(5):
        # Take photo
        filename = take_photo.takePictureAndSave()
        filenames.append(filename)

        # Analyse the emotion of the face
        emotions = emotion.analysisPhoto("" + filename)

        score = 0
        # Add up the score of each emotion
        for key, value in emotion_scores.items():
            score += emotions[key] * value

        print(score)
        # Store the score of this shot into the scores list
        scores.append(score)

    # Calculate the median of all the shots
    median = statistics.median(scores)

    print(median)

    # Response soth the emotion score of the person
    return HttpResponse(median)

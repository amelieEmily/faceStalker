from django.shortcuts import render
from django.http import HttpResponse
from . import emotion, take_photo
import statistics
import os
from google.cloud import pubsub_v1

def callback(request):
    request.ack()
    filenames = []

    scores = []

    # Takes 5 photos and get emotion, one every 10 sec
    for i in range(5):
        # Take photo
        filename = take_photo.takePictureAndSave()
        filenames.append(filename)

        # Analyse the emotion of the face
        emotions = emotion.analysisPhoto("" + filename)

        if not emotions:
            scores.append(0)
            continue

        score = 0
        # Add up the score of each emotion
        for key, value in emotion_scores.items():
            score += emotions[key] * value

        print(score)
        # Store the score of this shot into the scores list
        scores.append(score)

    # Calculate the median of all the shots
    median = statistics.mean(scores)

    print("Median:" + str(median))

    data = u'{}'.format(median)
    # Data must be a bytestringf
    data = data.encode('utf-8')
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data)

    print("Message sent: " + str(median))

    # Response soth the emotion score of the person
    return HttpResponse(median)


subscriber = pubsub_v1.SubscriberClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id='huddle72',
    topic='vote',  # Set this to something appropriate.
)
subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id='huddle72',
    sub='machine1',  # Set this to something appropriate.
)

return_topic = 'projects/{project_id}/topics/{topic}'.format(
    project_id='huddle72',
    topic='faceEmotion',  # Set this to something appropriate.
)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('huddle72', 'faceEmotion')



future = subscriber.subscribe(subscription_name, callback)

# Create your views here.

# Score of each emotion
emotion_scores = {
    "anger": -7,
    "contempt": -5,
    "disgust": -10,
    "fear": -4,
    "happiness": 9,
    "neutral": -1,
    "sadness": -6,
    "surprise": 6
}

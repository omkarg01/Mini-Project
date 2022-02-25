import cv2
import os
from cv2 import Algorithm
from findDist import find_X_dist, find_Y_dist

# Using haarcascade Algorithm
cascPath = os.path.dirname(cv2.__file__)  + "/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # dimension for red lines
    height = frames.shape[0]
    width = frames.shape[1]

    cv2.line(frames, (int(width/2), 0), (int(width/2), height), (0, 0, 255), 2)
    cv2.line(frames, (0, int(height/2)),
             (width, int(height/2)), (0, 0, 255), 2)

    radius = 8
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
        circleX = int(x + w/2)
        circleY = int(y + h/2)

        cv2.circle(frames, (circleX, circleY), radius, (255, 0, 0), -1)

        addOnX = -(radius + 2) if circleX > width/2 else radius + 2
        addOnY = -(radius + 2) if circleY > height/2 else radius + 2

        # X distance
        find_X_dist(frames, width, circleX, circleY, addOnX)

        # Y distance
        find_Y_dist(frames, height, width, circleX, circleY, addOnY)

    # Display the resulting frame
    cv2.imshow('Video', frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # loop ends here
video_capture.release()
cv2.destroyAllWindows()

import cv2

def find_X_dist(frames, width, circleX, circleY, addOnX):
    cv2.arrowedLine(frames, (int(width/2), circleY),
                    (circleX + addOnX, circleY), (0, 0, 255), 2)

    cv2.arrowedLine(frames, (circleX + addOnX, circleY),
                    (int(width/2), circleY), (0, 0, 255), 2)

    cv2.putText(frames, '' + str(abs(int(circleX - width/2))), 
                (int(width/2 + (circleX - width/2)/2), circleY - 4), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 1, cv2.LINE_AA)


def find_Y_dist(frames, height, width, circleX, circleY, addOnY):
    cv2.arrowedLine(frames, (circleX, int(height/2)),
                    (circleX, circleY + addOnY), (0, 0, 255), 2)

    cv2.arrowedLine(frames, (circleX, circleY + addOnY),
                    (circleX, int(height/2)), (0, 0, 255), 2)

    cv2.putText(frames, '' + str(abs(int(circleY - height/2))), 
               (circleX - 30, circleY + int((width/2 - circleY)/2)), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 1, cv2.LINE_AA)

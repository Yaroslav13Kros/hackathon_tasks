import cv2
import numpy as np

print(cv2.__version__)

train_video = cv2.VideoCapture("train.mp4")
frame_index = 1

while True:
    ret, frame = train_video.read()
    # If found, add object points, image points (after refining them)
    if (ret == True) & (frame_index == 301):
        str_id_image = str(frame_index)
        print('Images ' + str_id_image + ' saved for right and left cameras')
        cv2.imwrite('freme_' + str_id_image + '.png',frame)  # Save the image in the file

    # End the Programme
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Push the space bar and maintan to exit this Programm
        break

    frame_index = frame_index + 1

train_video.release()
cv2.destroyAllWindows()

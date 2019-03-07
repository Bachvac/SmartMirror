from imutils.video import VideoStream
from imutils.video import FPS
import datetime
import imutils
import time
import cv2
import numpy as np
import image
from threading import Lock, Thread


class MotionDetection(Thread):

    def has_movement(self):
        return self.has_movement

    def set_has_movement(self, value):
        old_value = self.has_movement
        self.has_movement = value
        if old_value != value:
            for update in self.movement_callbacks:
                update(self.has_movement)

    def __init__(self, show_display=True, movement_callbacks=None):
        Thread.__init__(self) #konstruktor od dretve

        if movement_callbacks is None:
            movement_callbacks = []

        self.has_movement = 0
        self.show_display = show_display
        self.movement_callbacks = movements_callbacks




    def detect_motion():

        print("[INFO] camera sensor warming up...")

        vs = VideoStream(src=1).start()
        # vs = VideoStream(usePiCamera=True).start() # Raspberry Pi
        time.sleep(2.0)
        i = 0
        detected = 0
        crop_rectangle = (50, 50, 100, 100)

        while True:

            prev = vs.read()
            prev = imutils.resize(prev, width=600)
            prev = prev[50:100, 50:100]
            prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

            frame = vs.read()
            frame = imutils.resize(frame, width=600)

            current = frame[50:100, 50:100]
            #cv2.imshow("cropped", current)
            #cv2.waitKey(0)

            gray = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)

            bX = 50
            bY = 50
            bW = 50
            bH = 50

            cv2.rectangle(frame, (bX, bY), (bX + bW, bY + bH),
                (255, 100, 255), 1)

            err = np.sum((prevgray.astype("float") - gray.astype("float")) ** 2)
            err /= float(prevgray.shape[0] * gray.shape[1])

            if err > 300:
                detected += 1
                self.set_has_movement(detected)
            text = "movements: {}".format(detected)
            cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 255), 1)

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        cv2.destroyAllWindows()
        vs.stop()


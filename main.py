from handdetector import HandDetector
import cv2
import time
import numpy as np

class DrawDetector(HandDetector):
    
    def isDrawPose(self, img):
        lmlist = self.findPosition(img)
        if lmlist:
            len1 = self._len(lmlist[8], lmlist[5])
            len2 = self._len(lmlist[12],lmlist[9])
            len3 = self._len(lmlist[16],lmlist[13])
            len4 = self._len(lmlist[20],lmlist[17])
            if len1 > len2 +len3 +len4:
                return True
            else:
                return False
        else:
            return False

    def _len(self, point1, point2):
        vec = np.array([point2[1]-point1[1],point2[2]-point1[2]])
        return np.linalg.norm(vec)

def main():
    img_counter = 0
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = DrawDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if detector.isDrawPose(img):
            print(True)
        if len(lmlist) != 0:
            print(lmlist[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        k = cv2.waitKey(1)
        
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1


if __name__ == "__main__":
    main()
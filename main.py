from draw_detector import DrawDetector
import cv2
import time
import numpy as np

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
            pos = detector.getPenPosition(img)
            if type(pos) == np.ndarray:            
                cv2.circle(img, (pos[0], pos[1]), 3, (255, 0, 0), cv2.FILLED)
                detector.add_to_board(pos)
        detector.paint_board(img)
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
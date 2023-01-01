from hand_detector import HandDetector
import numpy as np
import cv2

class DrawDetector(HandDetector):
    
    points = []
    
    def isDrawPose(self, img):
        lmlist = self.findPosition(img)
        if lmlist:
            len1 = self._len(lmlist[8], lmlist[5])
            len2 = self._len(lmlist[12],lmlist[9])
            len3 = self._len(lmlist[16],lmlist[13])
            len4 = self._len(lmlist[20],lmlist[17])
            if np.square(len1) > np.square(len2) + np.square(len3) + np.square(len4):
                return True
            else:
                return False
        else:
            return False

    def getPenPosition(self, img):
        lmlist = self.findPosition(img)
        pen = lmlist[8]
        if pen:
            return np.array([pen[1], pen[2]])
        else:
            return False
        
    def add_to_board(self, pos):
        self.points.append(pos)
        
    def paint_board(self, img):
        last_point = None
        is_first_loop = True
        for point in self.points:
            cv2.circle(img, (point[0], point[1]), 3, (0, 255, 0), cv2.FILLED)
            if not is_first_loop:
                cv2.line(img, (last_point[0], last_point[1]), (point[0], point[1]), (0,128,0),3)
            is_first_loop = False
            last_point = point
        return img
        
    def _len(self, point1, point2):
        vec = np.array([point2[1]-point1[1],point2[2]-point1[2]])
        return np.linalg.norm(vec)
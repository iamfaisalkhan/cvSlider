# -*- coding: utf-8 -*-
# @Author: Faisal Khan
# @Date:   2017-02-16 10:54:41
# @Last Modified by:   Faisal Khan
# @Last Modified time: 2017-02-16 11:48:40

import cv2

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ImageUI(QWidget):
    """ A widget to display OpenCV image along with operations applied to it. 
    """
    def __init__(self, cvImage):
        super(ImageUI, self).__init__()
        self.cvImage = cvImage

        self.initUI()

    def initUI(self):
        self.scene = QGraphicsScene(self)

        height, width, byteValue = self.cvImage.shape
        byteValue = byteValue * width
        cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        self.mQImage = QImage(self.cvImage, width, height, byteValue, QImage.Format_RGB888)
        self.mPixelMap = QPixmap.fromImage(self.mQImage)

        self.scene.addPixmap(self.mPixelMap)
        self.view = QGraphicsView(self.scene, self)
# app.y

import cv2

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from imageUI import ImageUI
from controllerUI import ControllerUI

from pipeline import Pipeline
from pipelineThread import PipelineThread

class MainWindow(QMainWindow):
    
    def __init__(self, pipeline = Pipeline):
        super(MainWindow, self).__init__()

        self.pipeline = pipeline

        self._initUI()

    def _initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(100, 100, 1280, 1024)
        self.setWindowTitle('OpenCV-Pipeline')

        self.cvImage = self.pipeline.getSource()

        self.imageScene = ImageUI(self.cvImage)

        self.setCentralWidget(self.imageScene)

        # Right Dock Widget
        dock = QDockWidget('Controls', self)
        dock.setAllowedAreas(Qt.RightDockWidgetArea)
        self.controller = ControllerUI(self.pipeline)
        dock.setWidget(self.controller)

        self.connect(self.controller, SIGNAL("valueChanged()"), self._updateImage)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def _updateImage(self):
        self.pipelineThread = PipelineThread(self.pipeline)
        self.connect(self.pipeline, SIGNAL("imageReady(QImage)"), self._imageReady)
        self.pipelineThread.start()

    def _imageReady(self, qImage):
        self.imageScene.updateImage(qImage)


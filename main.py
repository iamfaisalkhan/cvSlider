import sys
import cv2

import combining_thresholds
from PyQt4 import QtGui
from app import MainWindow
from pipeline import Pipeline

def main():
    img = cv2.imread(sys.argv[1])
    
    pipeline = Pipeline()
    pipeline.setSource(img)
    # pipeline.setVideoSource('challenge_video.mp4')

    pipeline.addStep(combining_thresholds.combined_threshold2)
    # pipeline.addStep(combining_thresholds.dir_threshold)

    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow(pipeline)
    myapp.showMaximized()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
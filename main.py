import sys
import cv2

import combining_thresholds
from PyQt4 import QtGui
from app import MainWindow
from pipeline import Pipeline

def main():
    img = cv2.imread('signs_vehicles_xygrid.png')
    
    pipeline = Pipeline()
    pipeline.setSource(img)

    pipeline.addFunction(combining_thresholds.mag_thresh)
    pipeline.addFunction(combining_thresholds.dir_threshold)

    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow(pipeline)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
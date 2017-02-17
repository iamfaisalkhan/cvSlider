import sys
from PyQt4 import QtGui
from app import MainWindow

def main():
    img = cv2.imread('signs_vehicles_xygrid.png')
    pipeline = Pipeline()
    pipeline.setSource(img)

    pipeline.addFunction(combining_thresholds.mag_thresh)
    pipeline.addFunction(combining_thresholds.dir_threshold)

    for stage in pipeline.stages:
        print ("\nFunction\n\t %s"%stage['name'])
        
        if len(stage['parameters']) > 0:
            print("Args\n\t")

        for param in stage['parameters']:
            print("\t %s:%s"%(param.name, param.value))

        print()

    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
import sys
from PyQt4 import QtGui
from app import MainWindow

def main():
  app = QtGui.QApplication(sys.argv)

  myapp = MainWindow()

  sys.exit(app.exec_())

if __name__ == '__main__':
    main()
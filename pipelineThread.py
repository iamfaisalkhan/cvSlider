
from PyQt4.QtCore import *

class PipelineThread(QThread):
    def __init__(self, pipeline):
        QThread.__init__(self)
        self.pipeline = pipeline

    def __del__(self):
        self.wait()

    def run(self):
        self.pipeline.execute()
        
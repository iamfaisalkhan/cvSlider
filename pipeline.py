import inspect
import cv2
import importlib


from PyQt4.QtCore import *
from PyQt4.QtGui import *

class FuncParam:
    def __init__(self, param = inspect.Parameter, funcName="", index=0):
        self.param = param
        self.name = param.name
        self.default = param.default
        self.value = self.default

        if type(self.value) == tuple:
            self.value = self.default[0]
        
        self.key = "%d_%s_%s"%(index, funcName, self.name)

    def isRange(self):
        return type(self.default) == tuple

    def isRangeFloat(self):
        if type(self.default) == tuple:
            return type(self.default[0]) == float or type(self.default[1]) == float

        return false

    def shortName(self):
        return (self.name[:15] + '..') if len(self.name) > 15 else self.name

    def __srt__():
        return self.name

class Pipeline(QObject):
    def __init__(self):

        super().__init__()

        self.stages = []
        self.paramMapping = {}
        self.source = None
        self.videoSource = None
        self.isVideo = False

    def setSource(self, image):
        """
        Specify the image source. 
        """ 
        self.source = image

    def setVideoSource(self, video):
        self.videoSource = video
        self.isVideo = True

        src = cv2.VideoCapture(self.videoSource)
        if (src.isOpened()):
            _, self.source = src.read()

    def getSource(self):
        return self.source

    def getOutput(self):
        return self.output

    def addStep(self, func, src=None, display=1):
        funcName = func.__module__ + "." + func.__name__
        sig = inspect.signature(func)

        stage = []
        for p in sig.parameters.values():
            param = FuncParam(p)
            stage.append(param)
            self.paramMapping[param.key] = param

        self.stages.append({"name" : funcName, "parameters" : stage})

    def execute(self):
        if not self.isVideo:
            src = self.source.copy()
            self._apply(src)
            return

        cap = cv2.VideoCapture(self.videoSource)

        while (cap.isOpened()):
            ret, frame = cap.read()

            self._apply(frame)
        
    def _apply(self, image):
        for stage in self.stages:
            print ("\nFunction\n\t %s"%stage['name'])
        
            if len(stage['parameters']) > 0:
                print("Args\n\t")

            args = [image]

            for param in stage['parameters'][1:]:
                args.append(param.value)
                print("\t %s:%s:%s"%(param.name, param.default, param.value))

            function_string = stage['name']
            mod_name, func_name = function_string.rsplit('.',1)
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            kwargs = {}
            image = func(*args, **kwargs)

        qImage = QImage(image, image.shape[1], image.shape[0], QImage.Format_Indexed8)
        self.emit(SIGNAL("imageReady(QImage)"), qImage)
        self.output = image







import cv2
import inspect

import combining_thresholds

class FuncParam:
    def __init__(self, param = inspect.Parameter, funcName="", index=0):
        self.param = param
        self.name = param.name
        self.default = param.default
        self.value = self.default

        if type(self.default) == tuple:
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

class Pipeline:
    def __init__(self):
        self.stages = []
        self.paramMapping = {}
        self.source = None

    def setSource(self, image):
        """
        Specify the image source. 
        """ 
        self.source = image

    def getSource(self):
        return self.source

    def addFunction(self, func, output_size=(500, 500), display=True):
        funcName = func.__name__
        sig = inspect.signature(func)

        stage = []
        for p in sig.parameters.values():
            param = FuncParam(p)
            stage.append(param)
            self.paramMapping[param.key] = param

        self.stages.append({"name" : funcName, "parameters" : stage})

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
            print("\t %s:%s:%s"%(param.name, param.default, param.value))

        print()

    print(pipeline.paramMapping)

if __name__ == "__main__":
    main()



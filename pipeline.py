import cv2
import inspect

import combining_thresholds


class FuncParam:
    def __init__(self, param = inspect.Parameter):
        self.param = param
        self.name = param.name
        self.value = param.default

    def isRange():
        return type(self.value) == tuple

    def __srt__():
        return self.name

class Pipeline:
    def __init__(self):
        self.stages = []
        self.source = None

    def setSource(self, image):
        """
        Specify the image source. 
        """ 
        self.source = image

    def getSource(self):
        return self.source

    def addFunction(self, func, output_size=(500, 500), display=True):
        name = func.__name__
        sig = inspect.signature(func)

        stage = []
        for p in sig.parameters.values():
            param = FuncParam(p)
            stage.append(param)

        self.stages.append({"name" : name, "parameters" : stage})

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



if __name__ == "__main__":
    main()



#import sys to import from outside folder
import sys
sys.path.append("../")

import os

from weeb.getter import GetterMain

class MainCompiler():
    def __init__(self, projName, reqUri):
        self.__projName = projName
        self.__reqUri = reqUri
    
    def startGetter(self):
        return GetterMain(self.__reqUri)
    def repLacer(self):
        ROOTDIR = os.path.dirname(os.path.realpath(__file__))
        #make a temp copy of the project
        #os.system("xcopy /weeb/")
        print(ROOTDIR)
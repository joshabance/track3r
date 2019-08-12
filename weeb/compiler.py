#import system commands
import os
import sys
sys.path.append("../")

import datetime

#import colorama
from colorama import init
from colorama import Fore, Style

#initialize colorama
init()

from weeb.getter import GetterMain

class MainCompiler():
    def __init__(self, reqUri, projName):
        self.__reqUri = reqUri
        self.__projName = projName
        self.__rootDir = os.path.dirname(os.path.abspath(__file__)) #get working dir
        #make dir and copy base files
        try:
            self.__makeDir()
            try:
                self.__copyFiles()
            except Exception as copyErr:
                print(Fore.RED + "\n\t\t  [!] Err!", copyErr)
        except Exception as mkdirErr:
            print(Fore.RED + "\n\t\t  [!] Err!", mkdirErr)

        #start the main getter
        try:
            self.__getter = GetterMain(self.__reqUri, self.__projName)
        except Exception as errGetter:
            print(Fore.RED + "\n\t\t  [!] Err!", errGetter)
            sys.exit(0)

        #get time
        self.__DateTime = datetime.datetime.now()

        #replace strings in the html file
        try:
            with open(self.__rootDir + "\\temp\\" + self.__projName + "\\index.html", "r") as rawFile:
                self.__indexData = rawFile.read()
            self.__rep = self.__indexData.replace("{start-time:}", self.__getStartTime()).replace("{end-time:}", self.__getEndTime()).replace("{proj-title:}", self.__projName.upper()).replace("{ip-web:}", self.__reqUri).replace("{ip-asn:}", self.__reqUri).replace("{ipweb-here:}", self.__reqUri).replace("{proj-name:}", self.__projName).replace("{proj-status:}", "DONE").replace("{ip-address:}", self.__reqUri).replace("{host-name:}", str(self.__getter.getHostName())).replace("{ip-country:}", str(self.__getter.getCountry())).replace("{ip-city:}", str(self.__getter.getCity())).replace("{ip-region:}", str(self.__getter.getRegion())).replace("{ip-postal:}", str(self.__getter.getPostal())) .replace("{ip-lat:}", str(self.__getter.getLatitude())).replace("{ip-long:}", str(self.__getter.getLongitude())).replace("{asn-name:}", str(self.__getter.getASN())).replace("{asn-domain:}", str(self.__getter.asnWebsite())).replace("{asn-route:}", str(self.__getter.asnCompany())).replace("{asn-type:}", str(self.__getter.asnName()))
            self.__getter.getMapLoc() #download the static image map
        except Exception as openErr:
            print(Fore.RED + "\n\t\t  [!]", openErr)

    def __makeDir(self):
        if os.path.isdir(self.__rootDir + "\\temp\\" + self.__projName + "\\"):
            pass
        else:
            os.system("mkdir " + self.__rootDir + "\\temp\\" + self.__projName + "\\ > nul")
    def __replacer(self):
        print(Fore.CYAN + "\n\t\t    [i] Gathering information...")
        print(Fore.YELLOW + "\n\t\t    [i] Making project folder...")
        try:
            print(Fore.LIGHTGREEN_EX + "\n\t\t  [i] Compiling...")
            with open(self.__rootDir + "\\temp\\" + self.__projName + "\\index.html", "w") as rawFile:
                rawFile.write(self.__rep)
        except Exception as comErr:
            print(Fore.RED + "\n\t\t  [!] An Error has occured while replacing contents.", comErr)
    #make project temp Directory
    def __copyFiles(self):
        try:
            #using a system command for consistency
            os.system("xcopy /S /Y " + self.__rootDir + "\\gens\\*.* " + self.__rootDir + "\\temp\\" + self.__projName + "\\ > nul") #copy the html base files
        except OSError:
            #print an error
            print(Fore.LIGHTRED_EX + "\n\t\t  [!] SYSTEM ERROR!")
            sys.exit(0) #exit when an error has occured
    
    def startGetter(self):
        self.__replacer()

    def __getStartTime(self):
        return self.__DateTime.strftime("[%a] %Y-%m-%d | %H:%M:%S")
    def __getEndTime(self):
        return self.__DateTime.strftime("[%a] %Y-%m-%d | %H:%M:%S")

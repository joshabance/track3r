#import colorama
from colorama import init
from colorama import Fore, Style

#get other modules
from .net import NetChecker
from .api import ApiChecker

#initialize colorama
init()

#prelim checkers
class MainChecker():
	def __init__(self):
		self.__apiChecker = ApiChecker()
		self.__netChecker = NetChecker()
	def checkAPIs(self):
		
		#check bing api
		if self.__apiChecker.getBingApi() == "" or self.__apiChecker.getBingApi() == "enter your api here":
			print(Fore.RED + "\n\t\t [!] Please Enter your BING API in the 'api/api-key.json' file." + Style.RESET_ALL)
		else:
			#check ip stack api
			if self.__apiChecker.getIpStackApi() == "" or self.__apiChecker.getIpStackApi() == "enter your api here":
				print(Fore.RED + "\n\t\t [!] Please Enter you IP Stack API in the 'api/api-key.json' file." + Style.RESET_ALL)
			else:
				print(Fore.YELLOW + "\n\t\t [ok] API Key Checking Done..." + Style.RESET_ALL)

	def checkNet(self):
		#check internet connection
		if self.getNet() == False:
			print(Fore.RED + "\n\t\t [!] INTERNET Connection is required for you to be able to Track IP Addresses." + Style.RESET_ALL)
		else:
			print(Fore.YELLOW + "\n\t\t [ok] Internet Connection present..." + Style.RESET_ALL)

	def getAPI(self):
		if self.__apiChecker.getBingApi() == "" or self.__apiChecker.getBingApi() == "enter your api here":
			return False
		else:
			return True
	def getNet(self):
		if self.__netChecker.checkInternet() == False:
			return False
		else:
			return True
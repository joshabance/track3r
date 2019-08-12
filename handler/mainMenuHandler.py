#append path to import packages
import sys
sys.path.append('../')

#import os for system commands
import os

#import checker
from inc import banner
from handler import subBanners
from handler.singleIpHandler import SingleIP
from handler.helpHandler import HelpTracker
from handler.KeyHandler import mainMenuInterrupt

#colorama
from colorama import init 
from colorama import Fore, Style

#initialize colorama
init()

class MainMenu():
	def displayMenu(self):
		os.system("cls") #clearscreen
		print(Fore.CYAN + banner.pickBanner() + Style.RESET_ALL)
		print(Fore.GREEN + "\n\t\t\t track3r v0.1 - Made Just for FUN :)")
		print(Fore.LIGHTMAGENTA_EX + "\n\t\t\tAVAILABLE OPTIONS")
		print(Fore.LIGHTRED_EX + "\n\t\t\t 1] Single IP Address")
		print(Fore.LIGHTRED_EX + "\t\t\t 2] Multiple TRACK [Not Available]")
		print(Fore.LIGHTRED_EX + "\t\t\t 3] Help (show help options)")
		print(Fore.LIGHTYELLOW_EX + "\n\t\t\t  00] Exit / (type in 'exit')" + Style.RESET_ALL)

	def getUserInput(self):
		__mainInput = '99'
		try:
			while __mainInput != '00':
				print(Fore.LIGHTBLUE_EX + "\n")
				__mainMenu = input("\t\t track3r [1-3/00]#:~> ")
				if __mainMenu == '1' or __mainMenu == 1:
					__newProj = SubMenu()
					__newProj.SIP()
				elif __mainMenu == '2' or __mainMenu == 2:
					pass
					#subBanners.multIP()
				elif __mainMenu == '3' or __mainMenu == 3:
					__getHelp = HelpTracker()
					if __getHelp.main() == True:
						self.getMain()
					else:
						__getHelp.main()
				elif __mainMenu == '' or __mainMenu == None:
					pass
				elif __mainMenu == '00' or __mainMenu == 'exit':
					exitHandler()
					break
				else:
					print(Fore.RED + "\n\t\t   [!] Options Error! Please choose only from the available options.")
		except KeyboardInterrupt:
			__mmKeyInterrupt = mainMenuInterrupt("mainMenu")
			if __mmKeyInterrupt.mainMenuHandling() == False:
				self.getMain()
			else:
				__mmKeyInterrupt.mainMenuHandling()
		except Exception as mainE:
			print(Fore.RED + "\n\t\t  [!]ERROR! ", mainE)
			pass
	def getMain(self):
		self.displayMenu()
		self.getUserInput()

class SubMenu():
	def SIP(self):
		try:
			subBanners.sipBanner()
			print(Fore.LIGHTBLACK_EX + "\n\t\t Enter the IP Address or Web Url [ex: 123.123.123 / www.website.com]")
			print("\t\t\t Type 'back' to go back..")
			__sUrl = "test"
			while __sUrl != None:
				print(Fore.LIGHTGREEN_EX)
				__sUrl = input("\n\t\t  IP / Web :#> ")
				if __sUrl == "" or __sUrl == None:
					pass
				elif __sUrl == "back":
					break
				elif __sUrl.isdigit():
					print(Fore.LIGHTRED_EX + "\n\t\t  [!] Please Enter an IP Address of a Web Hostname / URL.")
				else:
					try:
						__newProc = SingleIP(__sUrl)
						__newProc.main()
					except Exception as e:
						print(e)
						print(Fore.LIGHTRED_EX + "\n\t\t  [!] Err! A problem has occured.")
						print(Fore.YELLOW + "\t\t  [i] Retrying...")
		except Exception as sipE:
			print(Fore.RED + "\n\t\t  [!] " + sipE + Style.RESET_ALL)

def exitHandler():
	print(Fore.YELLOW + "\n\t\t  [ok] Exiting...")
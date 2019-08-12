import sys
sys.path.append("../")

#import colorama
from colorama import init 
from colorama import Fore, Style

#initialize colorama
init()

#import banners
from handler import subBanners

class HelpTracker():
	def __init__(self):
		self.__helpBanner = subBanners.helpBanner()
	def __mainHelp(self):
		print(Fore.CYAN + self.__helpBanner)
		print(Fore.LIGHTGREEN_EX + "\n\t\t  [i] This is just a SIMPLE IP TRACKER Script made from entirely scratch \n\t\t\t using free API Services from various websites which generates \n\t\t\t HTML Document as an output.")
		print(Fore.CYAN + "\n\n\t\t\t [.] Single IP Tracker " + Fore.LIGHTGREEN_EX + " tracks just a Sinlge Ip Address which requires an \n\t\t\t URL/IP to be tracked and Project Name.")
		print(Fore.LIGHTCYAN_EX + "\n\n\t\t\t [.] Multiple IP Tracker[NA] " + Fore.LIGHTGREEN_EX + " tracks Multiple Ip Addresses from user input or list of \n\t\t\t URL/IP to be tracked and Project Name." + Style.RESET_ALL)

	def __menuHelp(self):
		print(Fore.BLUE)
		__helpMenu = 'cont'
		while __helpMenu != 'back':
			__helpMenu = input("\n\t\t   [track3r\\help] ('back' to go back)~#: ")
			if __helpMenu == 'back':
				return True
			elif __helpMenu == '' or __helpMenu == None:
				pass
			else:
				print(Fore.RED + "\n\t\t  [!]Invalid command! Type 'back' to go back...")
	def main(self):
		self.__mainHelp()
		self.__menuHelp()
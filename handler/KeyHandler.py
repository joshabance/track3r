import sys

#import colorama
from colorama import init 
from colorama import Fore, Style

#initialize colorama
init()

#handler Ctrl + C / keyInterrupt
class mainMenuInterrupt():
	def __init__(self, getMenuName):
		self.__menuName = getMenuName

	def mainMenuHandling(self):
		print(Fore.LIGHTYELLOW_EX)
		mainMenuErr = "Yes"
		try:
			while mainMenuErr != "y" or mainMenuErr != "exit":
				mainMenuErr = input("\n\t\t   Do you want to exit now? (exit/y | n/no) ~#: ")
				if mainMenuErr == "y" or mainMenuErr == "exit":
					print(Fore.YELLOW + "\n\t\t  [ok...] Exiting...")
					sys.exit(0)
				elif mainMenuErr == "no" or mainMenuErr == "n":
					return False
				else:
					pass
		except KeyboardInterrupt:
			pass
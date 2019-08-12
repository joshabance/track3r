#import requests to get json response
import requests
import json

#check if ip or url with socket
import socket

#append path to import packages
import sys
sys.path.append('../')

#import api keys
from inc.api import ApiChecker
#import html generator module
from weeb.compiler import MainCompiler

#colorama
from colorama import init 
from colorama import Fore, Style

#initialize colorama
init()

class SingleIP():
	def __init__(self, urlIp):
		self.__urlIp = urlIp
		self.__getApi = ApiChecker()
	def main(self):
		__reqUri = self.__urlIp
		__baseReqUrl = "http://api.ipstack.com/" + __reqUri + "?access_key=" + self.__getApi.getIpStackApi() + "&format=1"

		__response = requests.get(__baseReqUrl)
		__rawJson = __response.json()
		__availability = __rawJson['type']

		__reqType = socket.gethostbyname(__reqUri)

		if __availability == None:
			print(Fore.RED + "\n\t\t  [!] The Website / IP cannot be accessed." + Fore.YELLOW + " Retrying..." + Style.RESET_ALL)
		else:
			sipProjName = "New Proj"
			try:
				while sipProjName != None:
					print(Fore.BLUE)
					sipProjName = input("\n\t\t  [|] Enter PROJECT Name #:> ")
					if sipProjName == "" or sipProjName == None:
						pass
					else:
						__webIP = json.loads(__response.text)['ip']
						print(Fore.YELLOW + "\n\t\t  [+] Getting INFORMATION of " + Fore.CYAN + __reqUri)
						if __reqType == __reqUri:
							print(Fore.LIGHTYELLOW_EX + "\n\t\t    [+] IP Address: " + Fore.CYAN + __reqUri)
						else:
							print(Fore.LIGHTYELLOW_EX + "\n\t\t    [+] Web HOSTNAME: " + Fore.CYAN + __reqUri)

						if __availability == 'ipv4' or __availability == 'ipv6':
							if __availability == 'ipv4':
								print(Fore.LIGHTYELLOW_EX + "\t\t    [i] IPV4: " + Fore.CYAN + __rawJson['ip'])
							elif __availability == 'ipv6':
								print(Fore.LIGHTYELLOW_EX + "\t\t    [i] IPV6: " + Fore.CYAN + __rawJson['ip'])

							#generate HTML Output Document
							print(Fore.YELLOW + "\n\t\t  [i] Generating HTML Document Report")
							sipProj = MainCompiler(__webIP, sipProjName)
							sipProj.startGetter()
						else:
							print(Fore.LIGHTRED_EX + "\t\t  [i] Unknown URI(Uniform Resource Identifier) Type")
			except Exception:
				pass

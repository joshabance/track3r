#import tracking modules
import ipinfo

#requests module for json requesting
import requests

#import system modules
import os
import sys
sys.path.append("../")

#import api keys
from inc.api import ApiChecker

#import colorama
from colorama import init 
from colorama import Fore, Style

#initialize colorama
init()

class GetterMain():
	def __init__(self, reqUri, projName):
		self.__projName = projName
		self.__retrieveIpInfoApi = ApiChecker()
		self.__accessToken = self.__retrieveIpInfoApi.getIpInfoKEY()
		self.__handler = ipinfo.getHandler(self.__accessToken)
		self.__reqUri = reqUri
		try:
			self.__details = self.__handler.getDetails(self.__reqUri)
		except Exception:
			print(Fore.RED + "\n\t\t  [!] An Error has occured!")
			print(Fore.YELLOW + "\n\t\t  [i] Retrying...")
			self.__details = self.__handler.getDetails(self.__reqUri)
		
		#hostname
		try:
			if self.__details.hostname == None or self.__details.hostname == '':
				self.__hostname = "None"
			else:
				self.__hostname = self.__details.hostname
		except AttributeError as hostErr:
			self.__hostname = "None"

		#city
		if self.__details.city == None or self.__details.city == '':
			self.__city = "None"
		else:
			self.__city = self.__details.city
		#region
		if self.__details.region == None or self.__details.region == '':
			self.__region = "None"
		else:
			self.__region = self.__details.region
		#country 
		if self.__details.country == None or self.__details.country == '':
			self.__country = "None"
		else:
			self.__country = self.__details.country
		#postal
		if self.__details.postal == None or self.__details.postal == '':
			self.__postal = "None"
		else:
			self.__postal = self.__details.postal
		#latitude
		if self.__details.latitude == None or self.__details.latitude == '':
			self.__latitude = "0"
		else:
			self.__latitude = self.__details.latitude
		#longitude
		if self.__details.longitude == None or self.__details.longitude == '':
			self.__longitude = "0"
		else:
			self.__longitude = self.__details.longitude
		#get asn number
		try:
			if self.__details.org == None or self.__details.org == '':
				self.__asnName = "None"
			else:
				self.__asnNum = self.__details.org.split()[0] #get the asn number only
		except AttributeError:
			self.__asnNum = "None"
		#get other asn details
		try:
			self.__asn = ASNGetter(self.__asnNum)
			self.__asnCompany = self.__asn.getAsnCompany()
			self.__asnWebsite = self.__asn.getAsnWebsite()
			self.__asnName = self.__asn.getAsnName()
		except Exception as asnErr:
			print(Fore.RED + "\n\t\t  [!]ERROR!", asnErr)

		#get map static image
		try:
			self.__mapGetter = MapGetter(self.__latitude, self.__longitude, self.__projName)
			self.__locMap = self.__mapGetter.getMap()
		except Exception as mapErr:
			print(Fore.RED + "\n\t\t  [!]ERROR!", mapErr)
	
	def getHostName(self):
		return self.__hostname
	def getCity(self):
		return self.__city
	def getRegion(self):
		return self.__region
	def getCountry(self):
		return self.__country
	def getPostal(self):
		return self.__postal
	def getLatitude(self):
		return self.__latitude
	def getLongitude(self):
		return self.__longitude
	def getASN(self):
		return self.__asnNum
	def asnCompany(self):
		return self.__asnCompany
	def asnWebsite(self):
		return self.__asnWebsite
	def asnName(self):
		return self.__asnName
	def getMapLoc(self):
		return self.__locMap

class ASNGetter():
	def __init__(self, asnNumber):
		self.__asnNumber = asnNumber
		try:
			self.__rawAsn = requests.get("https://api.bgpview.io/asn/" + self.__asnNumber).json()
		except requests.exceptions.RequestException as e:
			print(Fore.RED + "\n\t\t  [!] Err! " + e)
			self.__rawAsn = requests.get("https://api.bgpview.io/asn/" + self.__asnNumber).json()
	def getAsnCompany(self):
		return self.__rawAsn['data']['description_short']
	def getAsnWebsite(self):
		return self.__rawAsn['data']['website']
	def getAsnName(self):
		return self.__rawAsn['data']['name']
	
class MapGetter():
	def __init__(self, ipLat, ipLong, projName):
		self.__projName = projName
		self.__ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
		self.__retrieveBingApi = ApiChecker()
		self.__ipLat = ipLat
		self.__ipLong = ipLong
		self.__baseMap = "https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/" + self.__ipLat + "%2C" + self.__ipLong + "/14?mapSize=640,480&mapLayer=TrafficFlow&format=jpeg&pushpin=" + self.__ipLat + "," + self.__ipLong + ";60;&key=" + self.__retrieveBingApi.getBingApi()
	def getMap(self):
		try:
			__map = open(self.__ROOT_DIR + "\\temp\\" + self.__projName + "\\maps.jpg", "wb")
			__rawMap = requests.get(self.__baseMap)
			__map.write(__rawMap.content)
			__map.close()
		except Exception as mapE:
			print(Fore.RED + "\n\t\t  [!] An Error has Occured!", mapE)
#this class checks the API Keys in the api-key.txt
import json

with open("inc\\api\\api-key.txt", "r") as apiFile:
	__rawApi = json.load(apiFile)

	bingAPI = __rawApi['bing-api']
	ipStackAPI = __rawApi['ipstack-api']
	ipinfoAccessKey = __rawApi['ipinfoKey']
		
#open the json file
class ApiChecker():
	def getBingApi(self):
		return bingAPI
	def getIpStackApi(self):
		return ipStackAPI
	def getIpInfoKEY(self):
		return ipinfoAccessKey
		
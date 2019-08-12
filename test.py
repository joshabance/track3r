# import requests

# response = requests.get("http://api.ipstack.com/123.123.123?access_key=ba446c024cd4d56a8fe906d681b3106d&format=1")
# rawjSon = response.json()

# ipType = rawjSon['type']
# print(ipType)

# import socket
# url = "1.1.1.1"
# if socket.gethostbyname(url) == url:
#     print("IP")
# else:
#     print("Hostname")
# import sys

# test = "none here"
# while test != None:
# 	test = input("Enter anything here: ")
# 	if test == "" or test == None:
# 		pass
# 	elif test == "exit":
# 		sys.exit()
# 	else:
# 		print('unknown commands')

# class Outer():
#     """Outer Class"""

#     def __init__(self, num):
#         ## instantiating the 'Inner' class
#         self.num = num
#         self.inner = self.Inner()

#     def reveal(self):
#         ## calling the 'Inner' class function display
#         self.inner.inner_display("Calling Inner class function from Outer class")

#     def getNum(self):
#     	return self.num

#     class Inner(Outer):
#         """Inner Class"""

#         try:
#         	def inner_display(self, msg):
# 				print(msg)
# 	            print(Outer.getNum())
#         except Exception as e:
#         	print(e)
# ## creating an instance of the 'Outer' class
# outer = Outer(10)
# ## calling the 'reveal()' method
# outer.reveal()
import os
import fileinput, re

rootDir = os.path.dirname(os.path.abspath(__file__)) 

with open('test.html', 'r') as file:
    rawData = file.read()

def testText():
	return "World"

rawData = rawData.replace("{text1:}", testText()).replace("{text2:}", "this is my wold nigga").replace("{text3:}", "hehhe here").replace("{text4:}", "just a test one").replace("{text5:}", "test two")

with open('test.html', 'w') as file:
    file.write(rawData)
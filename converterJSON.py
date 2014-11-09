import os

def convert():
	currentPath = os.path.abspath("")
	print (currentPath)
	print (os.listdir(currentPath+"/docsetFolder"))
	for item in os.listdir(currentPath):
		
		if (item != ".DS_Store")
			print(item)
			os.system("xml2json -t xml2json -o jsonFolder/"+item+".json "+item+"/Contents/Resources/Tokens.xml")

convert()

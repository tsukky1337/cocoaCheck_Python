# import libs
import pathlib,glob,json

# function def
def printLog(data):
	if (int(data['MatchCount']) == 0):
		return
		
	str = ''
	str = str + data['Hash'] + '\n'
	str = str + ' '
	str = str + data['Timestamp'] + '\n'
	
	print(str)

def doCheck(logFilePath):
	with open('./' + logFilePath) as jsonFile:
		jsonObj = json.load(jsonFile)
		version = int(jsonObj['ExportVersion'])
		datas = jsonObj['ExposureChecks']
	
		if version == 1:
			for data in datas:
				printLog(data)
					
		elif version == 2:
			for data in datas:
				for file in data['Files']:
					printLog(file)

def main():
	path = pathlib.Path('./')
	logList = list(path.glob('ExposureChecks-*.json'))

	for log in logList:
		doCheck(log.name)

#main
main()

import json
import pyautogui
# import time

# delayBeforeStart = 5

logObj = open("log.txt", "w")
outputFile = open("input.txt", "w")
indexFile = open("fileIndex.txt", "r")



def log(str):
	logObj.write(str)
	logObj.flush()

with open('data.txt', 'r') as file:
    jsonString = file.read().replace('\n', '')

fileIndexNumber = int(indexFile.readline()[0])

data = json.loads(jsonString)
code = data['ref']['solution']['filesContentArr'][fileIndexNumber]['fileContent']

outputFile.write(code)

# time.sleep(delayBeforeStart)

pyautogui.PAUSE = 0.0001


# for line in code:
# 	for ch in line:
# 		if ch != '\t':
# 		    pyautogui.write(ch)
		    
log("Writing Completed")
logObj.close()
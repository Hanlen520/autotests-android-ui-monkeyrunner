import sys
import os
import time
import random

deviceID = sys.argv[4]

########### Initialize device
from com.android.monkeyrunner import MonkeyDevice, MonkeyRunner, MonkeyImage
device = MonkeyRunner.waitForConnection(deviceID)

########### demo_lib import path
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(parentdir + '/lib/')
import demo_lib

########### APP & APK DEFINITIONS
curTestRunDir = sys.argv[1]
curTestCaseScreen=sys.argv[2]
pathToOriginScreenshots=sys.argv[3]
app_name = "ViewSample"
testCaseName = "ViewSample-screenshot"
buildNumber = "XXX"
device_name = "S"
package = "com.android.view"
appActivity = "com.android.view.SampleActivity"
apk = 'ViewSample-debug.apk'

# Create screenshots directory for the test case
curTestCaseScreenDir=curTestRunDir+'/ScreenshotsFromDevice/'+testCaseName
os.makedirs(curTestCaseScreenDir)

#Creating empty arrays
newScreenshotsArray=[]
loadScreenshotsArray=[]
compareScreenshotArray=[]

# Close previous app
device.press('KEYCODE_BACK', 'DOWN_AND_UP')
time.sleep(1)
device.press('KEYCODE_BACK', 'DOWN_AND_UP')
time.sleep(1)

# LAUNCH APP
device.shell(' am start -n ' + package + '/' + appActivity)

# TESTCASE STEPS
steps=["Launch app, take screenshot, compare screenshots"]
print steps

# TESTCASE CONDITIONS
conditions=["Sample-screenshot is started"]
print conditions

# Wait for application to load
time.sleep (5)

################### BEGIN ACTIONS ######################################

#Take screenshot
demo_lib.takeScreenshot(testCaseName,curTestCaseScreenDir,MonkeyRunner,deviceID, newScreenshotsArray, 420, 60, 1280-420, 800-120)
time.sleep(1)

# Buttons Coordinates
buttonsArray = ['add Views','switch Views','replace Views','remove View']
coordsArray = [[200,180],[200,100],[200,260],[200,350]]

# Tap 'Add','Remove','Replace'
for currentCoord in range(4):
		device.touch(int(coordsArray[currentCoord][0]),int(coordsArray[currentCoord][1]), MonkeyDevice.DOWN_AND_UP)
		time.sleep(3)
		demo_lib.takeScreenshot(testCaseName,curTestCaseScreenDir,MonkeyRunner,deviceID, newScreenshotsArray,  420, 60, 1280-420, 800-120)
		time.sleep(2)
os.system('adb -s ' + deviceID + ' shell input keyevent 110')
time.sleep(2)
demo_lib.takeScreenshot(testCaseName,curTestCaseScreenDir,MonkeyRunner,deviceID, newScreenshotsArray,  420, 60, 1280-420, 800-120)
time.sleep(2)

################### END ACTIONS ########################################

################### Comparing screenshots ######################################

#Comparing screenshots
print 'Comparing screenshots'
loadScreenshotsArray= demo_lib.loadOriginalScreenshots(loadScreenshotsArray, pathToOriginScreenshots, testCaseName, MonkeyRunner)
compareScreenshotArray= demo_lib.compareScreenshots(curTestCaseScreenDir, testCaseName, pathToOriginScreenshots, newScreenshotsArray, loadScreenshotsArray)

# Write test case results to report
demo_lib.writeTestResultsTestCase(curTestRunDir,testCaseName,steps,conditions,compareScreenshotArray)

time.sleep(1)

# STOP APP
device.shell('am force-stop '+ package)
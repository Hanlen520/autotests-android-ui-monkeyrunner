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
app_name = "ViewSample"
testCaseName = "ViewSample-random"
buildNumber = "XXX"
device_name = "S"
package = "com.view"
appActivity = "com.view.SampleActivity"
apk = 'ViewSample-debug.apk'

# Close previous app
device.press('KEYCODE_BACK', 'DOWN_AND_UP')
time.sleep(1)
device.press('KEYCODE_BACK', 'DOWN_AND_UP')
time.sleep(1)

# LAUNCH APP
device.shell(' am start -n ' + package + '/' + appActivity)

# TESTCASE STEPS 
steps=["Make 500 random taps through application buttons"]
print steps

# TESTCASE CONDITIONS 
conditions=["ViewSample-random is started"]
print conditions 

# Wait for application to load
time.sleep (2)

################### BEGIN ACTIONS ######################################

# Initialize random and run it through buttons
# Create arrays with button names and coordinates for 1st half of menu

buttonsArray = ['add Views','switch Views','replace Views','remove View']
coordsArray = [[200,180],[200,100],[200,260],[200,350]]

# Initialize random seed number
seedNumb = 10

# Variable for assigning number of seed for the current run - selected randomly by default
random.seed(seedNumb)

# Array with random buttons sequence
randArray = [random.randrange(4) for i in range(100)]

# Create random sequence report
randReport=open(curTestRunDir+'/UISample-randomSeed('+str(seedNumb)+').txt', 'a')

# Run random sequence and write the buttons sequence to a file
for randNum in randArray:
    randReport.write(buttonsArray[randNum]+"\n")
    device.touch(int(coordsArray[randNum][0]),int(coordsArray[randNum][1]), MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.2)

time.sleep (1)

# Check activities
runResult = demo_lib.demo_crash_check(package, apk, deviceID)
time.sleep (1)

################### END ACTIONS ########################################

# Write test case results to report
demo_lib.writeTestResultsTestCase(curTestRunDir,testCaseName,steps,conditions,runResult)

# STOP APP
device.shell('am force-stop '+ package)
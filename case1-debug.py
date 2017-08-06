import sys
import os
import time

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
app_name = "ActivitySwitcher"
testCaseName = "ActivitySwitcher-debug"
buildNumber = "XXX"
device_name = "S"
package = "com.android.activityswitcher"
appActivity = "com.android.acivityswitcher.FirstActivity"
apk = 'ActivitySwitcher-debug.apk'

# Close previous app
device.press('KEYCODE_BACK', 'DOWN_AND_UP')
time.sleep(1)
device.press('KEYCODE_BACK', 'DOWN_AND_UP')
time.sleep(1)

# LAUNCH APP
device.shell(' am start -n ' + package + '/' + appActivity)

# TESTCASE STEPS
steps = ["Tap the button 500x times, Compare activities, check if the app hasn't crashed"]
print steps

# TESTCASE CONDITIONS
conditions = ["ActivitySwitcher is started"]
print conditions

# Wait for application to load
time.sleep(2)

################### BEGIN ACTIONS ######################################

# Buttons Coordinates
coordsArray = [[300,470],[300,530],[300,570],[300,630],[300,670]]

# Test transition
for currentCoord in range(5):
    device.touch(765, 30, MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.5)
    device.touch(600, 70, MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.5)
    device.touch(int(coordsArray[currentCoord][0]),int(coordsArray[currentCoord][1]), MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.5)
    device.touch(765, 30, MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.5)
    device.touch(600, 130, MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.5)
    device.touch(int(coordsArray[currentCoord][0]),int(coordsArray[currentCoord][1]), MonkeyDevice.DOWN_AND_UP)
    time.sleep(0.5)
    # Tap 500x times
    for i in range(30):
        device.touch(500, 650, MonkeyDevice.DOWN_AND_UP)
        print "Number Click: " +str(i+1)
        time.sleep(0.5)

time.sleep(3)
# Check activities
runResult = demo_lib.demo_crash_check(package, apk, deviceID)
time.sleep(1)
################### END ACTIONS ########################################

# Write test case results to report
demo_lib.writeTestResultsTestCase(curTestRunDir, testCaseName, steps, conditions, runResult)
time.sleep(1)

# STOP APP
device.shell('am force-stop ' + package)
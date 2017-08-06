#!/usr/bin/python
__author__ = 'o.budilovsky'

import sys
import os
import datetime

########### demo_lib import path
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir + '/lib/')
import demo_lib

#Device ID
deviceID = sys.argv[1]
buildNumber = sys.argv[2]

try:
    os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "/TestRuns/")
    print os.path.dirname(os.path.abspath(__file__))
    print "Directory for TestRuns was created"
except:
    print os.path.dirname(os.path.abspath(__file__))
    print "Can't create directory"
	
################################### PATHES ###################################################  
pathToOriginScreenshots = os.path.dirname(os.path.abspath(__file__)) + '/data/originScreenshots'
currentTime = datetime.datetime.now().strftime('%d.%m.%Y-%H.%M.%S')
curTestRunDir = os.path.dirname(os.path.abspath(__file__)) + '/TestRuns/TestRun-' + currentTime
curTestCaseLog = curTestRunDir + '/logsFromDevice/'
curTestCaseScreen = curTestRunDir + '/ScreenshotsFromDevice/'

# APP and device names
app_name = "UISamples"
device_name = "Device-X"

# Creating report dirs for current testcase
demo_lib.create_dirs(curTestRunDir, curTestCaseLog, curTestCaseScreen)

# Creating txt file with for results
demo_lib.create_report(curTestRunDir, app_name, buildNumber, currentTime, device_name)

# Creating array with test cases titles	
parentdir2 = os.path.dirname(os.path.abspath(__file__))

# ALL test cases suite
testCases_array=[

   'case1-debug.py',
   'case2-random.py',
   'case3-screenshot.py'
   
]

print "Device: %s" % device_name
print "This is a test run for %s" % app_name

###################################################### RUN test cases SUITE ###################################################
test_count = 1
for testCase in testCases_array:
    print "\n> Running test case %d out of %d - %s" % (test_count, len(testCases_array), testCase[:-3])
    os.system("adb logcat -c")
    os.system("monkeyrunner " + parentdir2+"/data/testCases/" + testCase + ' '+curTestRunDir + ' '+curTestCaseScreen + ' '+pathToOriginScreenshots + ' '+deviceID)
    os.system("adb logcat -d > "+curTestCaseLog+"/"+testCase[:-3]+".txt")
    test_count += 1

# create XLS report	
os.system(
    'python ' + parentdir + '/lib/Report_engine.py ' + curTestRunDir + ' ' + parentdir + '/_Test_reports/ ' + "0" + ' ' + "0" + ' ' + "0")

print'--------------------------------------------------------------------------------'
print '                          TESTS HAVE BEEN FINISHED                             '
print'--------------------------------------------------------------------------------'
print ''
# print '\n> See results in: '+curTestRunDir+'/test_report.txt'
print ('See results in ' + curTestRunDir)
print ''
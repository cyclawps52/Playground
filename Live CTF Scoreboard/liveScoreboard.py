#used for Google Drive API
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import time #used for sleep
import os #used for clear
import math #used for ordinal function
import sys #used for flush

#initial screen clear
os.system('cls')

#appends suffix to number to make it look pretty
def ordinal(n): 
    return "%d%s" % (n, "tsnrhtdd"[(n/10 % 10 != 1)*(n % 10 < 4)*n % 10::4])

#gets command line options and stores them in fancy dictionary file
def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
        argv = argv[1:]
    return opts

#authorize the application
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)

#get refresh rate from arguments or manual entry
from sys import argv
myargs = getopts(argv)
if '-r' in myargs:
    refreshRate = int(myargs['-r'])
else:
    sys.stdout.write('USAGE: "python liveScoreboard.py -r <SECONDS_TO_REFRESH>"')
    exit(0)

#define sheet
sheet = gc.open_by_key("SPREADSHEET KEY GOES HERE") #spreadsheet key code (from URL)
sys.stdout.write('\rGot worksheet!                  ')

#define scoreboard
scoreboard = sheet.get_worksheet(1) #worksheet by ID (starts at index 0)
sys.stdout.write('\rGot scoreboard!                 ')

#begin infinite loop for refresh
while True:
    #print status
    sys.stdout.write('\rREFRESHING NOW!               ')
    
    #define columns
    winners = scoreboard.col_values(2)  # column by ID (starts at index 1)
    sys.stdout.write('\rGot winners column!         ')
    duration = scoreboard.col_values(3)
    sys.stdout.write('\rGot duration column!        ')
    timeSinceLast = scoreboard.col_values(4)
    sys.stdout.write('\rGot time difference column! ')

    for x in winners:
        for i in range(1,1000):
            sys.stdout.write('\b')
    
    del winners[0] #deletes entry from dictionary and updates any dictionaries linked (starts at index 0)
    sys.stdout.write('\rDeleted header row!         ')

    sys.stdout.write('\rBeginning print NOW!        ')

    #print winners
    place = 1
    for x in winners:
        sys.stdout.write('\r                                  ')
        sys.stdout.write("Timestamp: %s\t|\t%s place\t|\t%s\n" % (duration[place], ordinal(place), x))
        place += 1

    #countdown display
    for i in range(1,refreshRate):
        secondsLeft = refreshRate - i  
        sys.stdout.write('\rRefreshing in %3d seconds              ' % secondsLeft)
        sys.stdout.flush()
        time.sleep(1)

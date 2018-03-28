import time
import winsound
import os
 
def waitForMeasure():
    bpm = int(input('Starting BPM: '))
    bpb = int(input('Measure: '))
    timeLimit = int(input('Time between increases (seconds): '))
    bpmIncrease = int(input('Increase by how much (bpm): '))

    sleep = 60.0 / bpm
    counter = 0
    beatCount = 1
    timeForCycle = int(bpm / 60)
    timeChange = int(timeLimit / timeForCycle)
    while True:
        counter += 1
        if counter % bpb:
            print('tick -', beatCount, '| Current BPM:', bpm)
            winsound.Beep(5000, int(1000/bpm))
            time.sleep(sleep)
            beatCount += 1
        else:
            print('TICK -', beatCount, '| Current BPM:', bpm)
            winsound.Beep(8000, int(1000/bpm))
            time.sleep(sleep)
            os.system('cls')
            beatCount = 1
        if (counter >= timeChange and counter % bpb == 0):
            counter = 0
            beatCount = 1
            os.system('cls')
            bpm += bpmIncrease
            sleep = 60 / bpm
            timeForCycle = int(bpm / 60)
            timeChange = int(timeLimit / timeForCycle)

def instantChange():
    bpm = int(input('Starting BPM: '))
    bpb = int(input('Measure: '))
    timeLimit = int(input('Time between increases (seconds): '))
    bpmIncrease = int(input('Increase by how much (bpm): '))

    sleep = 60.0 / bpm
    counter = 0
    beatCount = 1
    timeForCycle = int(bpm / 60)
    timeChange = int(timeLimit / timeForCycle)
    while True:
        counter += 1
        if counter % bpb:
            print('tick -', beatCount, '| Current BPM:', bpm)
            winsound.Beep(5000, int(1000/bpm))
            time.sleep(sleep)
            beatCount += 1
        else:
            print('TICK -', beatCount, '| Current BPM:', bpm)
            winsound.Beep(8000, int(1000/bpm))
            time.sleep(sleep)
            os.system('cls')
            beatCount = 1
        if (counter == timeChange):
            counter = 0
            beatCount = 1
            os.system('cls')
            bpm += bpmIncrease
            sleep = 60 / bpm
            timeForCycle = int(bpm / 60)
            timeChange = int(timeLimit / timeForCycle)

done = 0
while(done == 0):
    print('1. Wait for next measure')
    print('2. Change instantly')
    menuChoice = int(input('Choice: '))
    if(menuChoice == 1):
        waitForMeasure()
        done = 1
    elif(menuChoice == 2):
        instantChange()
        done = 1
    else:
        print('Not a valid option, try again!')
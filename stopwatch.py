import time
print('Press Enter to begin, Afterwards press Enter to click the stopwatch, Press CTRL+C to stop')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 0

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lapNum += 1
        print('Lap #%s: %s (%s)'% (lapNum, totalTime, lapTime), end='')
except KeyboardInterrupt:
    print('\nDone!')
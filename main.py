import time

def thirtyTwoOperation():
    timer_Start = time.time()
    testAdd = 0
    x = 2
    y = 2
    for i in range(10 ** 10):
        x + y
    print("finished first execution")
    for i in range(5 * (10 ** 9)):
        x * y
    print("finished second execution")
    for i in range(2 * (10 ** 9)):
        x / y
    timerEnd = time.time() - timer_Start
    print("The Execution Time for 32-bit Integer Operation: " + str(timerEnd) + " seconds")

def sixtyFourFloatOperation():
    pass

def hardDriveBenchmark1():
    pass

def hardDriveBenchmark2():
    pass

def memoryBenchmark():
    pass

thirtyTwoOperation()
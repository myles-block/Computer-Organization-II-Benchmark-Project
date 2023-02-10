import time
import array as arr

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
    timer_Start = time.time()
    floatX = 1.2
    floatY = 1.2
    for i in range(10 ** 10):
        floatX + floatY
    print("finished first execution")
    for i in range(5 * (10 ** 9)):
        floatX * floatY
    print("finished second execution")
    for i in range(2 * (10 ** 9)):
        floatX / floatY
    timerEnd = time.time() - timer_Start
    print("The Execution Time for 64-bit Integer operation: " + str(timerEnd) + " seconds")


def hardDriveBenchmark1():
    pass

def hardDriveBenchmark2():
    pass

def memoryBenchmark():
    timer_Start = time.time()
    array_Length = (5 * (10 ** 9))
    # there are 4 bytes in an integer
    array = arr.array("i", [0] * array_Length)
    print("reading through array...")
    for index in range(array_Length):
        readit = array[index]
    print("writing through array...")
    for index in range(array_Length):
        array[index] = 2
    timerEnd = time.time() - timer_Start
    print("The Execution Time for Memory Benchmark: " + str(timerEnd) + " seconds")

thirtyTwoOperation()
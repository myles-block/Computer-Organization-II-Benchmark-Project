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
    timer_Start = time.time()
    with open("Hard_Drive_1.txt", "wb") as writer:
        for i in range(10 ** 9):
            writer.write(b"0" * 100) # writing in binary

    print("in reading mode...")
    with open("Hard_Drive_1.txt", "rb") as reader:
        for i in range(10 ** 9):
            reader.read(100)
    timerEnd = time.time() - timer_Start
    print("The Execution Time for Hard Drive Bookmark 1: " + str(timerEnd) + " seconds")

def hardDriveBenchmark2():
    timer_Start = time.time()
    with open("Hard_Drive_2.txt", "wb") as writer:
        for i in range(10 ** 9):
            writer.write(b"0" * 10000)
    
    print("in reading mode")

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

# thirtyTwoOperation()
# sixtyFourFloatOperation()
# memoryBenchmark()
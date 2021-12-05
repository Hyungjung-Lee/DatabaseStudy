import os

def testFun1():
    for i in range(1,10):
        if i%2 == 0:
            print("divided by 2 " + str(i))

def testFun2(argument):
    for i in range(1, argument):
        if i%2 == 0:
            print("divided by 2 " + str(i))

if __name__ == "__main__":
    testFun1()
    testFun2(20)
import math
import numpy


def getCSum(mf, line):
    temp = 0
    tempList = numpy.zeros(mf.__len__(), dtype=numpy.int)
    for i in range(line.__len__()):
        if line[i] == 1:
            tempList = tempList + mf[:, i]
    for item in tempList:
        if item > 0:
            temp = temp + 1
    return temp


def getPc(mp, line):  # 得到Pc
    temp = 0
    tempList = numpy.zeros(mp.__len__(), dtype=numpy.int)
    for i in range(line.__len__()):
        if line[i] == 1:
            tempList = tempList + mp[:, i]
    for item in tempList:
        if item > 0:
            temp = temp + 1
    return temp


def getMO(cSum, Pc, mf):  # 得到适应度
    return cSum / math.sqrt(abs(mf.__len__() * (cSum + Pc)))

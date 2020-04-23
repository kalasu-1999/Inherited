# -*- coding: UTF-8 -*-
import numpy


# 获取频谱矩阵
def getM(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/gcov1.npy")


# 获取测试用例是否通过的结果矩阵
def getR(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/answerNumpy.npy")


# 获取只包含未通过的测试用例的矩阵
def getMF(gcovList, answerList):
    tempList = []
    for i in range(0, answerList.__len__()):
        if answerList[i] == 0:
            tempList.append(gcovList[i])
    return tempList


# 获取未通过测试用例的数目
def getTF(answerList):
    count = 0
    for item in answerList:
        if item == 0:
            count = count + 1
    return count


# 获取fai值
def getSum(mf, line):
    temp = 0
    for i in range(mf.__len__()):
        for j in range(line.__len__()):
            if line[j] > 0 and mf[i][j] > 0:
                temp = temp + 1
                break
    return temp


# 主函数
# dirPosition:错误程序所在文件夹路径（例：/home/temp.c则传入/home）
# 最终会产生一个Inialize.npy文件用于存放产生的初始化种群存放位置在numpyDataDir文件夹中
def Inialize(dirPosition):
    M = getM(dirPosition)
    R = getR(dirPosition)
    # 测试用
    # M = numpy.array([[1, 1, 1, 1, 1, 1],
    #                  [1, 1, 1, 1, 1, 1],
    #                  [1, 1, 1, 1, 1, 1],
    #                  [1, 1, 1, 1, 1, 1],
    #                  [1, 1, 0, 1, 0, 1],
    #                  [1, 1, 0, 1, 0, 1],
    #                  [1, 1, 1, 1, 1, 1],
    #                  [1, 1, 0, 1, 1, 1],
    #                  [1, 1, 1, 1, 1, 1]])
    # M = M.T
    # R = [0, 0, 0, 0, 1, 1]
    MF = getMF(M, R)
    TF = getTF(R)
    n = M[0].__len__()
    nList = numpy.eye(n,dtype=numpy.int)
    i = 1
    flag = 0
    lineList = []
    individual = []
    while i <= n:
        print(i)
        if flag == 0:
            lineList = nList[i - 1]
        cSum = getSum(MF, lineList)
        if cSum != TF:
            flag = 1
            lineNum = 0
            max = 0
            for l in range(n):
                tempList = list(lineList)
                if tempList[l] != 1:
                    tempList[l] = 1
                    cSum = getSum(MF, tempList)
                    if cSum == TF:
                        individual.append(lineList)
                        flag = 0
                        i = i + 1
                        break
                    elif cSum > max:
                        max = cSum
                        lineNum = l
            lineList[lineNum] = 1
        else:
            individual.append(lineList)
            flag = 0
            i = i + 1
    for item in individual:
        print(item)
    numpy.save(dirPosition + "/numpyDataDir/Inialize.npy", individual)


if __name__ == '__main__':
    Inialize("/mnt/e2ae2387-deae-49e8-bbbc-d48d4ca5897d/MyData/创新实践/totinfo_2.0/totinfo/versions.alt/versions.orig/v1")

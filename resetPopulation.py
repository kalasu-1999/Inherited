import numpy
import test_crossover
import test_mutation
import test_selection
import MultiOchiai

np = 300


def lordMF(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/MF.npy")


def lordMP(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/MP.npy")


def getMultiOchiai(mf, mp, population):
    multiOchiaiList = []
    for line in population:
        cSum = MultiOchiai.getCSum(mf, line)
        pc = MultiOchiai.getPc(mp, line)
        if cSum > 0 and pc > 0:
            mo = MultiOchiai.getMO(cSum, pc, mf)
        else:
            mo = 0
        multiOchiaiList.append(mo)
    return multiOchiaiList


# 获取未通过测试用例的数目
def getTF(answerList):
    count = 0
    for item in answerList:
        if item == 0:
            count = count + 1
    return count


# 获取测试用例是否通过的结果矩阵
def getR(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/answerNumpy.npy")


def getInialize(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/Inialize.npy")


def crossover(population):
    return test_crossover.crossover(population, 0.85, 0.5)


def mutation(population):
    return test_mutation.mutation(population, 0.02, 0.04)


def selection(population, popMultiOchiai):
    return test_selection.selection(population, popMultiOchiai, 0.4)


def inherited(oldPop, mf, mp):
    mul = getMultiOchiai(mf, mp, oldPop)
    population1 = numpy.array(selection(oldPop, mul))
    population2 = numpy.array(crossover(population1))
    population3 = mutation(population2)
    mul3 = getMultiOchiai(mf, mp, population3)
    newPopulation = []
    while newPopulation.__len__() < np / 2:
        max = numpy.max(mul)
        for i in range(mul.__len__()):
            if newPopulation.__len__() < np / 2 and mul[i] == max:
                newPopulation.append(oldPop[i])
    while newPopulation.__len__() < np:
        max = numpy.max(mul3)
        for i in range(mul3.__len__()):
            if newPopulation.__len__() < np and mul3[i] == max:
                newPopulation.append(population3[i])
    return numpy.array(newPopulation)


def resetMain(dirPosition):
    population = getInialize(dirPosition)
    mf = lordMF(dirPosition)
    mp = lordMP(dirPosition)
    tf = getTF(getR(dirPosition))
    for i in range(100):
        population = inherited(population, mf, mp)
        j = 0
        while j < population.__len__():
            if MultiOchiai.getCSum(mf, population[j]) != tf:
                population = numpy.delete(population, j, axis=0)
            else:
                j = j + 1
    print("finish")
    mul = getMultiOchiai(mf, mp, population)
    temp = []
    while temp.__len__() < 10:
        max = numpy.max(mul)
        for i in range(mul.__len__()):
            line = []
            if mul[i] == max:
                for j in range(len(population[i])):
                    if population[i][j] == 1:
                        line.append(j)
                if line not in temp:
                    temp.append(line)
                mul[i] = 0
    print(temp)
    numpy.save(dirPosition + "/numpyDataDir/population.npy", population)


if __name__ == '__main__':
    resetMain("/home/kalasu/PycharmProjects/tot_info")

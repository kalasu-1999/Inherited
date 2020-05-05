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
    population1 = oldPop.copy()
    population1 = mutation(population1)
    population2 = numpy.array(crossover(oldPop))
    population3 = numpy.array(selection(oldPop, mul))
    mul1 = getMultiOchiai(mf, mp, population1)
    mul2 = getMultiOchiai(mf, mp, population2)
    mul3 = getMultiOchiai(mf, mp, population3)
    tempPopulation = numpy.vstack((oldPop, population1, population2, population3))
    tempMul = numpy.hstack((mul, mul1, mul2, mul3))
    newPopulation = []
    for i in range(tempMul.__len__()):
        if newPopulation.__len__() < np and tempMul[i] == numpy.max(tempMul):
            newPopulation.append(tempPopulation[i])
            tempMul[i] = 0
    return numpy.array(newPopulation)


def resetMain(dirPosition):
    population = getInialize(dirPosition)
    mf = lordMF(dirPosition)
    mp = lordMP(dirPosition)
    tf = getTF(getR(dirPosition))
    for i in range(100):
        print(i)
        population = inherited(population, mf, mp)
        j = 0
        while j < population.__len__():
            if MultiOchiai.getCSum(mf, population[j]) != tf:
                population = numpy.delete(population, j, axis=0)
            else:
                j = j + 1
    numpy.save(dirPosition + "/numpyDataDir/population.npy", population)
    print(population)


if __name__ == '__main__':
    resetMain("/home/kalasu/PycharmProjects/tot_info")

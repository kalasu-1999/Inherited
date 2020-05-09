import numpy
import test_crossover
import test_mutation
import test_selection
import MultiOchiai

# 种群个体设定数量
np = 300


# 加载MF
def lordMF(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/MF.npy")


# 加载MP
def lordMP(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/MP.npy")


# 获取一个种群对应的适应度列表
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


# 加载初始化种群
def getInialize(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/Inialize.npy")


# 交叉算子
def crossover(population):
    return test_crossover.crossover(population, 0.85, 0.5)


# 变异算子
def mutation(population):
    return test_mutation.mutation(population, 0.02, 0.04)


# 选择算子
def selection(population, popMultiOchiai):
    return test_selection.selection(population, popMultiOchiai, 0.4)


# 遗传函数
def inherited(oldPop, mf, mp):
    # 计算传入种群的适应度
    mul = getMultiOchiai(mf, mp, oldPop)
    # 进行选择算子计算
    population1 = numpy.array(selection(oldPop, mul))
    # 对选择算子计算得到的种群进行交叉算子计算
    population2 = numpy.array(crossover(population1))
    # 对交叉算子计算得到的种群进行变异算子计算
    population3 = mutation(population2)
    # 计算得到的下一代种群的适应度
    mul3 = getMultiOchiai(mf, mp, population3)
    # 用于存放新种群
    newPopulation = []
    # 从原种群中选出10个最优的个体（适应度最高个体）加入新种群
    while newPopulation.__len__() < 10:
        max = numpy.max(mul)
        for i in range(mul.__len__()):
            if newPopulation.__len__() < 10 and mul[i] == max:
                newPopulation.append(oldPop[i])
    # 从下一代种群中选出剩余所需的np/2的个体加新种群
    while newPopulation.__len__() < np:
        max = numpy.max(mul3)
        for i in range(mul3.__len__()):
            if newPopulation.__len__() < np and mul3[i] == max:
                newPopulation.append(population3[i])
    return numpy.array(newPopulation)


# main函数
def resetMain(dirPosition):
    # 加载初始化种群
    population = getInialize(dirPosition)
    # 加载MF
    mf = lordMF(dirPosition)
    # 加载MP
    mp = lordMP(dirPosition)
    # 计算TF值
    tf = getTF(getR(dirPosition))
    # 对种群进行100次遗传
    for i in range(100):
        population = inherited(population, mf, mp)
        # 将fai值不等于TF值的个体剔除
        j = 0
        while j < population.__len__():
            if MultiOchiai.getCSum(mf, population[j]) != tf:
                population = numpy.delete(population, j, axis=0)
            else:
                j = j + 1
    # 遗传结束提示语句
    print("finish")
    # 计算最终得到的种群的适应度值（怀疑度值）
    mul = getMultiOchiai(mf, mp, population)
    # 用于存放前十的怀疑度结果
    temp = []
    # 根据适应度值对将前十怀疑的不相同的个体进行选择加入temp中
    while temp.__len__() < 20:
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
    # 遍历输出temp
    for item in temp:
        print(item)
    # 将计算得到的最终种群存放到指定文件中
    numpy.save(dirPosition + "/numpyDataDir/population.npy", temp)


if __name__ == '__main__':
    resetMain("/home/kalasu/PycharmProjects/tot_info")

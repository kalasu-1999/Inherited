import numpy as np


# pc1为两个染色体发生交叉的概率，pc2为两个染色体中每个基因发生交叉的概率
def crossover(populationNew, pc1, pc2):
    # 将初始化的种群平均分为父种群和母种群
    half = int(len(populationNew) / 2)
    father = populationNew[:half]
    mother = populationNew[half:]
    # 打乱两个种群中染色体的排列顺序
    np.random.shuffle(father)
    np.random.shuffle(mother)
    offSpring = []
    for f1 in range(half):
        son = []
        daugther = []
        if np.random.uniform(0, 1) <= pc1:
            for f2 in range(len(father[f1])):
                if np.random.uniform(0, 1) <= pc2:
                    son.append(father[f1][f2])
                    daugther.append(mother[f1][f2])
                else:
                    son.append(mother[f1][f2])
                    daugther.append(father[f1][f2])
        else:
            son = father[f1]
            daugther = mother[f1]
        offSpring.append(son)
        offSpring.append(daugther)
    return offSpring


# if __name__ == "__main__":
#     # 随机生成一个矩阵
#     population_new = []
#     for i in range(6):
#         population = []
#         for j in range(7):
#             k = np.random.randint(0, 2)
#             population.append(k)
#         population_new.append(population)
#     # 打印生成的矩阵
#     print(population_new)
#     # 华丽的分割线
#     print('------------------------')
#     offspring = crossover(population_new, 0.85, 0.5)
#     # 打印交叉后的矩阵
#     print(offspring)

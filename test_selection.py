import numpy as np


# value为一个list，存放每个染色体的适应度值
# ggap为种群中被选择的个体所占的比例
def selection(populations, values, ggap):
    length = len(values)
    # 轮盘赌选择
    fitness_sum = []
    for f1 in range(len(values)):
        if f1 == 0:
            fitness_sum.append(values[f1])
        else:
            fitness_sum.append(fitness_sum[f1 - 1] + values[f1])

    for f1 in range(len(fitness_sum)):
        fitness_sum[f1] /= sum(values)

    # 选择新种群
    populationNew = []
    for f1 in range(len(values)):
        rand = np.random.uniform(0, 1)
        if len(populationNew) < ggap * length:
            if f1 == 0:
                if 0 < rand <= fitness_sum[f1]:
                    populationNew.append(populations[f1])
                    np.delete(values, f1)
                    np.delete(populations, f1)
            else:
                if fitness_sum[f1 - 1] < rand <= fitness_sum[f1]:
                    populationNew.append(populations[f1])
                    np.delete(values, f1)
                    np.delete(populations, f1)
        else:
            break

    # 重新计算剩余没被选择的染色体
    fitness_sum_left = []
    for f1 in range(len(values)):
        if f1 == 0:
            fitness_sum_left.append(values[f1])
        else:
            fitness_sum_left.append(fitness_sum_left[f1 - 1] + values[f1])

    for f1 in range(len(fitness_sum_left)):
        fitness_sum_left[f1] /= sum(values)

    # 如果第一次选择的染色体个数少于所需个数，继续从剩余的染色体中选择直至达到所需个数
    while len(populationNew) < ggap * length:
        f2 = int(np.random.randint(0, len(values)))
        rand = np.random.uniform(0, 1)
        if f2 == 0:
            if 0 < rand <= fitness_sum_left[f2]:
                populationNew.append(populations[f2])
        else:
            if fitness_sum_left[f2 - 1] < rand <= fitness_sum_left[f2]:
                populationNew.append(populations[f2])

    return populationNew

# if __name__ == "__main__":
#     # 随机生成一个适应度值向量
#     value = []
#     for i in range(6):
#         value.append(np.random.randint(1, 10))
#     # 打印适应度值向量
#     print(value)
#     # 华丽的分割线
#     print('------------------------')
#     # 随机生成一个矩阵
#     population_old = []
#     for i in range(6):
#         population = []
#         for j in range(7):
#             k = np.random.randint(0, 2)
#             population.append(k)
#         population_old.append(population)
#     # 打印生成的矩阵
#     print(population_old)
#     # 华丽的分割线
#     print('------------------------')
#     population_new = selection(population_old, value, 0.4)
#     # 打印选择后的矩阵
#     print(population_new)

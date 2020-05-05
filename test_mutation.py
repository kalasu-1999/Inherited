import numpy as np


def mutation(offSpring, pm1, pm2):
    # Thresholdm 来保证候选分布中的缺陷数量维持在比较低的水平
    thresholdm = 2
    for f in range(len(offSpring)):
        num = 0
        for f1 in range(len(offSpring[f])):
            if offSpring[f][f1] == 1:
                num += 1
        # 如果个体中 “1”的数量小于或等于 Thresholdm,则该个体中的每一个 0 以 Pm1 概率变异为 1
        if num <= thresholdm:
            for f2 in range(len(offSpring[f])):
                if offSpring[f][f2] == 0 and np.random.uniform(0, 1) <= pm1:
                    offSpring[f][f2] = 1
        # 如果个体中 “1”的数量大于 Thresholdm,则该个体中的每一个 1 以 Pm2 概率变异为 0
        else:
            for l in range(len(offSpring[f])):
                if offSpring[f][l] == 1 and np.random.uniform(0, 1) <= pm2:
                    offSpring[f][l] = 0
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
#     print('--------------------------')
#     offspring = mutation(population_new, 0.02, 0.04)
#     # 打印变异后的矩阵
#     print(offspring)

import numpy


def lordMF(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/population.npy")


if __name__ == '__main__':
    # list1 = [[1, 2, 3], [2, 2, 2], [3, 3, 3]]
    # # list1 = [1, 2, 2]
    # list1 = numpy.array(list1)
    # list2 = [[1, 1, 1], [4, 4, 4]]
    # # list2 = [12, 31, 3]
    # list2 = numpy.array(list2)
    # list3 = numpy.vstack((list1, list2))
    # # print(numpy.max(list3))
    # print(list3)
    # list3 = numpy.delete(list3, 1, axis=0)
    # print(list3)
    # list1 = lordMF(
    #     "/mnt/e2ae2387-deae-49e8-bbbc-d48d4ca5897d/MyData/创新实践/totinfo_2.0/totinfo/versions.alt/versions.orig/v1")
    # i = 0
    # for line in list1:
    #     i = i + 1
    #     if i > 10:
    #         break
    #     for j in range(len(line)):
    #         if line[j] == 1:
    #             print(j)
    #     print("===========")
    list1 = []
    list2 = [3]
    list1.append(list2)
    print(list1)
    print("=======")
    list2 = [4,5]
    print(list1)
    list1.append(list2)
    print(list1)

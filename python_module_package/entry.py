# ./arithmetic_module.py
# import arithmetic_module
# print(arithmetic_module.sum(1,2))

# ./statistics_module.py
# import statistics_module
# print(statistics_module.sum(1,2))

# from statistics_module import sum
# print(sum(1,2))

# from statistics_module import sum as ssum
# print(ssum(1,2))


# import number_package.statistics_module
# print(number_package.statistics_module.sum(1,2))

# from number_package.statistics_module import sum
# print(sum(1,2))

from number_package.statistics_module import sum as ssum
print(ssum(1,2))
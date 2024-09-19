# Colyi Chen
# Belugas
# SoftDev
# K06 -- StI/O: Divine Your Destiny!
# 2024-9-18
# Time Spent:
from random import choices

dict = {}

with open("occupations.csv", "r") as file:
    for line in file:
        line = line.strip().replace('"', '').rsplit(",", 1)
        dict[line[1]] = line[0]

del dict["Percentage"]
del dict["99.8"]

print(dict.keys())
print(choices(population=dict.values(), weights=dict.keys()))

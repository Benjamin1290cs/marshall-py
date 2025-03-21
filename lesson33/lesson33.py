# Lesson 33

def mean(num_list):
    return sum(num_list) / len(num_list)

def median(num_list):
    num_list = sorted(num_list)
    midpoint = len(num_list) // 2

    if len(num_list) % 2 == 0:
        return (numlist[midpoint] + num_list[midpoint - 1]) / 2
    else:
        return num_list[midpoint]

from random import seed
from random import randrange

seed(2)
data = [randrange(1,100) for _ in range(randrange(10,30))]
print(f"Our random dataset: {data}")
print(f"Mean of our dataset: {mean(data)}")
print(f"Our sorted dataset: {sorted(data)}")
print(f"Median of our dataset: {median(data)}")
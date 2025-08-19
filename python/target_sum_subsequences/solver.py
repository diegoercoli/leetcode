import random
import numpy as np
from utils import *
# --- Input setup ---
n = 10
random.seed(15)
v = [random.randint(1, 10) for _ in range(n)]
v.sort(reverse=True)  # sort in descending order
max_value = v[0]

# DP table: rows = items, cols = sum values
P = np.array([[set() for _ in range(max_value+1)] for _ in range(n)], dtype=object)

print("Input array:", v)
print("Max value:", max_value)
print("DP table shape:", P.shape)

# --- DP filling ---
for index_item in range(n):
    current_value = v[index_item]
    for sum_value in range(max_value+1):
        prefix = f"{index_item}-th element: {current_value}, sum={sum_value}"
        if index_item == 2 and sum_value == 4:
            print("I'm here")
        if current_value == sum_value:
            # base case: single element matches sum
            P[index_item,sum_value].add(Subsolution(v=[current_value]))

        elif current_value < sum_value:
            # case 1: take current value
            set1 = set()
            prev_set = take_solution(P, index_item-1, sum_value - current_value)
            for sub in prev_set:
                sub_copy = sub.copy()
                sub_copy.add(current_value)
                set1.add(sub_copy)

            # case 2: don't take current value
            set2 = take_solution(P, index_item-1, sum_value)

            # combine
            final_set = set1.copy()
            for sub in set2:
                final_set.add(sub)
            P[index_item,sum_value] = final_set#set1.union(set2)
            print(prefix)
            content = [[s.items] for s in P[2,4]]
            print(f"P[2,4] = {content}")
            #set1.clear()
            #set2.clear()


# --- Output ---
target_sum = max_value
print(f"\nAll solutions for target sum = {target_sum}:\n")
for sol in P[n-1][target_sum]:
    print(sol)
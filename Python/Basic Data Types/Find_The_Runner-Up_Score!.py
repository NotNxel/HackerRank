# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python
# Credit : Neel Nikhil Pappu

# ========================
#         Solution
# ========================

n=int(input())
a=list(map(int, input().split()))
a=list(set(a))
a.sort()
print(a[len(a)-2])

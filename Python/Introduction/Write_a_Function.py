# ========================
#       Information
# ========================

# Direct Link: www.hackerrank.com/challenges/write-a-function/problem
# Difficulty: Medium
# Max Score: 10
# Language: Python
# Credit : Neel Nikhil Pappu

# ========================
#         Solution
# ========================

def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap= False
        else:
            leap=True
    else:
        leap=False
    return leap

year = int(input())
print(is_leap(year))

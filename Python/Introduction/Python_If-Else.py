# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-if-else/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python
# Credit : Neel Nikil Pappu

# ========================
#         Solution
# ========================

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==0 and n<5 and n>2:
        print("Not Weird")
    if n%2==0 and n<20 and n>6:
        print("Weird")
    if n%2==0 and n>21 :
        print("Not Weird")
    elif n%2!=0 or n==20 :
        print("Weird")

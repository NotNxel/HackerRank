# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python
# Credit : Neel Nikil Pappu

# ========================
#         Solution
# ========================

X = int(input()) + 1;
Y = int(input()) + 1;
Z = int(input()) + 1;
N = int(input());
list = [];
for x in range(0,X):
    for y in range(0,Y):
        for z in range(0, Z): 
            if (x + y + z) != N: 
                list.append([x,y,z]);

print(list);

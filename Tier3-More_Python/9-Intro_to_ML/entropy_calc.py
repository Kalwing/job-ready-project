import math

P = [2/3, 1/3]
entropy = - sum([Pi * math.log2(Pi) for Pi in P])
print(entropy)

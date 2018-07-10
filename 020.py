import math

def compute(num):
  num = str(math.factorial(num))
  ans = sum(int(d) for d in num)
  return ans

print(compute(100))
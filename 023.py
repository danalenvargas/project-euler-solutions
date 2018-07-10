import math

abundantList = []
numList = list(range(28124))

def getDivSum(num):
  if num != 1:
    sum = 1
    for i in range(2, math.floor(math.sqrt(num)) + 1):
      if num%i == 0:
        if num/i == i:
          sum += i
        else:
          sum += i + num//i
    return sum
  elif num == 1:
    return 0
    
def compute():
  for n in range(12, 28123):
    if getDivSum(n) > n:
      abundantList.append(n)
  
  for i in range(len(abundantList)):
    for j in range(i, len(abundantList)):
      x = abundantList[i] + abundantList[j]
      if x < 28124:
        numList[x] = 0
  
  return sum(numList)
  
print(compute())
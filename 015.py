import math

def lattice(gridWidth, gridHeight):
  return math.factorial(gridWidth + gridHeight)/(math.factorial(gridWidth) * math.factorial(gridHeight))
  

print(lattice(20, 20))
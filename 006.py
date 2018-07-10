def compute():
  sumOfSquares = sum(i**2 for i in range(1, 101))
  squareOfSum = sum(range(1, 101))**2
  return squareOfSum - sumOfSquares
  
print(compute())
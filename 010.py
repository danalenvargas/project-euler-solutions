def getPrimeSum(limit):
  primeList = []
  sum = 0
  for num in range(2, limit):
    for prime in primeList:
      if num % prime == 0:
        break
    else:
      sum += num
      primeList.append(num)
  return sum
      
print(getPrimeSum(2000000))

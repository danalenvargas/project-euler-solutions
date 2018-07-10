import math

def getPrimeFactors(num):
  pf = []
  while(num > 1):
    for i in range(2, math.floor(num/2)+1):
      if num%i == 0:
        pf.append(i)
        num = num/i
        break
    else:
      pf.append(num)
      break

  return pf
  
def getLargestPrimeFactor(pf):
  return pf[len(pf)-1]
	  
print (getLargestPrimeFactor(getPrimeFactors(600851475143)))
print (getPrimeFactors(600851475143))
import decimal

def compute():
  topN = 0
  topCount = 0
  for n in range(1, 1000):
    frac = decimal.Decimal(1/n)
    frac = str(frac)[2:]
    if len(frac) > 15:
      for j in range(len(frac)//2):
        count = 0
        for i in range(j, len(frac)//2 + j//2):
          #count += 1
          #print(frac[:i+1], frac[i+1:i+i+2])
          if frac[j:i+1] == frac[i+1:i+i+2-j]:
            count = i+1 - j
            if count >= topCount:
              print(n, frac, count, frac[j:i+1], frac[i+1:i+i+2-j], i, j)
              topCount = count
              topN = n
            break
        if topCount == count:
          break
  return topN

print(compute())
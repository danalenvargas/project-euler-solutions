sum = 0
prev = 1
n = 2
while (n < 4000000):
  if n%2 == 0:
    sum += n
  new = n + prev
  prev = n
  n = new
print(sum)
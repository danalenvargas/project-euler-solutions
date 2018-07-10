def compute(num):
  return sum(int(n) for n in str(num))

print(compute(2 ** 1000))
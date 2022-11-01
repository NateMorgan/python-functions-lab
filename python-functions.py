import math

def sum_to(n):
  output = 0
  for i in range(1,n+1):
    output += i
  return output

assert sum_to(6) == 21 , "sum_to failed testing"
assert sum_to(10) == 55 , "sum_to failed testing"

def largest(list):
  max = -math.inf
  for i in list:
    if i > max:
      max = i
  return max

assert largest([1, 2, 3, 4, 0]) == 4, "largest failed testing"
assert largest([10, 4, 2, 231, 91, 54]) == 231, "largest failed testing"
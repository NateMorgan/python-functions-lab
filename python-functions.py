def sum_to(n):
  output = 0
  for i in range(1,n+1):
    output += i
  return output

assert sum_to(6) == 21 , "sum_to failed testing"
assert sum_to(10) == 55 , "sum_to failed testing"
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

def occurences(str1, str2):
  output = 0
  for i in range(len(str1)-len(str2)+1):
    if str1[i:i+len(str2)] == str2:
      output += 1
  return output

assert occurences('fleep floop', 'e') == 2, "occurences failed testing"
assert occurences('fleep floop', 'p') == 2, "occurences failed testing"
assert occurences('fleep floop', 'ee') == 1, "occurences failed testing"
assert occurences('fleep floop', 'fe') == 0, "occurences failed testing"

def product(*args):
  output = 1
  for arg in args:
    output *= arg
  return output

assert product(-1,4) == -4, "product failed testing"
assert product(2,5,5) == 50, "product failed testing"
assert product(4,.5,5) == 10.0, "product failed testing"
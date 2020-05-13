from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

# sequence for ref
# 0=0 1=1 2=1 3=2 4=3 5=5 6=8 7=13
# 0=2 1=1 2=3 3=4 4=7 5=11 6=18 7=29


def test_fibonacci_zero():
 actual = fibonacci(0)
 expected = 0
 assert actual == expected

def test_fibonacci_one():
 actual = fibonacci(1)
 expected = 1
 assert actual == expected

def test_fibonacci_two():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fibonacci_five():
  actual = fibonacci(5)
  expected = 5
  assert actual == expected

def test_lucas_zero():
  actual = lucas(0)
  expected = 2
  assert actual == expected
  
def test_lucas_one():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_two():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lucas_five():
  actual = lucas(5)
  expected = 11
  assert actual == expected

def test_sum_series_zero():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_sum_series_three():
  actual = sum_series(3)
  expected = 2
  assert actual == expected

def test_sum_series_triple():
  actual = sum_series(0, 2, 1)
  expected = 2
  assert actual == expected

def test_sum_series_custom():
  actual = sum_series(4, 3, 4)
  expected = 18
  assert actual == expected

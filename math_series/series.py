#recursion call fib inside fib
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  elif n == 2 :
    return 1
  else:
    return ( fibonacci(n-1) + fibonacci(n-2) )

# print(fibonacci(5)) 

#recursion lucas function
def lucas(n):
  if n == 0:
    return 2
  elif n == 1:
    return 1
  elif n == 2 :
    return 3
  else:
    return ( lucas(n-1) + lucas(n-2) )

# print(lucas(5)) 

def sum_series(n, opt1=0, opt2=1):
    if n == 0:
      return opt1
    elif n == 1:
      return opt2
    else:
      return ( sum_series(n-1, opt1, opt2) + sum_series(n-2, opt1, opt2) )

print(sum_series(4, 1, 2)) 

if __name__ == "__main__":
  n = int(input())


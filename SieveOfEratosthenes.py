#Sieve of Eratosthenes method to find prime numbers

def stevyEr(n):
  primeList = set()
  notPrimeList = set()
  for j in range(2, n+1):
    if j not in notPrimeList:
     new_val = {j*k for k in range(j, n) if j*k<=n}
     notPrimeList = notPrimeList.union(new_val)
     primeList.add(j)
  return primeList

# Example Code Execution
print(stevyEr(100))


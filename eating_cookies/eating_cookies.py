#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
counter = 0

def eating_cookies(n, cache=None):
  global counter
  if n <= 0:
    None
    # N = number of cookies
    # 3 ways to subtract a cookie
    # Each time we subtract a cookie (meaning he ate the cookie(s)), we increase the counter += 1
    #n = 4
  else:
    for i in range(1, 4):
      if n > 0:
        print("before n", n)
        n = n - i
        counter += 1
        print("n", n)
        eating_cookies(n)
  return counter

print(eating_cookies(4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max = prices[1]
  least = prices[0]
  max_index = 0
  if len(prices) < 2:
    return print("Not enough data")
  for i in range(2, len(prices) - 1):
    if prices[i] > max:
      max = prices[i]
      max_index = i
  for e in range(1, max_index):
    if prices[e] < least:
      least = prices[e]
  return max - least
  
find_max_profit([1050, 270, 1540, 3800, 2])





if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
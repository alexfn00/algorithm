def normal_cost(bulbs):
  print('origin:', bulbs)
  cost = 0
  for index, bulb in enumerate(bulbs):
    if bulb == 1:
      continue
    else:
      cost += 1
      bulbs[index] = 1
      print('bulbs:', cost, bulbs)
      for i in range(index+1, len(bulbs)):  # 翻转后续元素
        bulbs[i] = int(not bulbs[i])
        cost += 1
        print('\tbulbs:', cost, bulbs)
  return cost


def greedy_cost(bulbs):
  print('origin:', bulbs)
  cost = 0
  for index, bulb in enumerate(bulbs):
    state = bulb     # 记录当前状态：0或1
    if cost % 2 != 0: state = int(not bulb)   # cost为奇数时表示翻转
    
    if state == 0:  # 当前状态为0时，增加一次开关操作
      cost += 1

      if bulbs[index]  == 0:
        bulbs[index] = 1
    print('bulbs:', index, bulbs)
  return cost

bulbs = [0, 1, 0]

# cost = normal_cost(bulbs)
cost = greedy_cost(bulbs)
print('cost =', cost)

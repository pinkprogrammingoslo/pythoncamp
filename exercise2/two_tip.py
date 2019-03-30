cost = float(input('How much did the meal cost? '))

global tip
if cost > 100:
    tip = cost * 0.05
else:
    tip = cost * 0.1

print('Suggested tip for a meal that costs {}, is {}.'.format(cost, round(tip, 2)))

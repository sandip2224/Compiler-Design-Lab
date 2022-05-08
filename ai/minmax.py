import math


def MinMax(curr, i, maxTurn, scores, target):
    if curr == target:
        return scores[i]

    if maxTurn:
        return max(MinMax(curr+1, i*2, False, scores, target), MinMax(curr+1, i*2 + 1, False, scores, target))
    else:
        return min(MinMax(curr+1, i*2, True, scores, target), MinMax(curr+1, i*2 + 1, True, scores, target))


scores = [3, 5, 2, 9, 12, 5, 23, 23]
depth = math.log(len(scores), 2)
print('The optimal value = ', end='')
print(MinMax(0, 0, True, scores, depth))

ans = []


def tsp(graph, v, cur, n, count, cost):

    if count == n and graph[cur][0]:
        ans.append(cost + graph[cur][0])
        return
    for i in range(n):
        if v[i] == False and graph[cur][i]:
            v[i] = True
            tsp(graph, v, i, n, count+1, cost + graph[cur][i])
            v[i] = False


n = 4
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]

v = [False for i in range(n)]
v[0] = True
tsp(graph, v, 0, n, 1, 0)
print(min(ans))

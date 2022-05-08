def TowerOfHanoi(n, src, dest, aux):
    if n == 0:
        return
    TowerOfHanoi(n-1, src, aux, dest)
    print("Moving disk", n, "from", src, "->", dest)
    TowerOfHanoi(n-1, aux, dest, src)


n = 4
TowerOfHanoi(n, 'A', 'C', 'B')

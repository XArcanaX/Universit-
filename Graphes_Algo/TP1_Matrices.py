import numpy as np

A = np.random.randint(0, 2, size=(6, 6))

print(A)



def is_directed(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != A[j][i]:
                return True
    return False
print(is_directed(A))

def remove_edge(x, y, A):
    A[x][y] = 0
    return A
print(remove_edge(0, 1, A))

def has_path(x, y, k, A):
    if k == 0:
        return x == y
    for i in range(len(A)):
        if A[x][i] == 1 and has_path(i, y, k-1, A):
            return True
    return False
print(has_path(0, 1, 2, A))

def vertex_degree(x, G):
    if is_directed(G):
        in_degree = sum(G[i][x] for i in range(len(G)))
        out_degree = sum(G[x][i] for i in range(len(G)))
        return (in_degree, out_degree)
    else:
        return sum(G[x][i] for i in range(len(G)))
print(vertex_degree(0, A))
    
def is_complete(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if i != j and M[i][j] != 1:
                    return False
    return True
print(is_complete(A))
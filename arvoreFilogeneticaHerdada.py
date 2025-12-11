import sys

def solve_case(N, L, leaves):
    size = 2 * N
    total_cost = 0
    root_chars = []
    
    
    for col in range(L):
        sets = [set() for _ in range(size)]
        # folhas
        for i in range(N):
            sets[N + i] = { leaves[i][col] }
        col_cost = 0
        # nós internos (bottom-up)
        for node in range(N - 1, 0, -1):
            left = sets[2 * node]
            right = sets[2 * node + 1]
            inter = left & right
            if inter:
                sets[node] = inter
            else:
                sets[node] = left | right
                col_cost += 1
        total_cost += col_cost
        root_chars.append(max(sets[1]))   # desempate: caractere mais alto
    return "".join(root_chars), total_cost
def main():
     while True:
        line = sys.stdin.readline()
        if not line:
            break    # fim do arquivo
        line = line.strip()
        if not line:
            continue
        N, L = map(int, line.split())
                # regra de parada
        if N == 0 and L == 0:
            break
        # ler as N sequências
        leaves = []
        for _ in range(N):
            s = sys.stdin.readline().strip()
            leaves.append(s)
        root_seq, cost = solve_case(N, L, leaves)
        print(root_seq, cost)
if __name__ == "__main__":
    main()

import sys
import math

class PhylogeneticTreeSolver:
    
    def __init__(self):
        # Alfabeto completo dos 20 aminoácidos comuns.
        self.ALPHABET = [
            'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 
            'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'
        ]
        # Mapeamento para indexação eficiente (0 a 19)
        self.char_to_index = {char: i for i, char in enumerate(self.ALPHABET)}
        self.num_chars = len(self.ALPHABET)
        self.INF = float('inf')

    def calculate_min_cost_for_child(self, parent_char_index, child_dp_row):
        """
        Calcula o custo mínimo do ramo (Pai -> Filho) somado ao custo da subárvore do filho.
        """
        
        # Custo mínimo se o caractere do filho for o mesmo do pai (custo da aresta = 0)
        cost_match = child_dp_row[parent_char_index]

        # Custo mínimo se o caractere do filho for diferente do pai (custo da aresta = 1)
        min_cost_child_not_parent = self.INF
        for c_prime_index, cost in enumerate(child_dp_row):
            if c_prime_index != parent_char_index:
                min_cost_child_not_parent = min(min_cost_child_not_parent, cost)

        cost_mismatch = 1 + min_cost_child_not_parent
        
        # O custo parcial é o mínimo entre manter o match (0) ou forçar o mismatch (1)
        return min(cost_match, cost_mismatch)
        

    def solve(self, N: int, L: int, sequences: list[str]) -> tuple[str, int]:
        if N == 0 or L == 0:
            return "", 0

        optimal_ancestor = []
        total_min_cost = 0
        num_nodes = 2 * N
        root_node = 1

        for j in range(L):
            DP = [[self.INF] * self.num_chars for _ in range(num_nodes)]

            # 1. Programação Dinâmica Bottom-Up (Folhas -> Raiz)
            for u in range(num_nodes - 1, 0, -1):
                
                # A. Caso Base: Nó Folha (índices N até 2N-1)
                if u >= N:
                    seq_index = u - N
                    fixed_char = sequences[seq_index][j]
                    
                    try:
                        fixed_char_index = self.char_to_index[fixed_char]
                        DP[u][fixed_char_index] = 0
                    except KeyError:
                        # Ignora caracteres inválidos ou fora do alfabeto
                        continue 
                
                # B. Caso de Transição: Nó Interno
                else:
                    v1, v2 = 2 * u, 2 * u + 1

                    for c_index in range(self.num_chars):
                        
                        # Custo Parcial para v1 e v2
                        min_cost_v1 = self.calculate_min_cost_for_child(c_index, DP[v1])
                        min_cost_v2 = self.calculate_min_cost_for_child(c_index, DP[v2])
                            
                        # DP[u][c] é a soma dos custos parciais
                        DP[u][c_index] = min_cost_v1 + min_cost_v2

            # 2. Recuperação da Solução na Raiz (Nó 1)
            
            # Coleta (custo, caractere) para desempate lexicográfica
            costs_at_root = []
            for c_index, c in enumerate(self.ALPHABET):
                costs_at_root.append((DP[root_node][c_index], c))
            
            # min() ordena por custo e desempata lexicograficamente pelo caractere
            min_cost_tuple = min(costs_at_root)
            
            min_pos_cost = min_cost_tuple[0]
            optimal_char = min_cost_tuple[1]
            
            # Acumula resultados globais
            total_min_cost += min_pos_cost
            optimal_ancestor.append(optimal_char)

        return "".join(optimal_ancestor), int(round(total_min_cost))

# ----------------- Função Principal para Entrada/Saída -----------------

def main():
    solver = PhylogeneticTreeSolver()
    
    # Redireciona a entrada/saída para ser mais rápido em submissões
    try:
        # Tenta ler N e L da entrada padrão
        while True:
            line = sys.stdin.readline().split()
            
            if not line:
                break
                
            N, L = map(int, line)
            
            # Condição de parada
            if N == 0 and L == 0:
                break
            
            # Lê as N sequências
            sequences = [sys.stdin.readline().strip() for _ in range(N)]
            
            optimal_seq, min_cost = solver.solve(N, L, sequences)
            
            print(f"{optimal_seq} {min_cost}")

    except Exception:
        # Se ocorrer EOF ou erro de leitura/formato, o loop encerra
        pass

if __name__ == "__main__":
    main()
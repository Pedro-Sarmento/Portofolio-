def ac3(csp):
    queue = csp.C
    while queue:
        arc_value = queue.pop(0)  # arc_value = [Xi, Xj]
        Xi = arc_value[0]
        Xj = arc_value[1]

        if revise(csp, Xi, Xj):
            if len(csp.D[Xi]) == 0:
                return False  # Se o CSP não tiver solução dá return False
            for Xk in csp.N[Xi]:
                if Xk != Xj:
                    queue.append([Xk, Xi])
    return True

def revise(csp, Xi, Xj):
    revised = False
    # Se o valor de Xi não existir no dominio de Xj
    for x in csp.D[Xi][:]:
        if not any(x != y for y in csp.D[Xj]):
            csp.D[Xi].remove(x)
            revised = True
    return revised

class CSP:
    def __init__(self):
        self.V = []  # lista de variáveis
        self.C = []  # lista de restrições(constrains)(arcs)
        self.D = {}  # dicionário de domínios para cada variável
        self.N = {}  # dicionário de neighbors para cada variável
    
    def add_variable(self, variable, domain):
        self.V.append(variable)
        self.D[variable] = domain
        self.N[variable] = []
    
    def add_constraint(self, variable1, variable2):
        self.N[variable1].append(variable2)
        self.N[variable2].append(variable1)
        self.C.append([variable1, variable2])
  
def solve_sudoku():
    puzzle = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]
    # cria objeto CSP
    csp = CSP()

    # adicionar variáveis ​​ao objeto CSP
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                csp.add_variable(f"V{i}{j}", [1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                csp.add_variable(f"V{i}{j}", [puzzle[i][j]])
    # print(csp.show_variable())
    # adicionar restrições ao objeto CSP
    for row in range(9):
        for column in range(9):
            # verifique se há restrições na linha
            for row_position in range(9):
                if row_position != column:
                    csp.add_constraint(f"V{row}{column}", f"V{row}{row_position}")

            # verifique se há restrições na coluna
            for column_position in range(9):
                if column_position != row:
                    csp.add_constraint(f"V{row}{column}", f"V{column_position}{column}")

            # verifique se há restrições na grade 3x3
            row_start = row // 3 * 3
            col_start = column // 3 * 3

            # x -> row
            # y -> column
            for x in range(3):
                for y in range(3):
                    if row_start + x != row and col_start + y != column:
                        csp.add_constraint(f"V{row}{column}", f"V{row_start + x}{col_start + y}")

    # resolver o CSP usando o algoritmo AC-3
    if ac3(csp):
        print("""Sudoku por resolver:       
 +-------+-------+-------+
 | 0 0 3 | 0 2 0 | 6 0 0 |
 | 9 0 0 | 3 0 5 | 0 0 1 |
 | 0 0 1 | 8 0 6 | 4 0 0 |
 |-------+-------+-------|
 | 0 0 8 | 1 0 2 | 9 0 0 |
 | 7 0 0 | 0 0 0 | 0 0 8 |
 | 0 0 6 | 7 0 8 | 2 0 0 |
 |-------+-------+-------|
 | 0 0 2 | 6 0 9 | 5 0 0 |
 | 8 0 0 | 2 0 3 | 0 0 9 |
 | 0 0 5 | 0 1 0 | 3 0 0 |
 +-------+-------+-------+
        """)
        # imprime o Sudoku resolvido dentro de uma grid
        print("Sudoku Resolvido:")
        print("+-------+-------+-------+")
        for i in range(9):
            for j in range(9):
                if j == 0:
                    print("| ", end='')
                print(csp.D[f"V{i}{j}"][0], end=" ")
                if j == 2 or j == 5:
                    print("|", end=" ")
            print("|")
            if i == 2 or i == 5:
                print("-" * 25)
        print("+-------+-------+-------+")
    else:
        print("Sem solução.")




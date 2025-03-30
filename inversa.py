def minor(matrix, row, col):
    result = []
    for i in range(len(matrix)):
        if i == row:
            continue
        new_row = []
        for j in range(len(matrix[i])):
            if j != col:
                new_row.append(matrix[i][j])
        result.append(new_row)
    return result

def cofactor(matrix, i, j):
    minor_det = determinant_gauss(minor(matrix, i, j))
    return (-1) ** (i + j) * minor_det

def adjugata(matrix):
    size = len(matrix)
    cofactor_matrix = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append(cofactor(matrix, i, j))
        cofactor_matrix.append(row)

    new_matrix = []

    for j in range(size):
        new_row = []
        for i in range(size):
            new_row.append(cofactor_matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix

def inversa(matrix):
    if len(matrix) == 1:
       return [[1 / matrix[0][0]]]
    
    if len(matrix) != len(matrix[0]):
        return "Matricea nu este patratica"
    
    det = determinant_gauss(matrix)
    if det == 0:
        return "determinant zero -> matricea nu are inversa"
    
    adj = adjugata(matrix)
    size = len(matrix)
    inversa = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append(adj[i][j] / det)
        inversa.append(row)
    return inversa

def permuta(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def eliminare_gaussiana(matrix):
    n = len(matrix)
    permutari = 0

    for i in range(n):
        pivot = i
        for r in range(i, n):
            if abs(matrix[r][i]) > abs(matrix[pivot][i]):
                pivot = r

        if matrix[pivot][i] == 0:
            return 0, permutari  
        
        if pivot != i:
            permuta(matrix, i, pivot)
            permutari += 1

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
                
    return matrix, permutari

def determinant_gauss(matrix):
    matrix_copy = [row[:] for row in matrix]
    triangular_matrix, num_permutations = eliminare_gaussiana(matrix_copy)

    if triangular_matrix == 0:
        return 0
    
    det = 1
    for i in range(len(triangular_matrix)):
        det *= triangular_matrix[i][i]
    det *= (-1) ** num_permutations

    return round(det, 2)

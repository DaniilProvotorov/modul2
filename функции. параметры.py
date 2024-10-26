def get_matrix(n, m, value):
    matrix = []
    for i in range(1, n+1):
        var = []
        matrix.append(var)
        for j in range(1, m + 1):
            var.append(value)
    print(matrix)

    
get_matrix(3, 5, 42)
"""Module 4 zyLab starter: matrix algebra and matrix equations."""


def copy_matrix(matrix):
    """Return a row-by-row copy of a matrix."""
    return [row[:] for row in matrix]


def validate_matrix(matrix):
    """Raise ValueError if matrix is empty or has uneven row lengths."""
    if len(matrix) == 0:
        raise ValueError("matrix must have at least one row")

    width = len(matrix[0])
    if width == 0:
        raise ValueError("matrix rows must have at least one entry")

    for row in matrix:
        if len(row) != width:
            raise ValueError("all matrix rows must have the same length")


def matrix_size(matrix):
    """Return the size of a matrix as (rows, columns)."""
    validate_matrix(matrix)
    return len(matrix), len(matrix[0])


def same_size(A, B):
    """Return True when two matrices have the same size."""
    validate_matrix(A)
    validate_matrix(B)
    return matrix_size(A) == matrix_size(B)


def add_matrices(A, B):
    """Return A + B."""
    if not same_size(A, B):
        raise ValueError("matrices must have the same size")

    result = []
    for row in range(len(A)):
        new_row = []
        for col in range(len(A[0])):
            # Level 1: Find and fix the arithmetic error on this line.
            new_row.append(A[row][col] + B[row][col])
        result.append(new_row)
    return result


def scalar_multiply(scalar, A):
    """Return scalar times A."""
    validate_matrix(A)

    result = []
    for row in range(len(A)):
        new_row = []
        for col in range(len(A[0])):
            # Level 1: Find and fix the arithmetic error on this line.
            new_row.append(A[row][col] * scalar)
        result.append(new_row)
    return result


def subtract_matrices(A, B):
    """Return A - B."""
    return add_matrices(A, scalar_multiply(-1, B))


def can_multiply(A, B):
    """Return True when the product AB is defined."""
    # Level 2:
    validate_matrix(A)
    validate_matrix(B)
    return len (A[0])== len(B)
    # 1. Validate both matrices.
    # 2. Compare the number of columns of A with the number of rows of B.
    pass


def matrix_multiply(A, B):
    """Return the matrix product AB."""
    # Level 2:
    if not can_multiply(A, B):
      raise ValueError("matrices must have the same size") 
    result = [] 
    for row in range(len(A)):
        new_row=[]
        for col in range(len(B[0])):
            total = 0
            for index in range(len(A[0])):
                total += A[row][index] * B[index][col]
            new_row.append(total)
        result.append(new_row)
        
    return result
     
    # 2. Use row-column dot products to compute each entry.
    # 3. Return the completed result matrix.
    pass


def identity_matrix(n):
    """Return the n by n identity matrix."""
    # Level 2:
    # 1. Reject invalid sizes.
    if n < 1:
        raise ValueError("n must be a positive integer")
    result = []
    for row in range(n):
        new_row=[]
        for col in range(n):
            if row == col:
                new_row.append(1)
            else:
                new_row.append(0)
    
        result.append(new_row)

    return result
    # 2. Put 1 on the main diagonal and 0 elsewhere.
    pass


def matrix_vector_product(A, x):
    """Return A times vector x."""
    # Level 3:
    
    # 1. Validate A and check that len(x) matches the number of columns of A.
    validate_matrix(A)
    if not len(x) == len(A[0]):
        raise ValueError("x must matches number of column of A")
    result = []
    # 2. For each row, compute the dot product of that row with x.
    for row in range(len(A)):
        total = 0
        for col in range(len(A[0])):
            total += A[row][col] * x[col]
        result.append(total)

    return result
    # 3. Return the output vector.
    pass


def is_homogeneous(b):
    """Return True when b is the zero vector."""
    # Level 3:
    for val in b:
        if val !=0:
            return False
    
    return True
    # Return True only when every entry of b is 0.
  


def is_solution(A, x, b, tolerance=1e-9):
    """Return True when x solves A x = b."""
    # Level 3:
    
  
    # x must match number of columns in A
    if not isinstance(x, list) or len(x) != len(A[0]):
        return False

    # b must match number of rows in A  <-- this check was missing
    if not isinstance(b, list) or len(b) != len(A):
        return False

    try:
        left_side = matrix_vector_product(A, x)
    except Exception:
        return False

    if len(left_side) != len(b):
        return False

    for i in range(len(b)):
        if abs(left_side[i] - b[i]) > tolerance:
            return False

    return True


def main():
    print("Level 1")
    A = [
        [1, -2],
        [3, 0],
    ]
    B = [
        [4, 5],
        [-1, 2],
    ]
    print("Sum:", add_matrices(A, B))
    print("Scaled:", scalar_multiply(-2, A))

    print()
    print("Level 2")
    C = [
        [2, -1],
        [0, 4],
    ]
    D = [
        [5, 1, 2],
        [-1, 0, 3],
    ]
    print("Can multiply:", can_multiply(C, D))
    print("Product:", matrix_multiply(C, D))
    print("Identity:", identity_matrix(2))

    print()
    print("Level 3")
    system_A = [
        [2, -5],
        [-3, 8],
        [7, 4],
    ]
    x = [1, -2]
    b = [12, -19, -1]
    print("A times x:", matrix_vector_product(system_A, x))
    print("Is solution:", is_solution(system_A, x, b))
    print("Homogeneous:", is_homogeneous([0, 0, 0]))


if __name__ == "__main__":
    main()

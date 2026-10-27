"""Module 3 zyLab starter: row operations and Gauss-Jordan elimination."""


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


def swap_rows(matrix, row_a, row_b):
    """Return a copy of matrix with two rows switched."""
    validate_matrix(matrix)
    result = copy_matrix(matrix)
    result[row_a], result[row_b] = result[row_b], result[row_a]
    return result


def scale_row(matrix, row_index, scale):
    """Return a copy of matrix after cR_i -> R_i."""
    validate_matrix(matrix)
    if scale == 0:
        raise ValueError("row scaling factor must be nonzero")

    result = copy_matrix(matrix)
    for col in range(len(result[row_index])):
        # Level 1: Find and fix the arithmetic error on this line.
        result[row_index][col] *= scale  
    return result


def replace_row(matrix, source_row, target_row, scale):
    """Return a copy of matrix after cR_source + R_target -> R_target."""
    validate_matrix(matrix)
    result = copy_matrix(matrix)
    for col in range(len(result[target_row])):
        # Level 1: Find and fix the arithmetic error on this line.
        result[target_row][col] += scale * result[source_row][col]
    return result


def leading_entry_index(row):
    """Return the index of the first nonzero entry, or None for a zero row."""
    for index in range(len(row)):
        if row[index] != 0:
            return index
    return None


def is_echelon_form(matrix):
    """Return True when matrix is in echelon form."""
    # Level 2:
    prev_pivot_col = -1
    zero_row = False

    for row in matrix:
        idx = leading_entry_index(row)
        if idx is None:
            zero_row = True
        else:
            if zero_row:
                return False
            if idx <= prev_pivot_col:
                return False
            prev_pivot_col = idx
    return True

    #for index in range(len(row))
    # 1. Track the previous leading-entry column.
    # 2. Once a zero row appears, all later rows must also be zero.
    # 3. Each nonzero row's leading entry must be to the right of the one above.
    pass


def pivot_columns(matrix):
    """Return a list of zero-based pivot-column indices."""
    # Level 2:
    # 1. For each nonzero row, find the leading-entry index.
    # 2. Append that index to a list.
    # 3. Return the list.
    result = []
    for row in matrix:
        idx = leading_entry_index(row)
        if idx is not None:
            result.append(idx)
    return result
    pass


def basic_and_free_variables(echelon, num_variables):
    """Return (basic_variables, free_variables) using variable names x1, x2, ..."""
    # Level 2:
    # 1. Find pivot columns using only the first num_variables columns.
    # 2. Columns with pivots are basic variables.
    # 3. Columns without pivots are free variables.
    # 4. Return two lists of names, such as ["x1", "x3"] and ["x2"].
    pivot_cols = set()
    for row in echelon:
        idx = leading_entry_index(row[:num_variables])
        if idx is not None:
            pivot_cols.add(idx)
        
    basic = []
    free = []

    for col in range(num_variables):
        name = f"x{col + 1}"
        if col in pivot_cols:
            basic.append(name)
        else:
            free.append(name)

    return basic, free
    pass


def find_pivot_row(matrix, start_row, pivot_col):
    """Return the first row at or below start_row with a nonzero pivot entry."""
    validate_matrix(matrix)
    for row in range(start_row, len(matrix)):
        if matrix[row][pivot_col] !=0:
        # Level 3: Replace False with the condition that finds a nonzero pivot.
            return row
    return None


def normalize_pivot_row(matrix, pivot_row, pivot_col):
    """Return a copy with the pivot row scaled so the pivot becomes 1."""
    validate_matrix(matrix)
    result = [[float(value) for value in row] for row in matrix]
    pivot = result[pivot_row][pivot_col]
    if pivot == 0:
        raise ValueError("pivot cannot be zero")

    for col in range(len(result[pivot_row])):
        # Level 3: Divide each entry in the pivot row by the pivot value.

        result[pivot_row][col] = result[pivot_row][col] / pivot

    return result


def eliminate_column(matrix, pivot_row, pivot_col):
    """Return a copy with zeros above and below the pivot in pivot_col."""
    validate_matrix(matrix)
    result = [[float(value) for value in row] for row in matrix]
    col_count = len(result[0])

    for row in range(len(result)):
        if row != pivot_row and result[row][pivot_col] != 0:
            factor = -result[row][pivot_col]
            for col in range(col_count):
                # Level 3: Add factor times the pivot row to the current row.
                result[row][col] = result[row][col] + factor* result[pivot_row][col]

    return result


def gauss_jordan_elimination(augmented):
    """Return a reduced-echelon-form copy of an augmented matrix."""
    # Level 3:
    # Most of the structure is provided. Complete the helper functions above.
    # 1. Work left to right through coefficient columns.
    # 2. Find a nonzero pivot at or below the current row.
    # 3. Swap that pivot row into position when needed.
    # 4. Scale the pivot row so the pivot is 1.
    # 5. Create zeros above and below that pivot.
    validate_matrix(augmented)
    matrix = [[float(value) for value in row] for row in augmented]
    row_count = len(matrix)
    col_count = len(matrix[0])
    pivot_row = 0

    for pivot_col in range(col_count - 1):
        candidate = find_pivot_row(matrix, pivot_row, pivot_col)
        if candidate is None:
            continue

        if candidate != pivot_row:
            matrix = swap_rows(matrix, pivot_row, candidate)

        matrix = normalize_pivot_row(matrix, pivot_row, pivot_col)
        matrix = eliminate_column(matrix, pivot_row, pivot_col)

        pivot_row += 1
        if pivot_row == row_count:
            break

    if pivot_row < col_count - 1:
        raise ValueError("system does not have a unique solution")

    return matrix


def solve_system(augmented):
    """Solve a unique-solution system using Gauss-Jordan elimination."""
    # Level 3:
    # 1. Call gauss_jordan_elimination.
    # 2. In RREF, the solution is in the last column.
    # 3. Return the solution.
    rref = gauss_jordan_elimination(augmented)
    solution = []

    for row in range(len(rref[0]) - 1):
        # Level 3: Append the right-hand-side value from this row.
        solution.append(rref[row][-1])

    return solution


def main():
    print("Level 1")
    A = [
        [1, 3, -6],
        [-2, 5, 4],
    ]
    print("Scaled row:", scale_row(A, 0, 3))
    print("Replaced row:", replace_row(A, 0, 1, 1))

    print()
    print("Level 2")
    echelon = [
        [3, -2, 6, 0, 1],
        [0, 0, 2, 7, 5],
        [0, 0, 0, -3, 5],
        [0, 0, 0, 0, 0],
    ]
    print("Is echelon:", is_echelon_form(echelon))
    print("Pivot columns:", pivot_columns(echelon))
    rref = [
        [1, 3, 0, -3, 0, 4],
        [0, 0, 1, -2, 0, 2],
        [0, 0, 0, 0, 1, -3],
    ]
    print("Basic/free:", basic_and_free_variables(rref, 5))

    print()
    print("Level 3")
    system = [
        [1, -2, 2, 7],
        [-2, 5, -5, -20],
        [-1, 2, -1, -3],
    ]
    print("Solution:", solve_system(system))


if __name__ == "__main__":
    main()

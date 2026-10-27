"""Module 2 zyLab starter: products, projections, and point-plane distance."""
import math

def same_dimension(u, v):
    """Return True when u and v have the same number of components."""
    return len(u) == len(v)


def dot_product(u, v):
    """Return the dot product of u and v."""
    if not same_dimension(u, v):
        raise ValueError("vectors must have the same dimension")

    total = 0
    for i in range(len(u)):
        # Level 1: Find and fix the arithmetic error on this line.
        total += u[i] * v[i]
    return total


def cross_product(u, v):
    """Return u x v for vectors in R^3."""
    if len(u) != 3 or len(v) != 3:
        raise ValueError("cross product requires two vectors in R^3")

    first = u[1] * v[2] - u[2] * v[1]
    # Level 1: Find and fix the arithmetic error on this line.
    second = u[2] * v[0] - u[0] * v[2]
    third = u[0] * v[1] - u[1] * v[0]
    return [first, second, third]


def vector_projection(u, v):
    """Return the projection of u onto nonzero v."""
   



    # Level 2:
    # 1. Confirm that u and v have the same dimension.
    if not same_dimension(u, v):
        raise ValueError("vectors must have the same dimension")
    # 2. Compute v dot v and reject the zero vector.
    denominator = dot_product(v, v)
    if denominator == 0:
        raise ValueError
    # 3. Compute the scale factor (u dot v) / (v dot v).
    scale = dot_product(u, v) / denominator
    # 4. Use a loop to multiply each component of v by the scale factor.
    total = []
    for i in range(len(v)):
        total.append(v[i] * scale)
   
    # 5. Return the projected vector as a list.
    return total
    pass


def point_to_plane_distance(point, plane):
    """Return the distance from a point in R^3 to Ax + By + Cz + D = 0."""
    # Level 3:
    # 1. Confirm that point has 3 values and plane has 4 coefficients.
    if len(point) !=3:
        raise ValueError("point must have 3 coordinates")
    if len(plane) !=4:
        raise ValueError("plane must have 4 coefficients")
    A, B, C, D = plane
    # 2. Form the normal vector [A, B, C].
    normal = [A, B, C]
    denominator_squared = dot_product(normal, normal)

    
    # 3. Compute A*x + B*y + C*z with dot_product, then add D.
    numerator = abs(dot_product(normal, point) + D) 

    # 4. Reject a plane whose normal vector is the zero vector.
    if denominator_squared == 0:
        raise ValueError("normal vector cannot be the zero vector")
    # 5. Return |A*x + B*y + C*z + D| / sqrt(A^2 + B^2 + C^2).
    return numerator / math.sqrt(denominator_squared)
    pass


def main():
    print("Level 1")
    u = [4, 0, 1]
    v = [-2, 8, 13]
    print("Dot product:", dot_product(u, v))
    print("Cross product:", cross_product(u, v))

    print()
    print("Level 2")
    projection = vector_projection([4, -2], [6, 2])
    print("Projection:", projection)

    print()
    print("Level 3")
    point = [0, 0, 0]
    plane = [3, -4, 1, 3]
    distance = point_to_plane_distance(point, plane)
    if distance is not None:
        distance = round(distance, 4)
    print("Distance:", distance)


if __name__ == "__main__":
    main()

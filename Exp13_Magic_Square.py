def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("This method only works for odd-order magic squares.")

    # Step 3: Create an n x n array filled with 0
    magic_square = [[0] * n for _ in range(n)]

    # Step 4.1: Place the number 1 in the middle of the first row
    number = 1
    i, j = 0, n // 2

    while number <= n**2:
        magic_square[i][j] = number
        number += 1

        # Step 4.2: Calculate new position
        new_i, new_j = (i - 1) % n, (j + 1) % n

        # Step 4.2.2: If not possible, follow these steps
        if magic_square[new_i][new_j] != 0:  # Cell already occupied
            new_i, new_j = (i + 1) % n, j  # Step 4.2.2.3 and 4.2.2.4

        # Update position
        i, j = new_i, new_j

    return magic_square

def print_magic_square(square):
    n = len(square)
    for row in square:
        print(" ".join(f"{num:2d}" for num in row))

# Step 2: Read the order of the matrix from the user
n = int(input("Enter the order of the magic square (must be odd): "))

if n % 2 == 1:
    magic_square = generate_magic_square(n)
    print("Magic Square:")
    print_magic_square(magic_square)
else:
    print("Error: Only odd order magic squares are supported in this implementation.")


def generate_magic_square(n):
    if n % 2 == 0:
        print("Only odd numbers allowed for this method.")
        return
    
    magic_square = [[0]*n for _ in range(n)]
    
    num = 1
    i, j = 0, n // 2  # Start from middle of first row
    
    while num <= n**2:
        magic_square[i][j] = num
        num += 1
        new_i, new_j = (i-1) % n, (j+1) % n
        
        if magic_square[new_i][new_j]:
            i = (i+1) % n
        else:
            i, j = new_i, new_j

    # Display neatly
    print(f"\nMagic Square of size {n}x{n}:\n")
    for row in magic_square:
        print("  ".join(f"{val:2d}" for val in row))
    
    magic_constant = n * (n**2 + 1) // 2
    print(f"\nMagic Constant: {magic_constant}")

# 👇 Take input from user
try:
    user_n = int(input("Enter an odd number (n) for magic square size: "))
    generate_magic_square(user_n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
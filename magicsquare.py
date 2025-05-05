import random
 
def generate_magic_square(n):
    """
    Generate an N x N magic square (N must be odd).
    Returns the magic square if successful, None otherwise.
    """
    if n % 2 == 0:
        return None
 
    # Initialize the N x N grid with 0
    magic_square = [[0 for _ in range(n)] for _ in range(n)]
 
    # Randomize starting position
    row = random.randint(0, n-1)
    col = random.randint(0, n-1)
 
    for num in range(1, n * n + 1):
        magic_square[row][col] = num  # Place the current number
 
        # Calculate the next position
        next_row = (row - 1) % n  
        next_col = (col + 1) % n  
 
        if magic_square[next_row][next_col] != 0:
            next_row = (row + 1) % n  
            next_col = col  
        # Update position
        row, col = next_row, next_col
 
    return magic_square
 
def print_magic_square(square):
    """Print the magic square in a formatted way"""
    for row in square:
        print(" ".join(f"{cell:2}" for cell in row))
 
def main():
    while True:
        try:
            # Get user input
            n = input("Enter an odd size for the Magic Square (N) or 'q' to quit: ")
           
            # Check if user wants to quit
            if n.lower() == 'q':
                print("Goodbye!")
                break
           
            # Convert input to integer
            n = int(n)
           
            # Validate input
            if n < 1:
                print("Please enter a positive number.")
                continue
           
            if n % 2 == 0:
                print("Please enter an odd number.")
                continue
           
            # Generate and print the magic square
            magic_square = generate_magic_square(n)
            if magic_square:
                print(f"\nMagic Square for N={n}:")
                print_magic_square(magic_square)
            else:
                print("Failed to generate magic square.")
               
        except ValueError:
            print("Please enter a valid number.")
 
if __name__ == "__main__":
    main()

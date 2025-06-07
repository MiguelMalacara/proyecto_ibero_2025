import numpy as np

def solve_linear_system():
    # Define the coefficients of the linear equations
    A = np.array([[3, 2], [1, 2]])
    
    # Define the constants on the right-hand side
    B = np.array([5, 4])
    
    # Solve the linear system
    solution = np.linalg.solve(A, B)
    
    print("Solution to the linear system:")
    print(solution)
import numpy as np

print("================================")
print("     MATRIX OPERATIONS TOOL")
print("================================")

# Taking Matrix A input
rows = int(input("Enter number of rows for Matrix A: "))
cols = int(input("Enter number of columns for Matrix A: "))

print("Enter Matrix A elements:")
A = []

for i in range(rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

A = np.array(A)

# Taking Matrix B input
print("\nEnter Matrix B elements:")
B = []

for i in range(rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    B.append(row)

B = np.array(B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Menu
while True:
    print("\n========== MENU ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose of Matrix A")
    print("5. Determinant of Matrix A")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAddition:")
        print(A + B)

    elif choice == "2":
        print("\nSubtraction:")
        print(A - B)

    elif choice == "3":
        if A.shape[1] == B.shape[0]:
            print("\nMultiplication:")
            print(A @ B)
        else:
            print("Matrix multiplication is not possible.")

    elif choice == "4":
        print("\nTranspose of Matrix A:")
        print(A.T)

    elif choice == "5":
        if A.shape[0] == A.shape[1]:
            print("\nDeterminant of Matrix A:")
            print(np.linalg.det(A))
        else:
            print("Determinant is possible only for a square matrix.")

    elif choice == "6":
        print("\nThank you for using Matrix Operations Tool!")
        break

    else:
        print("Invalid choice. Please try again.")

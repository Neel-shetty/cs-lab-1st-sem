def lower_triangular(matrix):
  n = len(matrix)
  for i in range(n):
    for j in range(n):
      if i > j:
        print("0", end=" ")
      else:
        print(matrix[i][j], end=" ")
    print()

def upper_triangular(matrix):
  n = len(matrix)
  for i in range(n):
    for j in range(n):
      if i < j:
        print("0", end=" ")
      else:
        print(matrix[i][j], end=" ")
    print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Lower triangular matrix:")
lower_triangular(matrix)
print("Upper triangular matrix:")
upper_triangular(matrix)


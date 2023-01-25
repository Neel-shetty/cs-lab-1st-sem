#print upper and lower triangle on a matrix array
# res = []
# for i in range(0, 10):
#   for j in range(0, i):
#     print("*", end='',)
#   print('\r')

# for i in range(5):
#   res.append("*"*i)
# print("\n".join(res))

def lower(matrix, row_col):
	for i in range(0, row_col): #0, 1, 2
		for j in range(0, row_col): #{0, 1, 2}, {0,1,2},{0,1,2}
			if (i < j):	  
				print("0", end = " ");  
			else:
				print(matrix[i][j],  #prints 1, 
					end = " " ); 
		print(" ");

def upper(matrix, row_col):
	for i in range(0, row_col):
		for j in range(0, row_col):
			if (i > j):
				print("0", end = " ");
			else:
				print(matrix[i][j],
					end = " " );
		print(" ");

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]];
row_col = int(input('enter the number of rows - '));


print('lower matrix')
lower(matrix, row_col);

print('upper matrix')
upper(matrix, row_col);

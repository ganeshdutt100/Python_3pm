# nums  = [1,2,3]
# for i in  nums:
#     for j in nums:
#         print(f"{i} , {j}")

A = [[1,2],[3,4]]        
B = [[1,2],[3,4]]        
for i in range(2):
    for j in range(2):
        print(A[i][j] +  B[i][j] , end="")        
    print()    
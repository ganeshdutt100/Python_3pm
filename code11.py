# nums  = [1,2,3]
# for i in  nums:
#     for j in nums:
#         print(f"{i} , {j}")

# A = [[1,2],[3,4]]        
# B = [[1,2],[3,4]]        
# for i in range(2):
#     for j in range(2):
#         print(A[i][j] +  B[i][j] , end="")        
#     print()    

# 10 
# n = 5
# for i in range(n):
#     print(" "*(n-i-1) +  "*" *(2*i+1))
# for  i in range(n-2, -1, -1):
#     print(" "*(n-i-1)+"*"*(2*i+1))    

# i = 0  (5-0-1) = 4  +  2*0+1 =  1*x = x
# i = 1  (5-1-1) = 3  +  2*1+1 =  3x* = ***
# i = 2  (5-2-1) = 2  +  2*2+1 =  5x* = *****
# i = 3  (5-3-1) = 1  +  2*3+1 =  7x* = *******
# i = 3  (5-3-1) = 1  +  2*3+1 =  7x* = *******
# i = 2  (5-2-1) = 2  +  2*2+1 =  5x* = *****
# i = 1  (5-1-1) = 3  +  2*1+1 =  3x* = ***
# i = 0  (5-0-1) = 4  +  2*0+1 =  1*x = x

# s  = "  hello  "
# print(s.strip())

# sentence  =  "i,love,python,coding"
# word  =   sentence.split(",")
# print(len(word)) 


# a =  "aman manmhan"
# print(a.title())

# a =  "I like apples"
# print(a.replace("apple","banana"))

# a =  "banana"
# print(a.count("a"))

# a = "silent"
# b = "listenp"
# if sorted(a) ==  sorted(b):
#   print("Anagrams")

password = "Ganesh123"
if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit()  for  char in password ):
    print("Valid password")
else:
    print("Invalid password")    

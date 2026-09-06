#lab-5.py

#project 1:
# x =int(input("enter x:"))
# y = int(input("enter y:"))
# n = int(input("enter n:"))
# for i in range(x+1,y+1):
#     if i % n == 0:
#         print(i)
  
# #project 2:
# num = int(input("enter a integer:"))
# total_sum = 0

# temp =num
# while temp > 0:
#     total_sum  += temp % 10
#     temp //= 10
    
# print("sum of digits:", total_sum)    

    
#project 3:
# n =int(input("enter N :"))
# if n == 0:
#     print("N cannot be zero")
#     while num> 0:
#         digit = num% 10
#         sum = sum +digit
#         num = num// 10
# else:
#     divisible = 0
#     not_divisible = 0
    
#     while True:
#         if num % n == 0:
#             divisible = divisible +1
#         else :
#             not_divisible = not_divisible + 1
#     print("count divisible by N =",divisible)
#     print("count not_divisible by N =",not_divisible)    
    
    
#project 4:
# n = int(input("enter a integer:"))
# if n < 0:
#     print("invalid")
# else:
#      factorial = 1
#      i =1
    
#      while i <= n:
#              factorial = factorial * i
#              i =i + 1
#      print("factorial=",factorial)



#project 5:
# num  = int(input("enter a integer:"))
# if num < 0:
#     print("invalid")
# else:
#     orignal = num 
#     reverse = 0

#     while num > 0:
#         digit = num % 10
#         reverse = reverse * 10 + digit
#         num = num //  10

#     if orignal == reverse :
#         print("palindrome")
#     else:
#         print("not palindrome")           
    
    
# #project 6:
# n = int(input("enter N:"))

# if n <= 0:
#     print("invalid")
# else:
#     a =1
#     b =1

#     print(" Fibonacci sequence")

#     for i in range(n):
#         print(a,end ="  ")
#         c =a+b 
#         a = b
#         b = c


# #project 7:
# n = int(input("enter an integer :"))

# if n<= 1:
#     print("not prime")
# else:
#     prime = True
#     i = 2

#     while i*i <= n:
#         if n % i ==0:
#             prime = False
#             break
#         i = i+1
#     if prime:
#         print("prime")
#     else:
#         print("not prime")



# #project 8:
# sentence =input("enter a sentence :")

# capital = 0
# small = 0
# digit =0
# special = 0

# i = 0

# while i < len(sentence):

#     ch =sentence[ i]

#     if 'A'<= ch <= 'Z':
#         capital = capital + 1
#     elif 'a' <= ch <= 'z':
#         small = small + 1
#     elif '0'<= ch <= '9':
#         digit = digit +1
#     else:
#         special = special + 1

#     i = i +1

# print("Capital letters =", capital)
# print("Small letters =",small) 
# print("digits =",digit)
# print("special characters =",special)   

         
    
        
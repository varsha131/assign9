Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[]
num=int(input("how many numbers:"))
for n in range(num):
    numbers=int(input("enter number"))
    list.append(numbers)
print("maximum element in the list is:",max(list))
print("maximun element in the list is:",min(list))
how many numbers:6
enter number5
enter number4
enter number3
enter number6
enter number7
enter number1
maximum element in the list is: 7
maximun element in the list is: 1
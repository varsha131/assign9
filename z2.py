Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def enquiry(list1):
    if len(list1)==0:
        return 0
    else:
        return 1
list1=[]
if enquiry(list1):
    print("the list is not empty")
else:
    print("empty list")

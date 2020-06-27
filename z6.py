Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[1,3,5,7,9]
list2=[1,2,4,6,7,8]
diff_list1_list2=list(set(list1)-set(list2))
diff_list2_list1=list(set(list2)-set(list1))
total_diff=diff_list1_list2+diff_list2_list1
print(total_diff)
[9, 3, 5, 8, 2, 4, 6]
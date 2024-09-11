# word = input("Enter String ")  
# for i in word:
#     if not i.isalnum():
#         print(f"{word} is not  Alphanumeric")
#         break
# else:
#     print(f"{word} is  Alphanumeric")
       




s = input("enter string")
flag=True
for i in range (len(s)):

    p=ord(s[i])


    if((p>=65 and p<=90) or (p>=97 and p<=122) or (p>=48 and p<=57)):
        continue

    else:

        flag=False
        break

if flag==True:
 print("True")

else:
  print("False")
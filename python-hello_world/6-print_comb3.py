for i in range (10):
  for j in range(i+1,10):
    if(i !=j or str(i)+ str(j) !=str(j)+str(i)):
     if(str(i)+ str(j) != '89' ):
       print("{}, ".format(str(i)+ str(j)),end="")
# print("{}, ".format(79),end="")
print(89)  
for i in range (10):
  for j in range(i+1,9):
    if(i !=j or str(i)+ str(j) !=str(j)+str(i)):
     print("{}, ".format(str(i)+ str(j)),end="")
print("{}, ".format(79),end="")
print(89)  
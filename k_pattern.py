#  #
# # 
##  
# # 
#  #
for i in range (5):
    for j in range(5):
        if(j==0):
            print("#",end="")
        elif(i+j==2 or (i==3 and j==1) or (i==4 and j==2)):
            print("#",end="")
        else:
            print(" ",end="")
    print()
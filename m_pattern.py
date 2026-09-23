#   #
## ##
# # #
#   #
#   #
for i in range (5):
    for j in range(5):
        if(j==0 or j==4):
            print("#",end="")
        elif((i==j and i+j<=4) or (j>=i and i+j==4 )):
            print("#",end="")
        else:
            print(" ",end="")
    print()
# #####
# ####
# ###
# ##
# #
#     *
#    **
#   ***
#  ****
# *****
for i in range(5,0,-1):

    for j in range(6):

        if(j<i):

            print("#",end="")

    print()

for i in range(5,0,-1):

    for j in range(6):

        if(j>=i):

            print("*",end="")

        else:

            print(" ",end="")

    print()
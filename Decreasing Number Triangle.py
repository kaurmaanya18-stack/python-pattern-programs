#     1 2 3 4 5
#       2 3 4 5
#         3 4 5
#           4 5
#             5
for i in range(1,6):
    for j in range(1,6):
        if(j>=i):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
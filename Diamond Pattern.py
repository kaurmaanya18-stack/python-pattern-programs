    #    
   ###   
  #####  
 ####### 
#########
 ####### 
  #####  
   ###   
    #    
for i in range (1,5):
    for j in range(1,10):
        if(j==5):
            print("#",end="")
        elif(j<5):
            if((i+j)>=6):
                print("#",end="")
            else:
                print(" ",end="")
        elif(j>5):
            if((j-i)<=4):
                print("#",end="")
            else:
                print(" ",end="")
        else:
            print(" ",end="")
    print()
for i in range (1,6):
    for j in range(1,10):
        if(j==5):
            print("#",end="")
        elif(j<5):
            if(j>=i):
                print("#",end="")
            else:
                print(" ",end="")
        elif(j>5):
            k=j-5
            if((k+i)<=5):
                print("#",end="")
            else:
                print(" ",end="")
        else:
            print(" ",end="")
    print()
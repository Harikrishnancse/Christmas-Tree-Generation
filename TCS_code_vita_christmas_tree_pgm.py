'''
enter the no of days:5
     *     
    ***    
   *****   
  *******       ==== part 1
 ********* 
***********
    ***    
   *****   
  *******       ==== part 2
 ********* 
    ***    
   *****        ==== part 3
  *******  
    ***        ====== part 4
   *****        
     *         =====  stand
     *  


'''


N = int(input('enter the no of days:'))
if N==1:
    print('Tree not grown....')
elif N>20:
    print('Tree doesnt exist..')
else:
    #part 1
    for i in range(0,N+1):
        for j in range(0,(2*N)+1):
            if (N-i <= j <= N+i):
                print('*',end='')
            else:
                print(' ',end='')
        print()
    #part 2 to N-1
    if N>2:
        no_of_rows=N
        for part in range(2,N):
            for i in range(1,no_of_rows):
                for j in range(0,(2*N)+1):
                    if (N-i <= j <= N+i):
                        print('*',end='')
                    else:
                        print(' ',end='')
                print()
            no_of_rows-=1
    #stand
    for i in range(0,2):
        for j in range(0,(2*N)+1):
            if (j==N):
                print('*',end='')
            else:
                print(' ',end='')
        print()

    

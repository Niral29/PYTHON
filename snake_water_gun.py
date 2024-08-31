import random
# Snake=-1 , Water=0 , Gun=1

while(True):
     i=int(input("Attempt chance :  "))
     j=random.randrange(-1,0,1)
     if(i==-1 and j==0 or i==0 and j==1 or i==1 and j==-1):
        print("You win!!")
     elif(i==j):
      print("Match draw ")
     else:
        print("Computer Wins..")
        print(f"computer choice is {j} ")
      
    
                   
    


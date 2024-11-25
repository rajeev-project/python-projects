import random
a=[[0,0,0],
   [0,0,0],
   [0,0,0]]
def win(a,b):
    n = len(a)

    for i in a:
        if all(j == b for j in i):
            return True

  
    for j in range(n):
        if all(a[i][j] == b for i in range(n)):
            return True

    if all(a[i][i] == b for i in range(n)):
        return True

    if all(a[i][n - 1 - i] == b for i in range(n)):
        return True

    return False
     
n=1
count=0
print("computer choose X or O")
comp=random.choice(["X","O"])
X_O=comp
print(f"the computer choose {comp}")
print("\n")
user_choice=input("enter X or O")
print(f"user choose :{user_choice}")
print("\n")
row=len(a)
col=len(a[0])
while n==1:
    print("computer's turn")
    def ran():
      while True:
       rand_row = random.randint(0, len(a) - 1)
       rand_col = random.randint(0, len(a[0]) - 1)
       if a[rand_row][rand_col]==0:
                a[rand_row][rand_col]=X_O 
                return a   
    b=ran()
    print(b)
    count+=1
    g=win(b,X_O)
    if g==True:
        print("computer wins")
        exit()
    if count==9:
        print("match is a draw")

    else:
        pass
    print("\n")
    print("users turn:")
    def use():
      c=int(input("choose row"))
      d=int(input("choose column"))
      if a[c][d]==0:
        a[c][d]=user_choice
        return a
      else:
        print("row and column invalid")
        use()
    c=use()
    print(c)
    count+=1
    k=win(c,user_choice)
    if k==True:
        print("user wins")
        exit()
    

   





  
    
    






    
import random
print("user")
n=1
def die(name):
     print(f"{name}'s turn")
     d=random.randint(1,6)
     return d
"""while n==1:
    c=input("roll the die")
    d=die()
    if d==6 or d==1:
          print("you can start the game",d)
          n=0
    else:
          print("try again",d)
print("user")  
        
ladder={2:23,8:12,17:93,29:54,32:51,39:80,62:78,70:89,75:96}
snake={99:4,31:14,41:20,67:50,59:37,82:61,92:76}
count=0
while count<100:
    d=die()
    print("\n")
    print(f"value of die {d}")
    count+=d
    print(f"you reached {count}")
    for i in snake:
         if count==i:
            count=snake[i]
            print(f"snake dropped you from {i} to {snake[i]}")
            print(count)
         else:
              continue
    for keys in ladder:
         if count==keys:
              count=ladder[keys]
              print(f"you climbed ladder from {keys} to {ladder[keys]}")
              print(count)
         else:
              continue
    if count>100:
         count=count-d
         print("not possible try again")
         continue
    if count==100:
         print("you have won")"""
   
n=1
while n==1:
    c=input("roll the die")
    d=die()
    if d==6 or d==1:
          print("you can start the game",d)
          n=0
    else:
          print("try again",d)
     
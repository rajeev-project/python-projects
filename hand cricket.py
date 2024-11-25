import random
flag=0
def oddeven():
    a=["odd","even"]
    b=random.choice(a)
    return b
def computer_turn():
    a=random.randint(1,6)
    return a
def bat_ball():
    a=random.choice(["bat","balling"])
    return(a)  
def win(sumu,sumc):
   if sumu>sumc:
       print(f"user wins by {sumu-sumc} runs")
   else:
       print(f"computer wins by {sumc-sumu} runs")
print("user : odd or even ?")
d=oddeven()
print(f"the computers choice is : {d}")
print("\n")
a=int(input("user enter a no: "))
b=computer_turn()
print(f"the computers choice is: {b}")
c=a+b
if d=="odd":
    if c%2==0:
        print(f"{c} is even")
        print("user choose batting or bowling")
        start=input("user chooses:  ")
        flag=1
    else:
        print(f"{c} is odd")
        print("computer choose batting or bowling")
        start=bat_ball()
if d=="even":
    if c%2==0:
        print(f"{c} is even")
        print("computer choose batting or bowling")
        start=bat_ball()
    else:
        print(f"{c} is odd")
        print("user choose batting or bowling")
        start=input("user chooses:  ")
        flag=1
print("\n")
sumc=0
sumu=0
count=0
n=1
while count != 2:
 if start=="balling" and flag==1:
    print("computer is batting")
    while n!=0:
     a=int(input("user enter a no:"))
     b=computer_turn()
     print(f"the computer used : {b} ")
     if a==b:
        print(" computer is out!!!")
        count+=1
        print("\n")
        break
     else:
      sumc+=b
     print(f"the current score of computer is {sumc}")
    print(f"the total score of computer is {sumc}")
    while n!=0:
       print("user is batting")
       a=int(input("user enter a no:"))
       b=computer_turn()
       print(f"the computer used : {b} ")
       if a==b:
        print(" user is out!!!")
        print("\n")
        count+=1
        break
       else:
        sumu+=a
        if sumu>sumc:
           print("user wins")
           count+=1
           break
        print(f"the current score of user is {sumu}")  
    print(f"the total score of user is {sumu}")
    
 elif start=="batting" and flag==1:
    print("user is batting")
    while n!=0:
     a=int(input("user enter a no:"))
     b=computer_turn()
     print(f"the computer used : {b} ")
     if a==b:
        print(" user is out!!!")
        count+=1
        print("\n")
        break
     else:
      sumu+=a
     print(f"the current score of user is {sumu}")
    print(f"the total score of user is {sumu}")
    print("computer is batting") 
    while n!=0:
       a=int(input("user enter a no:"))
       b=computer_turn()
       print(f"the computer used : {b} ")
       if a==b:
        print(" computer is out!!!")
        count+=1
        print("\n")
        break
       else:
        sumc+=b
        if sumc>sumu:
            print("computer wins")
            count+=1
            break
       print(f"the current score of computer is {sumc}")
    print(f"the total score of computer is {sumc}")   
  
 elif start=="batting" and flag==0:
    print("computer is batting")
    while n!=0:
     a=int(input("user enter a no:"))
     b=computer_turn()
     print(f"the computer used : {b} ")
     if a==b:
        print(" computer is out!!!")
        count+=1
        print("\n")
        break
     else:
      sumc+=b
     print(f"the current score of computer is {sumc}")
    print(f"the total score of computer is {sumc}")
    print("user is batting") 
    while n!=0:
       a=int(input("user enter a no:"))
       b=computer_turn()
       print(f"the computer used : {b} ")
       if a==b:
        print(" user is out!!!")
        count+=1
        print("\n")
        break
       else:
        sumu+=a
        if sumu>sumc:
            print("user wins")
            count+=1
            break
       print(f"the current score of user is {sumu}")
    print(f"the total score of user is {sumu}")
   
 elif start=="balling" and flag==0:
    print("computer is balling")
    while n!=0:
     a=int(input("user enter a no:"))
     b=computer_turn()
     print(f"the computer used : {b} ")
     if a==b:
        print(" user is out!!!")
        count+=1
        print("\n")
        break
     else:
      sumu+=a
     print(f"the current score of user is {sumu}")
    print(f"the total score of user is {sumu}")
    print("computer is batting") 
    while n!=0:
       a=int(input("user enter a no:"))
       b=computer_turn()
       print(f"the computer used : {b} ")
       if a==b:
        print(" computer is out!!!")
        count+=1
        print("\n")
        break
       else:
        sumc+=b
        if sumc>sumu:
            print("computer wins")
            count+=1
            break
       print(f"the current score of computer is {sumc}")
    print(f"the total score of computer is {sumc}")
    print("\n")
if sumu>sumc:
       print(f"user wins by {sumu-sumc} runs")
else:
       print(f"computer wins by {sumc-sumu} runs")
       




        


        








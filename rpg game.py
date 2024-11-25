import time
import random
name=input("enter a name: ")
villain_welcome = ["So we meet again!", "Ha ha ha!", "welcome ", "winter is coming" ]
villain_dialogue = ["I've been waiting for this moment.","You won't escape this time.","Prepare to meet your doom!", "I underestimated you before, but not this time!"]
hero_responses = ["I won't let you get away with this!","Your reign of terror ends here!","I'm not afraid of you!","This time, it's your turn to fall."]
villain_retorts = ["Foolish words for someone who stands no chance!","Brave, but foolish!","You can't stop what's coming!","I'll crush you like I did last time!"]
a=random.choice(villain_welcome)
b=random.choice(villain_dialogue)
c=random.choice(hero_responses)
d=random.choice(villain_retorts)
time.sleep(2)
print(f"\nramsey:{a}" +" "+ name)
time.sleep(2)
print(f"\nramsey:{b}")
time.sleep(2)
print(f"\nsnow:{c}")
time.sleep(2)
print(f"\nramsey:{d}")
time.sleep(2)
snow_xp=100
ram_xp=100
def snowattack(a,ram_xp):
        if a==1:
          ram_xp-=10
        elif a==2:
          ram_xp-=15
        elif a==3:
          ram_xp-=25
        else:
          ram_xp-=40
        print("ramsey damage : " ,ram_xp)
        return ram_xp
print("\n")
time.sleep(2)
print("let the battle begin!")
        
count=0
while ram_xp>=0 and snow_xp>=0:
    print("\n")
    ram_attack={"arrow":10,"stab":20,"hit":25,"power_stab":40}
    b=random.choice(list(ram_attack))
    c=ram_attack[b]
    print("ramsey attack :" ,b)
    snow_xp-=c
    print("snow damage : ",snow_xp)
    time.sleep(2)
    if snow_xp<=0:
       print(f"{name} has been defeated")
       break
    print("\n")
    print("attack options=arrow:1,stab:2,hit:3")
    if count>=1:
       print("****power stab : 4****")
    s_attack=int(input("choose attack :"))
    count=count+1
    if count<=1:
       if s_attack>=4:
          print("not available")
          continue
    ram_xp=snowattack(s_attack,ram_xp)
    time.sleep(1)
    
    
    if ram_xp<=0:
       print(f"{name} wins")
       break

      



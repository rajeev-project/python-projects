roman=input("enter an element")
romanlogic = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
sum=0
for i in range(len(roman)):
        if roman[i] in romanlogic:
                 value=romanlogic[roman[i]]
                 if i+1<len(roman) and romanlogic[roman[i+1]]>value :
                         sum-=value
                 else:
                         sum+=value 
        else:
             print("wrong elements")
             break
                                           
print(sum)

                

  





          

        
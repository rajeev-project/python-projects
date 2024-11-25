n=1
a="rajeevr"
c=[]
count=0
def hang():
    print(count)
    hangman_stages = {1:
    """
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,2:
    """
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,3:
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,4:
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,5:
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========
    """,6:
    """
       +---+
       |   |
       O   |
      /|\ |
      /    |
           |
     =========
    """,7:
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
     =========
    """
     }
    if count in hangman_stages:   
       return hangman_stages[count]
while n==1:
   b=input("enter letter")
   if b not in a:
      print(f"wrong guess ")
      count+=1
      print(hang())
   else:
      c.append(b)
      print("Correct guess")
   guess=0
   for char in a:
      if char in c:
         print(char, end=" ")
         guess+=1
      else:
         print("_", end=" ")
   print() 
   turn=len(a)-guess
   print(f" {turn} letter left")
    
   if guess==len(a):
        print("Congratulations! You've guessed the word!")
        break
    
   if count == 7:
        print("Game over! The word was:", a)
        break



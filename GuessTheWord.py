print("-------------------------------------------------------------------------")
print("                   WELCOME TO WORD GUESSING GAME")
print("-------------------------------------------------------------------------")
wordcollection=['Hello','name','dragon','class','tree','beautiful','object','anime','fish','tiger','lady','ant','man','world','ANIMAL','girl','deer']

name=input("Enter username:")
flag=0

while(flag==0):
    word=input("Enter your word that your guessing:")
    for i in wordcollection:
        if word.upper()==i.upper():
            print(f"{name} guessed the correct word!!! \n CONGRATULATIONS\nGame is ENDING....")
            flag=1
    if(flag==0):
        print("You guessed the wrong word!!!")
        
        
        



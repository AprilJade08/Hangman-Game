l=["examination", "education", "psychology","orientation", "supplementary", "contemporary"]
m=len(l)
import random
print ("HANGMAN")
print ()
print ()
rank=[]
while True:
    print ("1.Administrator")
    print ("2.New Game")
    print ("3.Quit")
    print ()
    y=int (input ("Enter your choice: "))
    print ()
    print ()
    if y==1:
        password="Hangman123"
        pword=input ("Enter Password: ")
        print ()
        print ()
        if pword==password:
            print ()
            print ()
            print ("List of Words: \n")
            print ("S.No. ", "Word")
            print()
            for i in range (m):
                print (i+1,"   ",l[i])
            print ()
            print ()
            while True:
                print ("1. Add a new word to the list")
                print ("2. Delete a word")
                print ("3. Return to the Game")
                print ()
                print ()
                ch=eval (input ("Enter Choice: "))

                if ch==1:
                    nword=input ("\nEnter New Word: ")
                    l.append(nword)
                    print ("\nThe updated list is:\n")
                    print ("S.No. ", "Word")
                    print()
                    nlist=len(l)
                    for i in range (nlist):
                        print (i+1,"   ",l[i])
                    print ()
                    continue
                elif ch==2:
                    sno=int (input("Enter S.No. of the word to be deleted: "))
                    l.pop(sno-1)
                    print ("The updated list is")
                    print ("S.No.   ", "Word")
                    nlist=len(l)
                    for i in range(nlist):
                        print (i+1,"   ",l[i])
                    print ()
                    print ()
                    continue
                elif ch==3:
                    break
                else:
                    print("Invalid Choice")
                    continue
                continue

        else:
            print ("Incorrect Password")
            print ()
            print ()
            continue
    elif y==2:
        x=random.choice(l)
        w=list(x)
        n=len (w)
        empty=[]
        for i in range (n):
            empty.append("_ ")
        user=input ("Username: ")
        print()
        print ("Your word has", n, "letters.")
        string=""

        for i in range(n):
            string+=empty[i]
        print(string)
        print()
        print()
        count=0
        msg=0
        score=7
        for i in range(n+7):
            a=input("Enter letter: ")
            if a in w:
                repeat=w.count(a)
                for p in range(repeat):
                    ind=w.index(a)
                    empty[ind]=a
                    w[ind]="0"
                    string=""
                    msg+=1
                for k in range (n):
                    string+=empty[k]
                print (string)
                if (n-msg)==0:
                    score+=10
                    print ("You've guessed the word!!!")
                    print ()
                    print ()
                    rank.append( [user, score])
                    length=len (rank)
                    for d in range (length):
                        for e in range (length-1-d):
                            if (rank[e][1])<(rank[e+1] [1]) :
                                rank[e], rank[e+1]=rank[e+1], rank[e]
                    left_aligned=""
                    center= "SCOREBOARD"
                    right_aligned = ""
                    print("{:<15}{:^10}{:>15}".format (left_aligned, center, right_aligned))
                    print ()
                    left_aligned = "RANK"
                    center = "PLAYER"
                    right_aligned = "SCORE"
                    print("{:<15} {:^10}{:>15}".format (left_aligned, center, right_aligned))
                    for f in range (1, length+1):
                        left_aligned = f
                        center=rank[f-1][0]
                        right_aligned = rank[f-1][1]
                        print("{:<15}{:^10}{:>15}".format (left_aligned, center, right_aligned))
                    print()
                    print()
                    print()
                    break
                else:
                    print("Well done!",n-msg, "more to go...")
                    print()
                    print()
            else:
                score-=1
                print ("Oh no!")
                count+=1

            if count==1:
                j='''
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|

'''
                print(j)

            elif count==2:
                j='''
   ____
  |    |
  |    o
  |    |
  |
  |
 _|_
|   |______
|          |
|__________|

'''
                print(j)

            elif count==3:
                j='''
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|

'''
                print(j)

            elif count==4:
                j='''
   ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|

'''
                print(j)

            elif count==5:
                j='''
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|

'''
                print(j)

            elif count==6:
                j='''
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / 
 _|_
|   |______
|          |
|__________|

'''
                print(j)

            elif count==7:
                j='''
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|

'''
                print(j)
                print('''
GAME OVER!

''')
                rank.append([user, score])
                length=len(rank)
                for d in range(length):
                    for e in range (length-1-d):
                        if rank[e][1]<rank[e+1][1]:
                            rank[e], rank[e+1]=rank[e+1], rank[e]
                left_aligned = ""
                center = "SCOREBOARD"
                right_aligned = ""
                print("{:<15}{:^10}{:>15}".format (left_aligned, center, right_aligned))
                print ()
                left_aligned = "RANK"
                center="PLAYER"
                right_aligned = "SCORE"
                print("{:<15} {:^10} {:>15}".format (left_aligned, center, right_aligned))
                for f in range (1, length+1):
                    left_aligned = f
                    center = rank[f-1][0]
                    right_aligned = rank[f-1][1]
                    print("{:<15} {:^10}{:>15}".format (left_aligned, center, right_aligned))
                print ()
                print ()
                print ()
                break


    elif y==3:
        print(">>>>> GAME EXITED <<<<<")
        break
    else:
        print ("Invalid Choice")

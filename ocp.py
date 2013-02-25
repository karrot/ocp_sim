import random
import time

#writing to txt function
def writing():
    f = open( 'results.txt', 'a' )
    f.write('player1 '+repr(player1)+'\n')
    f.write('player2 '+repr(player2)+'\n')
    f.write('\n')
    f.close()

# Now your sampling bit
rank1 = (10,10.5,12,12.5)
#10=10s
#10.5=10h
#12=Qs
#12.5=Qh
player1=100
player2=100

#x is player 1 stack size
#y is player 2 (computer) stack size
#optimal bluffing

sample=int(raw_input("Enter sample size: "))
for i in range(0,sample):
    x=random.choice(rank1)
    if x==12 or x==12.5:
        player1=player1+3
        player2=player2-3
            #he calls value bet no matter what - value bet of $2 gives 2:1 odds
            #twice as many value bets as bluffs
            #GTO must make 50 vb (queens), 25b, 25f (10s)
        
    if x==10:
        player1=player1-3
        player2=player2+3
    if x==10.5:
        player1=player1-1
        player2=player2+1
    print player1
    print player2
    writing()

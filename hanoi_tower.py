#Hanoi tower
import time

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
        
def moveDisk(fp,tp):
    print("Moving disk from",fp,"to",tp)

diskNumber = 1
while diskNumber != 0:
    print("============================")
    diskNumber = input("Give how many disk you have.\nGive 0 to end.\n============================\n")
    print("============================")
    diskNumber=int(diskNumber)
    moveTower(diskNumber,"A","C","B")

print("Thanks for your time.")
time.sleep(4)

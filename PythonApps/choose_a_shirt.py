#Check if the age and the weight of user are positive numbers
import time

def permission(x):
    if x <=0:
        return False
    else:
        return True

start=True
while start==True:
    name=input("Give your name.\n")
   
    age=input("\nGive your age.\n")

    #Check the value of the user's age
    validName = False
    while validName != True:
        try:
            age=int(age)
            validName = permission(age)
            if validName == False:
                age=input("\nThat's not a positive number of age. Try again!!!\n")        
        except ValueError:
            age=input("\nThat's not a number. Try again!!!\n")
            validName = False
            
            
    weight=input("\nGive your weight.\n")

    #Check the value of the user's weight
    validName = False
    while validName != True:
        try:
            weight=float(weight)
            validName = permission(weight)
            if validName == False:
                weight=input("\nThat's not a positive number of weight. Try again!!!\n")        
        except ValueError:
            weight=input("\nThat's not a weight. Try again!!!\n")
            validName = False    

    #Choice the color according to the user's age
    colore=["White","Pink","Red","Green","Blue","Black"]
    if(age>=0 and age<=17):
        col=colore[0]
    elif(age>=18 and age<=24):
        col=colore[1]
    elif(age>=25 and age<=35):
        col=colore[2]
    elif(age>=36 and age<=45):
        col=colore[3]
    elif(age>=45 and age<=55):
        col=colore[4]
    elif(age>55):
        col=colore[5]

    #Choice the size according to the user's weight
    size=["Small","Medium","Large","X-Large"]
    if(weight<50):
        siz=size[0]
    elif(weight>=50 and weight<=64):
        siz=size[1]
    elif(weight>=65 and weight<=79):
        siz=size[2]
    elif(weight>=80):
        siz=size[3]
    
    print("==========================================")
    print("Hey ",name,", it is cool to be ",age,
          " years old!\n You should buy a ",col," ",siz," shirt.")
    print("==========================================")
    
    end=input("Would you like to finish? Yes/No (Y/N): ")
    print("==========================================")
    
    if (end =="Y")or(end =="y"):
        print("Thanks for your time.")
        time.sleep(4)
        break
    
        



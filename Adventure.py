name = input("Enter Your Name:- ")
print("Welcome", name,"To This Adventure..!")

answer = input("You Are On Dirt Road, It Has Come To End And You Can Go To Left Or Right.Which Way Would You Like To go..?").lower()

if answer == "left":
    answer = input("You Come TO A River, You Can Walk Around It Or Swin Accross..? Type Walk To Walk Around And Swim TO Swim Accross :- ").lower()

    if answer == "swim":
        print("You Swam Accross And Were Eaten By Alligator..")
    elif answer == "walk":
        print("You Walk For many Miles, Ran Out Of Water And You Lost The Game :) ")
    else:
        print(' Not A Valid Option..')

elif answer == "right":
    answer = input("You Come To A Bridge, It Lookes Like Wobbly, Do You Want To Cross It Or Head Back.(Cross/Back)  ?").lower()
    
    if answer == "back":
        print("You Go Back And Lose :)")
    elif answer == "cross":
        answer = input("You Cross The Bridge And Meet A Stranger.Do You Want To Talk To Them(Yes/No)..? ").lower()

        if answer == "yes":
            print("You Talk To Stranger And The Give You Gold.You Win..!!")
        elif answer == "no":
            print("You Ignore The Stranger And They Are Offended.And You Lose :)")
        else:
            print(' Not A Valid Option..')


    else:
        print(' Not A Valid Option..')

else:
    print(' Not A Valid Option..')

print("Thank You For Trying", name)
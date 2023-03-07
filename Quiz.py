print ("Welcome To My Computer Quiz..! ")

playing = input("Do You Want TO Play Game..? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play...")
score = 0

answer = input("What Does CPU Stand For..? ").lower()
if answer == "central processing unit":
    print('Correct..!')
    score = score+1
else:
    print("Incorrect..!")

answer = input("What Does GPU Stand For..? ")
if answer.lower() == "graphic processing unit":
    print('Correct..!')
    score += 1
else:
    print("Incorrect..!")

answer = input("What Does RAM Stand For..? ")
if answer.lower() == "random access memory":
    print('Correct..!')
    score +=1
else:
    print("Incorrect..!")

answer = input("What Does PSU Stand For..? ")
if answer.lower() == "power supply":
    print('Correct..!')
    score += 1
else:
    print("Incorrect..!")

print("You Got " + str(score) + " Question Correct..!")
print("You Got " + str((score/4) * 100) + "%.")
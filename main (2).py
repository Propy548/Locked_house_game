import random
import time

global score #A variable For the player's score to use it in the code 
#wherever you need it.
score = 100 

global password 
password ="pyS" #This is the password that we will check to see if the player won or not


#Function to delay the print command for 2 seconds.
def print_pause(*messages):
      for message in messages:
            print(message)
            time.sleep(2)

#Function in case the player chooses a number that is not allowed(1,2,3).

# (1,2,3)دالة في حال اختار المستخدم رقم غير المسموح به 
def invalid_choice():
    print("Invalid choice, pls just enter (1,2,3)")
    #try_again=int(input("Let's try again, enter your choice:"))
    #return try_again

def clues():
   global password
   get_clues=input("Did you get the two clues(y/n):")
   if get_clues.lower()=="y":
       print_pause("Good job ")
       your_password=input("Enter the password you have got:")
       if your_password==password:
          print_pause("Congratulations,You win\nYou can get out of this house now")

   
   else: 
          print ("okay,let's get the clues")
          
   



#Introduction to the rules of the game and how to play it.
#تعريف بقواعد اللعبة وكيفية لعبه
def game_rules():
    print_pause("***Welcome to the locked house game...***")
    print_pause("Somehow you found your self in a locked house.")
    print_pause("there are 3 rooms in front of you,these rooms are your way out.")
    print_pause("This house is locked with a password.")
    print_pause("and to know it, there are clues to help you.")
    print_pause("two of these rooms have the clues.")
    print_pause("and the other room contains DANGEROUS ANIMALS")
    print_pause("you need to know the right password from the clues to win")
    print_pause("You will have a score starts with 100")
    print_pause("Your score will increase or decrease by 50 depending on your choice ")
    print_pause("Your score will not affect your progress in the game"
"\nit is just for encouragement.")
    print_pause("Are you ready,let's get started.")

#A variable using randomness to determine 
#the danger you will face if you enter the wrong room.
#متغير باستخدام العشوائية ليحدد الخطر الذي ستواجهه أذا دخلت الغرفة الخاطئة 
random_danger=random.choice(["snacks","lions","wild dogs"])


#A function that allows the player to play again if he want.
#دالة للسماح للاعب باللعب مرة أخري إذا أراد
def play_again():
    while True:
        choice =input("Do you want to play again(y/n):")
        if choice.lower()=="y":
           continue 
        else:
           break







#A function to determine what is in the first room.
#دالة لتحديد ماذا يحدث في الغرفه الاولي
def room_1():
    global score
    print_pause("Good choice,let's see the first clue")

    print_pause("our first clue is:"
                "\nOne of the symbols of ancient Egyptian civilization")
    print_pause("and considered one of the seven wonders of the world.")
    clue_one=input("Write the first TWO letters of its name as small:\n")
    while True :
            if clue_one==("py"):
               print("Good guess, remember it to use it later")
               score +=50
               print_pause(f"Your score is {score}")
               
             
               break
             
            else: 
              print_pause("It seems you couldn't guess it.\nLet's give it other try.")
              clue_one=input("Enter your new guess:\n")
           



#A function to determine what is in the second room .
#دالة لتحديد ماذا يحدث في الغرفة الثانية 

def room_2():
      global score
      print_pause("Oops,bad choice")
      print_pause(f"This room is filled with {random_danger}")
      print_pause("Let's escape from here quickly ")
      print_pause("your score will decrease because you chose the wrong room")
      score -=50
      print(f"Your score is {score}")
      
      
         
         
         
#A function to determine what is in the third room .
#دالة لتحديد ماذا يحدث في الغرفة الثالثة 

def room_3():
    global score
    print_pause("Good choice,let's get the second clue")
    print_pause("Our second clue is:\n")
    print_pause("He is a native of Egypt,"
                "\nand considered one of the ten best football players in the world.")
    print_pause ("Write the first letter of his father's name in capital")
    second_clue=input("Enter your guess:")
    while True:
        if second_clue=="S":
           print_pause("Good guess,remember it to use it later.")
           score +=50
           print_pause(f"Your score is {score}")
           break
        else:
          
           print_pause("It seems you couldn't guess it.\nLet's give it another try.")
           second_clue=input("Enter your guess:")


#room_number=int(input("Enter the room number(1,2,3):"))
#التحقق مما إذا كان المستخدم ادخل رقم صحيح ام لا(1,2,3)
#واذا ادخل رقم من القائمة الموضحة له كشف ما يوجد في هذه الغرف له

while True:
    room_number =int(input("Enter the room number:"))
    if room_number not in (1,2,3):
       invalid_choice()
    else:
        #while  room_number in (1,2,3):
      if room_number == 1:
         print_pause()
         room_1()
         #print_pause("Let's get the other clue")
         clues()
         #room_number =int(input("Enter the room number(1,2,3):"))
         
            




      elif room_number == 2:
         print_pause()
         room_2()
         room_number=int(input("Enter the room number(1,2,3):"))

      else:
         print_pause()
         room_3()
         #room_number=int(input("Enter the room number(1,2,3)"))

         break



play_again()    ################  
def game():
   



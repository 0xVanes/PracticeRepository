print("You are a detective trying to solve a mysterious disappearance. A wealthy businessman, Mr. White, has vanished from his mansion. You must explore the mansion, discover hidden clues, and solve puzzles to unravel the mystery and find Mr. White.")

People = {
'Mr. White': 'A wealthy businessman who has vanished from his mansion.', 
'Mr. Blue': 'A friend of Mr. White who has anxiety.',
'Mr. Red': 'A colleague of Mr. White who has only one leg.',
'Mr. Black': 'Was the husband of Mrs. Pink',
'Mrs. Pink': 'A very beautiful secretary of Mr. White'}

print(f"{People} are the people in the mansion.")

puzzles = [
    {
        'type': 'riddle',
        'question': 'What has keys but can\'t open locks?',
        'solution': 'piano',
        'story': 'You find a hidden key inside the piano that opens a secret door. The door leads to a room, full of perfume.'
    },
    {
        'type': 'code',
        'question': 'Decrypt this message: "Wklv phvvdjh lv hqfubswhg xvlqj Fdhvdu flskhu."',
        'solution': 'This message is encrypted using Caesar cipher',
        'story': 'The decrypted message reveals a clue about a hidden safe in Mr. White\'s office. Mr. White is in huge debt.'
    },
    {
        'type': 'pattern',
        'question': 'What comes next in the sequence? 2, 4, 8, 16, ...',
        'solution': '32',
        'story': 'Entering the correct number into a keypad unlocks a mysterious box containing a crucial piece of evidence. A love poem about Mrs. Pink from Mr. Blue.'
    },
    {
        'type': 'riddle',
        'question': 'What has a head, a tail, but does not have a body?',
        'solution': 'coin',
        'story': 'You find an old coin which reveals the year when the mansion was built. Mr White has a lot of money.'
    },
    {
        'type': 'code',
        'question': 'Decrypt this message using the reversed alphabet: "Gsv xzhrmt yvhg zm gsv xlnnkzmzoob."',
        'solution': 'The secret lies at the mysterious door',
        'story': 'A mysterious door is discovered, leading to a hidden room. Mr Blue\'s been using Mr White\'s money.'
    },
    {
        'type': 'pattern',
        'question': 'What comes next in the sequence? 1, 1, 2, 3, 5, ...',
        'solution': '8',
        'story': 'The correct number reveals the number of steps to take in a secret passage.'
    },
    {
        'type': 'riddle',
        'question': 'What is always in front of you but can’t be seen?',
        'solution': 'future',
        'story': 'A painting of Mr. White reveals a hidden message about his plans. He wanted to run away from Mr. Blue.'
    },
    {
        'type': 'code',
        'question': 'Decode this Morse code: ".- / --. .... --- ... -"',
        'solution': 'A ghost',
        'story': 'A hidden diary tells a story about a ghost haunting the mansion. Which is in fact Mr. Red\'s cousin. Mr. Red\'s cousin is actually Mr. Black.'
    },
    {
        'type': 'pattern',
        'question': 'What comes next in the sequence? 3, 6, 12, 24, ...',
        'solution': '48',
        'story': 'Entering the correct number into a lock reveals a hidden chamber. In there you can see Mr. Black\'s corpse which is preserved.'
    },
    {
        'type': 'riddle',
        'question': 'What can you hold in your left hand but not in your right?',
        'solution': 'your right elbow',
        'story': 'Discovering a hidden lever shaped like an elbow, you open a secret compartment. You could see blood stains.'
    }
]

import random
import time


def play_puzzle(puzzle, time_limit, solvedpuzzle):       
     
     while len(puzzles) != 0:

       random_puzzle = random.choice(puzzles)
       print(random_puzzle['question'])
       answer = input("Your answer: ").lower()
       if answer != random_puzzle['solution']:
         print("You are wrong! We will deduct 30s from your timer")
         time_limit -= 30
         puzzles.remove(random_puzzle)
         if len(puzzles) == 0:
             print("No more puzzle.")
             print(f"Total puzzle solved = {10-solvedpuzzle}")
             bonuspuzzle()
             break
         return play_timer(time_limit, solvedpuzzle)
       elif answer == random_puzzle['solution']:
             print(random_puzzle['story'])
             time.sleep(5)
             puzzles.remove(random_puzzle)
             

     else:
       print("No more puzzle.")
       print(f"Total puzzle solved = {10-solvedpuzzle}")
       bonuspuzzle()


def play_timer(time_limit, solvedpuzzle):
    while len(puzzles) != 0:
        for puzzle in puzzles:
            solvedpuzzle += 1
            elapsed_time = time.time() - start_time
            if elapsed_time >= time_limit:
                print("Time is Up! You Fail!")
                break
            else:
                print(f"You have {round(time_limit - elapsed_time)} seconds left.")
                play_puzzle(puzzle, time_limit, solvedpuzzle)
    
            
def bonuspuzzle():
    correct = 10-solvedpuzzle
    if correct >= 4 and len(puzzles) == 0:
         Trial = 3
         Murderer = input(f"Who is the murderer? (You have {Trial} guesses) ").lower
         while Trial != 1 and Murderer != 'mrs. pink':
             Trial -= 1
             print(f"Try again. You have {Trial} guesses left.")
             Murderer = input(f"Who is the murderer? (You have {Trial} guesses) ").lower()
             if Murderer == 'mrs. pink':
                 print("You are right! You win!")
                 print("Mrs. Pink is the murderer. She knew that Mr. White was the one who killed Mr. Black, so she make Mr. Blue who is currently in love with Mrs. Pink make Mr. White go bankrupt. Mr. White is now in debt and he met Mrs. Pink to ask for financial aid. But since Mrs. Pink knew that he will come to her sooner or later, she decided to kill him with a lever.")
             else:
                 print("You lose!")
                 break



play = input("Do you want to play? (yes/no): ").lower()

if play == "yes":
    solvedpuzzle = 0
    print("\nYou have 5 minutes to finish the challenge. Start now!")
    start_time = time.time()
    play_timer(300, solvedpuzzle)


else:
    print("Okay, maybe next time.")
import random

def roll():
    num=random.randint(1,6)
    return num

value=roll()

while True:
    players=input("Enter the number of players (2-4) ")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print("must be atleast 2 players")
    else:
        print("Invalid try again")        


max_score=50
player_scores=[0 for _ in range(players)]

while max(player_scores)<max_score:
    
    for player_idx in range(players):
        print("\n player",player_idx+1,"has started\n")
        current_score=0

        while True:
            should_roll=input("Would you like to roll(y)? ")
            if should_roll.lower()!="y":
                break
        
            value=roll()
            if value==1:
                current_score=0
                print("You rolled a one , you are done")
                break
            else:
                current_score+=value
                print("you rolled a", value)  

            print("your score is",current_score)
            if(current_score>=max_score):
                break

        player_scores[player_idx] += current_score  
        print("Your total score is :", player_scores[player_idx])

max_score=max(player_scores)
winner=player_scores.index(max_score)
print("Player who won is",winner)







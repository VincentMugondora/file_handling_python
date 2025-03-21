# rock paper scissors game

def get_choices():
    player_choice = "rock"
    computer_choice = "paper"

    choices = {
        "player": player_choice, 
        "computer": computer_choice
        }

    return choices

choices = get_choices()

print(choices)
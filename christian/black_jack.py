import random
import os



def deal_card():
        cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

def calculate_score(card_list):
        if sum(card_list) == 21:
            return 0 
        if 11 in card_list and sum(card_list) > 21:
            card_list.remove(11)
            card_list.append(1)
            return sum(card_list)
        return sum(card_list)


def is_it_blackjack(player_score, computer_score):
    if computer_score == 0:
        print(f"{final_hands()}\nThe computer got a Blackjack.\nYou lose")
            
    elif player_score == 0:
        print(f"{final_hands()}\nYou got a Blackjack!\nYou WIN!")
          
    else:
        print(f"\nYour current hand: {player_cards}\nYour current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
    

def compare_score(player_score, computer_score):
    if computer_score > 21:
        print(final_hands())
        print("The computer went over 21.\nYou WIN!")

    elif player_score > computer_score:
        print(final_hands())
        print("You WIN!")

    elif player_score == computer_score:
        print(final_hands())
        print("You scored the same\nIt's a draw :/")

def final_hands():
    return f"\nYour final hand: {player_cards}, final score: {player_score}\nComputer's final hand: {computer_cards}, final score: {computer_score}"


player_cards = []
computer_cards = []
player_score = 0
computer_score = 0



continue_playing = True
   
while continue_playing:
    
    user_response = input("Would you like to play a game of Blackjack? Type 'y' for yes, or 'n' for no: ").lower()
    
    if user_response == 'y':
        player_cards.clear()
        computer_cards.clear()
        player_score = 0
        computer_score = 0
        os.system('clear')
        
        
        for card in range(2):
            player_cards.append(deal_card())
            computer_cards.append(deal_card())
          
        computer_score = calculate_score(computer_cards)
        print(f"Computer score: {computer_score}")
        player_score = calculate_score(player_cards)
        print(f"Player score: {player_score}")

        is_it_blackjack(player_score, computer_score)

        if computer_score == 0 or player_score == 0:
            continue 
            
        additional_card = True
        while additional_card:
            
            draw_card = input("\nWould you like to draw another card? Type 'y' for yes, or type 'n' to pass: ").lower()
        
            if draw_card == 'y':
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
                # print(f"Player score: {player_score}")

                if player_score > 21:
                    print(final_hands())
                    print("You went over 21, you lose.")
                    additional_card = False
                    
                    
                else:
                    is_it_blackjack(player_score, computer_score)
                    continue
                    
            elif draw_card == 'n':
                additional_card = False
                
            computer_less_than_17 = True
            while computer_less_than_17:
                if computer_score < 17:
                    #Added cards are not showing up in final hand?
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                    print(f"Computer hand: {computer_cards}")
                    print(f"Computer score: {computer_score}")
                    continue
                        
                elif computer_score >= 17:
                    computer_less_than_17 = False
                    print(f"Computer cards: {computer_cards} ")
                    print(f"Computer score: {computer_score}")
                    
                    print("Got to computer score is greater than or equal to 17")
                    compare_score(player_score, computer_score)
                    continue
                

    else:
        print("I see, you don't want to play this great game I made.")
        continue_playing = False
        
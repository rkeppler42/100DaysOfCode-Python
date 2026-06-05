import art
import random



def give_random_card(hand: list) -> None:
    """
    Gives a random card to the hand
    :param hand: player's or dealer's hand
    :return: None
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)


def print_game_state(your_cards: list, dealer_cards:list) -> None:
    """
    Prints the game state
    :param your_cards: player's hand
    :param dealer_cards: dealer's hand
    :return: None
    """
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")


def print_final_game_status(your_cards: list, dealer_cards: list) -> None:
    """
    Prints the final game status
    :param your_cards: player's hand
    :param dealer_cards: dealer's hand
    :return: None
    """
    print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
    print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
    if sum(your_cards) > 21:
        print("You went over. You lose 😭")
    elif sum(dealer_cards) > 21:
        print("Opponent went over. You win 😁")
    elif sum(your_cards) == sum(dealer_cards):
        print("It's a draw 🙃")
    elif sum(your_cards) > sum(dealer_cards):
        print("You win 😃")
    else:
        print("You lose 😤")



def player_turn(your_cards: list, dealer_cards: list) -> None:
    """
    Deals cards to the player according to their choice and score
    :param your_cards: player's hand
    :param dealer_cards: dealer's hand
    :return: None
    """
    while sum(your_cards) < 21:
        print("Type 'y' to get another card, type 'n' to pass: ")
        if input() != "y":
            break
        give_random_card(your_cards)
        print_game_state(your_cards, dealer_cards)


def dealer_turn(dealer_cards: list) -> None:
    """
    Deals cards to the dealer according to rules of the game (if sum of hand is less than 17 keep giving cards)

    :param dealer_cards: dealer's hand
    :return: None
    """
    while sum(dealer_cards) < 17:
        give_random_card(dealer_cards)



def main() -> None:
    """
    Main function of the game
    :return: None
    """
    print(art.logo)
    print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    user_input = input()
    while user_input != "n":
        if user_input == "y":
            your_cards = []
            dealer_cards = []
            give_random_card(your_cards)
            give_random_card(your_cards)
            give_random_card(dealer_cards)
            give_random_card(dealer_cards)
            print_game_state(your_cards, dealer_cards)
            player_turn(your_cards, dealer_cards)
            if sum(your_cards) <= 21:
                dealer_turn(dealer_cards)
            print_final_game_status(your_cards, dealer_cards)
        print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        user_input = input()


if __name__ == "__main__":
    main()
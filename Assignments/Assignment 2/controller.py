from card import *
from wallet import *
def main():
    '''
    main controller class. Runs user through main menu and allows them to call
    wallet methods to modify the wallet
    :return:
    '''
    cards_ = generate_card_slots()
    wallet = Wallet(cards_)
    user_input = None;
    while user_input != "q":
        print("Welcome to your wallet!")
        print(f"Enter 'add' to add a card to your wallet")
        print(f"Enter 'remove' to remove a card from your wallet")
        print(f"Enter 'display' to view your wallet")
        print(f"Enter 'search' to search your wallet for a specific card")
        print(f"Enter 'save' to save your wallet to a file")
        print(f"Enter 'q' to exit")
        user_input = input('>')
        user_input = user_input.casefold()
        if user_input == 'add':
            wallet.add_card()

        elif user_input == 'remove':
            user_query = None
            print("Please enter the nickname of the card you would like to remove")
            user_query = input('>')
            wallet.remove_card(user_query)

        elif user_input == 'display':
            print(f"Enter 'Credit' to view all Credit Cards")
            print(f"Enter 'Debit' to view all Debit Cards")
            print(f"Enter 'Loyalty' to view all Loyalty Cards")
            print(f"Enter 'Business' to view all Business Cards")
            print(f"Enter 'ID' to view personal ID cards")
            print(f"Enter 'Other' to view all other cards")
            print(f"Leave blank if you just want to see the entire wallet")
            user_input = input(">")
            user_input = user_input.casefold()
            if user_input == 'credit':
                wallet.display_wallet_by_type(CreditCard)
                input("\nPress Enter to continue.")
            elif user_input == 'debit':
                wallet.display_wallet_by_type(DebitCard)
                input("\nPress Enter to continue.")
            elif user_input == 'loyalty':
                wallet.display_wallet_by_type(LoyaltyCard)
                input("\nPress Enter to continue.")
            elif user_input == 'business':
                wallet.display_wallet_by_type(BusinessCard)
                input("\nPress Enter to continue.")
            elif user_input == 'id':
                wallet.display_wallet_by_type(PersonalIdentificationCard)
                input("\nPress Enter to continue.")
            elif user_input == 'other':
                wallet.display_wallet_by_type(OtherCard)
                input("\nPress Enter to continue.")
            else:
                wallet.display_wallet()
                input("\nPress Enter to continue.")

        elif user_input == 'search':
            print("would you like to search by Card Name or Number?")
            user_input = input(">")
            user_input = user_input.casefold()
            if user_input == 'name' or user_input == 'card name':
                user_query = "";
                print("enter the card name")
                user_input = user_input.casefold()
                user_query = input('>')
                wallet.search_wallet_by_name(user_query)
            elif user_input == 'number' or user_input == 'card number':
                user_query = None;
                print("enter the card number")
                user_query = input('>')
                wallet.search_wallet_by_number(user_query)
            else:
                continue

        elif user_input == 'save':
            print("Enter a name for your textfile")
            path = input(">")
            print("Saving to file..")
            wallet.write_to_file(path+'txt')
            print(f"Saved to: {path+'txt'}")

        elif user_input == 'q':
            print("Have a nice day! :)")

        else:
            print('Sorry that is an invalid option, press enter to be returned to the main menu')
            input()


if __name__ == '__main__':
    main()
from options import choice
import sys

def main():
    repeat=0 #variable to repeatidly display options menu in a while loop
    my_options=choice()
    while(repeat==0):
        print("***** Web Scrapping Adventure *****")
        print("1. Display Latest Deals")
        print("2. Analyze Deals by Category")
        print("3. Find Top Stores")
        print("4. Log Deal Information")
        print("5. Exit")
        choice_valid=0 #variable for while to repeatidly tell user to enter choice until a right input (1-5) is entered

        while(choice_valid==0):

            user_choice = input("Enter your choice (1-5): ")

            # Check if the input is a valid choice
            if user_choice.isdigit() and 1 <= int(user_choice) <= 5:
                option_choice = int(user_choice)

                if option_choice == 1:
                    # Code for option 1
                    print()
                    my_options.DisplayLatestDeals()
                    print()
                    choice_valid=1
                elif option_choice == 2:
                    # Code for option 2
                    print()
                    my_options.AnalyzeDealsByCategory()
                    print()
                    choice_valid=1
                elif option_choice == 3:
                    # Code for option 3
                    user_nb = input("Enter the number of top stores to display: ")
                    if user_nb.isdigit():
                        nb = int(user_nb)
                        print()
                        my_options.topStores(nb)
                        print()
                        choice_valid=1
                elif option_choice == 4:
                    # Code for option 4
                    print()
                    my_options.logDealInfo()
                    print()
                    choice_valid=1
                elif option_choice ==5:
                    print("Exiting the program. Goodbye!")
                    sys.exit(0)
            else:
                print("Please enter a number between 1 and 5")


                    

if __name__ == "__main__":
    main()




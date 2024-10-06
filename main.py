from database_setup import setup_database
from menu_recommender import recommend_food
from chatgpt_integration import get_menu_recommendation_from_gpt

def main():
    # Database setup
    setup_database()
    
    # Get user input to recommend cuisine type
    print("Choose a type of cuisine: (Korean, Chinese, Japanese, Western)")
    cuisine_type = input(">> ").strip()

    chosen_restaurant_id, chosen_restaurant_name = recommend_food(cuisine_type)

    if chosen_restaurant_id is not None:
        while True:
            print("\nWould you like to hear more details about a specific menu item? (yes/no)")
            more_info = input(">> ").strip().lower()
            if more_info == 'yes':
                menu_name = input("\nEnter the name of the menu item you want to know more about: ").strip()
                # Get detailed description from GPT-3.5
                description = get_menu_recommendation_from_gpt(menu_name)
                print(f"\nDetailed description of {menu_name}:\n{description}")
            elif more_info == 'no':
                print("Thank you for using our service. Enjoy your meal!")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()

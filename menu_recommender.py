import sqlite3

# SQLite database connection
conn = sqlite3.connect('korean_restaurants.db')
cursor = conn.cursor()

# Add review function
def add_review(restaurant_id, review_text, rating):
    cursor.execute("INSERT INTO Reviews (restaurant_id, review_text, rating) VALUES (?, ?, ?)",
                   (restaurant_id, review_text, rating))
    conn.commit()
    print("Review added successfully.")

# Show reviews function
def show_reviews(restaurant_id):
    cursor.execute("SELECT review_text, rating FROM Reviews WHERE restaurant_id = ?", (restaurant_id,))
    reviews = cursor.fetchall()
    if reviews:
        print("\nList of reviews:")
        for review in reviews:
            print(f"- Rating: {review[1]}, Review: {review[0]}")
    else:
        print("No reviews available.")

def recommend_food(cuisine_type):
    cursor.execute("SELECT id, name FROM Restaurants WHERE cuisine_type = ?", (cuisine_type,))
    restaurants = cursor.fetchall()
    
    if not restaurants:
        print("No restaurants available for the selected cuisine.")
        return None

    print(f"\nList of {cuisine_type} restaurants:")
    for idx, restaurant in enumerate(restaurants, start=1):
        print(f"{idx}. {restaurant[1]}")

    try:
        restaurant_choice = int(input("\nSelect the number of the restaurant you want a recommendation for: "))
        chosen_restaurant_id, chosen_restaurant_name = restaurants[restaurant_choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Please restart the program and select a valid option.")
        return None

    # Retrieve menu for the selected restaurant
    cursor.execute("SELECT name, description FROM Menus WHERE restaurant_id = ?", (chosen_restaurant_id,))
    menus = cursor.fetchall()

    if menus:
        print(f"\nMenu at {chosen_restaurant_name}:")
        for menu in menus:
            print(f"- {menu[0]}: {menu[1]}")
    else:
        print(f"No menu available for {chosen_restaurant_name}.")

    # Show reviews for the selected restaurant
    show_reviews(chosen_restaurant_id)

    # Return restaurant ID and name
    return chosen_restaurant_id, chosen_restaurant_name

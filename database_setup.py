import sqlite3

# SQLite database connection
conn = sqlite3.connect('korean_restaurants.db')
cursor = conn.cursor()

# Database setup (table creation)
def setup_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            cuisine_type TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Menus (
            id INTEGER PRIMARY KEY,
            restaurant_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Reviews (
            id INTEGER PRIMARY KEY,
            restaurant_id INTEGER NOT NULL,
            review_text TEXT,
            rating INTEGER CHECK (rating >= 1 AND rating <= 5),
            FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id)
        )
    ''')
    conn.commit()

# Insert sample data
def insert_sample_data():
    cursor.execute("SELECT COUNT(*) FROM Restaurants")
    if cursor.fetchone()[0] == 0:  # 만약 Restaurants 테이블에 데이터가 없다면
        cursor.execute("INSERT INTO Restaurants (name, cuisine_type) VALUES ('Kimchi House', 'Korean')")
        cursor.execute("INSERT INTO Restaurants (name, cuisine_type) VALUES ('Sushi World', 'Japanese')")
        cursor.execute("INSERT INTO Restaurants (name, cuisine_type) VALUES ('Panda Express', 'Chinese')")
        cursor.execute("INSERT INTO Restaurants (name, cuisine_type) VALUES ('Burger King', 'Western')")

        cursor.execute("INSERT INTO Menus (restaurant_id, name, description) VALUES (1, 'Kimchi Stew', 'Spicy kimchi stew')")
        cursor.execute("INSERT INTO Menus (restaurant_id, name, description) VALUES (2, 'Sushi', 'Fresh fish sushi')")
        cursor.execute("INSERT INTO Menus (restaurant_id, name, description) VALUES (3, 'Jjajangmyeon', 'Sweet black bean sauce noodles')")
        cursor.execute("INSERT INTO Menus (restaurant_id, name, description) VALUES (4, 'Cheeseburger', 'Beef patty with cheese')")
        conn.commit()

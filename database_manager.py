import sqlite3

# Create database lava_menu.db
conn=sqlite3.connect('lava_menu.db')
cur=conn.cursor()

# Create table menu and insert data
cur.execute('CREATE TABLE IF NOT EXISTS menu '
            '(id INTEGER PRIMARY KEY, category TEXT, item_name TEXT, price REAL, description TEXT)')
cur.execute('''
             INSERT INTO menu (category, item_name, price, description) VALUES 
             ('Appetizers', 'Spring rolls', 7.99, '6 pieces'), ('Appetizers', 'Spam musubi', 6.99, '2 pieces'),
             ('Appetizers', 'Crab rangoon', 8.99, '8 pieces'), ('Appetizers', 'Cajun fries', 4.99, '12 oz'), 
             ('Rice bowl', 'Teriyaki chicken', 10.99, 'includes rice, mixed veggies and meat'), 
             ('Rice bowl', 'Teriyaki shrimp', 10.99, 'includes rice, mixed veggies and meat'),
             ('Chicken', 'Hawaiian bbq chicken', 13.49, 'Grilled marinated chicken'), 
             ('Chicken', 'Curry chicken katsu', 13.49, 'Breaded chicken cutlet with curry sauce'),
             ('Seafood', 'Garlic shrimp', 14.49, 'Sauteed with garlic and butter'), 
             ('Seafood', 'Island white fish', 13.99, 'Grilled white fish with tropical salsa'),
             ('Tropical smoothies', 'Hawaiian punch', 4.69, 'Passion fruit & pina colada'), 
             ('Tropical smoothies', 'Island berry', 4.69, 'Guava & wildberry')
            '''
             )
conn.commit()
conn.close()
print('Data base and table created!!!')


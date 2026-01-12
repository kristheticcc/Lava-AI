import sqlite3

def search_menu(user_query):
    # Connect to the database
    conn=sqlite3.connect('lava_menu.db')
    cur=conn.cursor()

    # Search for matching items
    key_words=f"%{user_query}%"

    # SQL query to search in category, item_name, and description
    query='''
            SELECT * FROM menu WHERE 
            category LIKE ?
            OR item_name LIKE ?
            OR description LIKE ?'''

    # Execute the query with parameters
    cur.execute(query, (key_words, key_words, key_words))

    results=cur.fetchall()
    conn.close()

    if results:            # If there are matching items
        return results
    else:                  # If no matching items found
        return 'No matching items found.'

import sqlite3
import json

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

# JSON schema for the tool function
tool_function={
    "name": "search_menu",
    "description": "Use this tool to search for menu items based on user queries.",
    "parameters": {
        "type": "object",
        "properties": {
            "user_query": {
                "type": "string",
                "description": "The user's query about the menu items."
            }
        },
        "required": ["user_query"],
        "additionalProperties": False
    }
}

# List of tools to be used in the chat function
tools=[{"type": "function", "function": tool_function}]

# Function to handle tool calls
def handle_tool_calls(message):
    responses=[]

    # Process each tool call in the message
    for tool_call in message.tool_calls:
        if tool_call.function.name=="search_menu":
            arguments=json.loads(tool_call.function.arguments)
            user_query=arguments.get("user_query", "")
            result=search_menu(user_query)
            responses.append({
                "role": "tool",
                "content": result,
                "tool_call_id": tool_call.id
            })
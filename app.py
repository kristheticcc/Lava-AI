
# Import necessary libraries
import os
from dotenv import load_dotenv
from openai import OpenAI
from menu_tools import search_menu, handle_tool_calls, tools
import gradio as gr

# Load environment variables from .env file
load_dotenv(override=True)
api_key=os.getenv('OPENAI_API_KEY')

# Check if API key is available
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI client
model='gpt-4.1-mini'
client=OpenAI()

# System prompt to guide the AI's behavior
system_prompt="""
You are Lava, a helpful assistant for Lava Hawaiian BBQ restaurant.
Your task is to greet users and assist them in finding menu items.
If you don't know the answer, just say so. 
If a user asks 'Are there any discounts?' respond with something like 'Sorry, we only have discounts during holiday season.'
"""

# Chat function to handle user queries
def chat(message, history):
    current_system_prompt=system_prompt
    history = [{"role": h["role"], "content": h["content"]} for h in history]

    if "dessert" in message.lower():
        current_system_prompt += ("If user asks about desserts, respond with something like "
                          "'We don't have desserts, but we do have smoothies.")

    messages=[{"role": "system", "content": current_system_prompt}]+ history + [{"role": "user", "content": message}]
    response=client.chat.completions.create(model=model, messages=messages, tools=tools)

    # For multiple tool calls
    while response.choices[0].finish_reason=="tool_calls":
        msg_obj=response.choices[0].message
        tool_responses=handle_tool_calls(msg_obj)
        messages.append(msg_obj)
        messages.extend(tool_responses)
        response=client.chat.completions.create(model=model, messages=messages, tools=tools)

    return response.choices[0].message.content

# Gradio interface
view=gr.ChatInterface(
                      fn=chat,
                      type="messages",
                      title="Lava AI",
                      chatbot=gr.Chatbot(
                                type="messages",
                                value=[{"role": "assistant", "content": "Hi, I'm Lava! 🌴 "
                                "I'm your AI assistant for iLava Hawaiian BBQ. How can I help you today?"}]),
                      )

# Launch the Gradio app
if __name__=="__main__":
    view.launch()


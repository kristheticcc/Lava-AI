
# Import necessary libraries
import os
from dotenv import load_dotenv
from openai import OpenAI
from menu_tools import search_menu
import gradio as gr

# Load environment variables from .env file
load_dotenv(override=True)
api_key=os.getenv('OPENAI_API_KEY')

# Check if API key is available
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI client
model='gpt-4.1 mini'
client=OpenAI()

# System prompt to guide the AI's behavior
system_prompt="""
You are Lava, a helpful assistant for Lava Hawaiian BBQ restaurant.
Your task is to greet users and assist them in finding menu items.
If you don't know the answer, just say so. 
If a user asks 'Are there any discounts?' respond with something like 'Sorry, we only have discounts during holiday season.'
"""



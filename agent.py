import google.generativeai as genai
from agno.agent import Agent
from config import GEMINI_API_KEY, SYSTEM_PROMPT
from chat import GeminiAssistant  # custom class defined in chat.py

# ---------------------------------------------------
# Initialize Gemini-powered model via custom wrapper
# ---------------------------------------------------
recipe_model = GeminiAssistant(api_key="GEMINI_API_KEY")

# ---------------------------------------------------
# Define the agent using Agno + Gemini + prompt
# ---------------------------------------------------
recipe_agent = Agent(
    model=recipe_model,
    tools=[],  # Add Agno @tool functions here if needed
    instructions=SYSTEM_PROMPT,
    markdown=True,
)

# ---------------------------------------------------
# Core function to get recipe idea from user input
# ---------------------------------------------------
def generate_recipe_idea(user_query: str) -> str:
    """
    Uses the Gemini model to generate a recipe based on ingredients or a description.
    """
    conversation = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ]
    response = recipe_agent.model.chat(conversation)
    return response


# ---------------------------------------------------
# External recipe search using Exa API
# ---------------------------------------------------
import requests
from config import EXA_API_KEY

def fetch_recipe_links(query: str):
    """
    Fetches real-world recipe links using Exa API.
    Returns a list of recipes with title, URL, author, publish date, and image.
    """
    url = "https://api.exa.ai/search"
    headers = {
        "x-api-key": EXA_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "query": query,
        "num_results": 6,
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        results = response.json()
    except Exception:
        return []

    recipe_list = []
    for item in results.get("results", []):
        recipe_list.append({
            "title": item.get("title", "Untitled"),
            "url": item.get("url", "#"),
            "author": item.get("author", ""),
            "published": item.get("publishedDate", "")[:10],
            "image": item.get("image", None),
        })

    return recipe_list

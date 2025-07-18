import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from agno.agent import Agent
import requests

# ------------------------------
# 🔐 Load environment variables
# ------------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("AIzaSyCrkZJib8QQFXD12FprTt0RXdLBwvYyMYg")
EXA_API_KEY = os.getenv("e93ca605-824c-4b1a-b16c-9c57ad6e6ed4")

# ------------------------------
# 🤖 Gemini Model Wrapper Class
# ------------------------------
class RecipeAI:
    def __init__(self, model_name="models/gemini-2.5-pro", api_key=None):
        if api_key:
            genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=genai.GenerationConfig(
                temperature=0.7,
                top_p=1,
                top_k=1,
                max_output_tokens=2048,
            )
        )

    def chat(self, messages):
        prompt_text = "\n".join([m["content"] for m in messages])
        response = self.model.generate_content(prompt_text)
        return response.text.strip()

# ------------------------------
# 🌐 Exa Search API Handler
# ------------------------------
class RecipeFinder:
    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, keywords: str):
        url = "https://api.exa.ai/search"
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }
        payload = {
            "query": keywords,
            "num_results": 5
        }
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=10)
            r.raise_for_status()
            result = r.json()
        except Exception as e:
            return f"❌ Exa API Error: {e}"

        entries = result.get("results", [])
        return [
            {
                "title": e.get("title", "Untitled"),
                "url": e.get("url", "#"),
                "author": e.get("author", ""),
                "published": e.get("publishedDate", "")[:10],
                "image": e.get("image", None),
            }
            for e in entries
        ] if entries else []

# ------------------------------
# 🧠 System Prompt
# ------------------------------
INSTRUCTION = """
You are RecipeBot Pro, an expert virtual chef.

Respond ONLY in markdown and always include:
- A fun recipe name
- A structured list of ingredients with amounts
- Clear, step-by-step instructions
- Emojis for tags: ⏱️, 🍽️, 🌱, 🌿, 🌾, 🥜
- Approximate nutrition info per serving
- Extra tips on plating, swaps, and storage

Stay friendly and compact. Tailor for user needs and diets.
"""

# ------------------------------
# 🤖 Initialize Agent + Tools
# ------------------------------
chef_ai = RecipeAI(api_key=GEMINI_API_KEY)
recipe_tool = RecipeFinder(EXA_API_KEY)

agent = Agent(
    model=chef_ai,
    tools=[recipe_tool],
    instructions=INSTRUCTION,
    markdown=True
)

# ------------------------------
# 📁 Download Options
# ------------------------------
def download_as_txt(text):
    st.download_button("📄 Download as TXT", data=text, file_name="recipe.txt", mime="text/plain")

def download_as_md(text):
    st.download_button("📄 Download as Markdown", data=text, file_name="recipe.md", mime="text/markdown")

# ------------------------------
# 🖼️ Streamlit UI
# ------------------------------
st.set_page_config(page_title="RecipeBot Pro 👨‍🍳", layout="centered")
st.markdown("<h1 style='text-align:center;'>🍴 RecipeBot Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Your AI Chef Assistant</p>", unsafe_allow_html=True)
st.markdown("---")

with st.form("input_form"):
    ingredients = st.text_area(
        "🧾 List your ingredients or preferences",
        placeholder="e.g. I have paneer, spinach, and I want something gluten-free.",
    )
    show_sources = st.checkbox("🔍 Show real recipes from the web")
    run = st.form_submit_button("✨ Generate Recipe")

if run:
    if not ingredients.strip():
        st.warning("⚠️ Please provide some ingredients or instructions.")
    else:
        prompts = [
            {"role": "system", "content": INSTRUCTION},
            {"role": "user", "content": ingredients}
        ]

        with st.spinner("👨‍🍳 Cooking up your custom recipe..."):
            result = agent.model.chat(prompts)
            st.markdown(result)
            download_as_txt(result)
            download_as_md(result)

        if show_sources:
            with st.spinner("🌐 Searching real-world recipes..."):
                links = recipe_tool.search(ingredients)

                if isinstance(links, str):
                    st.error(links)
                elif not links:
                    st.info("❗ No real-world results found.")
                else:
                    for item in links:
                        st.markdown("---")
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            if item["image"]:
                                st.image(item["image"], width=120)
                            else:
                                st.text("No Image")
                        with col2:
                            st.markdown(f"### [{item['title']}]({item['url']})")
                            details = f"*{item['author']}* • {item['published']}" if item['author'] or item['published'] else ""
                            st.markdown(details)

st.markdown("<hr><p style='text-align:center; color:gray;'>Made with ❤️ by Parneet (but you own it now 😉)</p>", unsafe_allow_html=True)

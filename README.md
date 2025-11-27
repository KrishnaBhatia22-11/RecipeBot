🚀 RecipeBot – AI-Powered Recipe Generator

A smart AI application built using Google Gemini, Agno AI Agents, Python, and Streamlit.
RecipeBot takes a food item (e.g., "dal makhani") and instantly generates a complete recipe including ingredients, steps, cooking time, and tips — all powered by modern AI tools.

✨ Features

🍽 AI-generated recipes based on user input

🤖 Gemini 2.5-Pro model integration

🧠 Agno Agent-powered prompt processing

⚡ Streamlit UI for fast, interactive usage

🔐 Easy .env based API key management

💡 Modular code design for future expansion

📂 Project Structure
RecipeBot/
│
├── app.py               # Main Streamlit application
├── agent.py             # Agno AI Agent configuration
├── chat.py              # Message structure
├── config.py            # Model configuration settings
├── templates/           # HTML / UI templates (if any)
├── static/              # Images/CSS (optional)
├── requirements.txt     # Dependencies
├── .env                 # API keys (ignored on GitHub)
└── README.md            # This file

🛠 Tech Stack
Technology	Usage
Python	Backend logic
Streamlit	Web Interface
Agno	AI agent processing
Google Gemini API	Recipe generation
dotenv	Environment variable handling
🔧 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/RecipeBot.git
cd RecipeBot

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the environment

Windows (PowerShell):

.\venv\Scripts\activate


macOS / Linux:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Add your API keys

Create a file named .env in the project root:

GOOGLE_API_KEY=your_gemini_key_here
EXA_API_KEY=your_exa_key_if_used


⚠️ Do NOT upload .env to GitHub.

▶️ Running the Project
python -m streamlit run app.py


Then open the link:

http://localhost:8501

💡 How It Works
1. User enters a dish name

Example: "dal makhani"

2. Agno Agent processes the prompt

Formats message

Sends it to Gemini model

3. Gemini generates the recipe

Ingredients

Steps

Tips

Cooking time

4. Streamlit displays the structured output
📸 Screenshots (to add in repo)

You can include:

Home UI

Input example

Generated recipe output

(Upload images to GitHub and attach here.)

🚀 Future Improvements

Add voice input

Add recipe image generation (Gemini Vision)

Add shopping list generator

Save recipe history

Multi-dish meal planner

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Krishna Bhatia
BTech CSE-AIML
Manav Rachna International Institute of Research & Studies

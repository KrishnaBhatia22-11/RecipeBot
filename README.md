🍽️ RecipeBot – AI-Powered Recipe Generator

RecipeBot is an AI-driven application that generates complete cooking recipes based on user input.
It uses Google Gemini, Agno AI Agents, Python, and Streamlit to build a fast and interactive recipe assistant.

Simply enter any dish name (e.g., "dal makhani") and get a detailed recipe instantly!

🚀 Features

AI-generated recipes using Gemini 2.5 Pro

Agno-powered intelligent agent

Clean and interactive Streamlit UI

Modular, scalable code architecture

Secure API key management via .env

Easy to extend with more AI tools or models

📦 Project Structure

RecipeBot/
├── app.py – Main Streamlit application
├── agent.py – Agno AI agent configuration
├── chat.py – Helper for chat/messages
├── config.py – Model configuration
├── templates/ – Optional templates
├── static/ – Optional assets
├── requirements.txt – Dependencies
├── .env – Environment variables
└── README.md – Documentation

🛠️ Technologies Used

Python – Backend logic
Streamlit – Web UI
Google Gemini API – Recipe generation
Agno AI Agent – Prompt processing
dotenv – API key loading
Requests – API calls

⚙️ Installation & Setup
1. Clone the repository

git clone https://github.com/your-username/RecipeBot.git

cd RecipeBot

2. Create a virtual environment

python -m venv venv

3. Activate the environment

Windows (PowerShell):
.\venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Add your API keys

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key
EXA_API_KEY=your_exa_api_key (optional)

Do NOT upload .env to GitHub.

▶️ Running the Application

python -m streamlit run app.py

Open the app at:
http://localhost:8501

💡 How RecipeBot Works

User enters a dish name (e.g., Dal Makhani).

Agno AI Agent formats the prompt.

Gemini processes and generates the recipe.

Streamlit displays ingredients, steps, tips, and more.

🔮 Future Enhancements

Add voice input

Generate shopping lists

Include AI-generated food images

Add meal planner

Add recipe history & user authentication

🤝 Contributing

Contributions are welcome! Open an issue or submit a pull request.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Krishna Bhatia
BTech CSE – AIML
Manav Rachna International Institute of Research & Studies

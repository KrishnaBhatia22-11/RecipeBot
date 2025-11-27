# 🍽️ RecipeBot – AI-Powered Recipe Generator

RecipeBot is an AI-driven application that generates complete cooking recipes based on user input.  
It uses **Google Gemini**, **Agno AI Agents**, **Python**, and **Streamlit** to build a fast and interactive recipe assistant.

Simply enter any dish name (e.g., *"dal makhani"*) and get a detailed recipe instantly!

---

## 🚀 Features

- 🔥 AI-generated recipes using Gemini 2.5 Pro  
- 🤖 Agno-powered intelligent agent  
- ⚡ Clean and interactive Streamlit UI  
- 🧩 Modular, scalable code architecture  
- 🔐 Secure API key management via `.env`  
- 🌱 Easy to extend with more AI tools or models  

---

## 📦 Project Structure

RecipeBot/
│
├── app.py # Main Streamlit application
├── agent.py # Agno AI agent configuration
├── chat.py # Helper methods for chat/messages
├── config.py # Model configuration settings
├── templates/ # HTML templates (optional)
├── static/ # Images/CSS assets (optional)
├── requirements.txt # Python dependencies
├── .env # Environment variables (API keys)
└── README.md # Documentation


---

## 🛠️ Technologies Used

| Technology           | Purpose                           |
|---------------------|------------------------------------|
| **Python**          | Backend logic                      |
| **Streamlit**       | Web UI interface                   |
| **Google Gemini API** | Recipe generation via LLM          |
| **Agno AI Agent**   | Prompt processing + reasoning      |
| **dotenv**          | Load environment variables         |
| **Requests**        | API communication                  |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/RecipeBot.git
cd RecipeBot

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the environment

Windows (PowerShell):

.\venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Add your API keys

Create a file named .env in the project root:

GOOGLE_API_KEY=your_gemini_api_key_here
EXA_API_KEY=your_exa_key_here    # optional


⚠️ Important: Do NOT upload .env to GitHub.

▶️ Running the Application

Use Streamlit to launch the app:

python -m streamlit run app.py


The app will open at:

http://localhost:8501

💡 How RecipeBot Works

User enters a dish name (e.g., "Dal Makhani").

The Agno AI agent processes the prompt.

The request is sent to Google Gemini for recipe generation.

A structured recipe (ingredients, steps, tips, etc.) is returned.

Streamlit displays the result in a clean format.

📸 Screenshots (optional for GitHub)
/screenshots/home.png
/screenshots/recipe_output.png


(Upload images and update links later.)

🔮 Future Enhancements

🗣️ Add voice input

🛒 Generate shopping list automatically

🖼️ Add AI-generated food images (Gemini Vision)

🍽️ Multi-recipe meal planner

📚 Save recipe history / user login

🤝 Contributing

Contributions are welcome!
Feel free to open an issue or submit a pull request.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Krishna Bhatia
BTech CSE – AIML
Manav Rachna International Institute of Research & Studies

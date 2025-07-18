from flask import render_template, request
from agent import generate_recipe_idea, fetch_recipe_links
from config import SYSTEM_PROMPT

def setup_routes(app):
    """
    Sets up the main Flask routes for the web app.
    """

    @app.route("/", methods=["GET", "POST"])
    def index():
        recipe = None
        error = None
        real_recipes = []
        show_real = True  # Show real recipes by default

        if request.method == "POST":
            user_input = request.form.get("ingredients", "").strip()

            if not user_input:
                error = "⚠️ Please enter some ingredients or preferences."
            else:
                try:
                    # Generate AI-based recipe text from user input
                    recipe = generate_recipe_idea(user_input)

                    # Fetch real recipes from Exa API
                    real_recipes = fetch_recipe_links(user_input)

                except Exception as e:
                    error = f"❌ AI Service Error: {e}"

        # Render index.html template with all variables
        return render_template(
            "index.html",
            recipe=recipe,
            error=error,
            real_recipes=real_recipes,
            show_real=show_real
        )

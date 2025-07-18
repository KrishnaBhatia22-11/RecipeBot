from flask import Flask, request, send_file
import io
from ui import setup_routes  # Custom UI setup from ui.py

# -----------------------------------
# Initialize Flask app
# -----------------------------------
app = Flask(__name__)

# Attach all frontend routes (index, form, etc.)
setup_routes(app)

# -----------------------------------
# Route: Download recipe as TXT
# -----------------------------------
@app.post("/download/txt")
def download_txt():
    recipe_text = request.form.get("recipe_text", "")
    return send_file(
        io.BytesIO(recipe_text.encode("utf-8")),
        mimetype="text/plain",
        as_attachment=True,
        download_name="recipe.txt"
    )

# -----------------------------------
# Route: Download recipe as Markdown
# -----------------------------------
@app.post("/download/md")
def download_md():
    recipe_text = request.form.get("recipe_text", "")
    return send_file(
        io.BytesIO(recipe_text.encode("utf-8")),
        mimetype="text/markdown",
        as_attachment=True,
        download_name="recipe.md"
    )

# -----------------------------------
# Run the Flask app (debug mode)
# -----------------------------------
if __name__ == "__main__":
    app.run(debug=True)

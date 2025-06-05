import os
import json
import re
import shutil
from jinja2 import Template
from templates import index_template, category_template, game_template

# Configurable domain name
DOMAIN = "https://example.com"  # Replace with your domain

# This constant is used in the following places:
# 1. In the index_template for the og:image meta tag
# 2. In the category_template for the og:image meta tag
# 3. In the game_template for the og:image meta tag

# Create the games directory if it doesn't exist
os.makedirs("recreate/games", exist_ok=True)
os.makedirs("recreate/assets/icons", exist_ok=True)

# Sanitize filename by replacing invalid characters with underscores
def sanitize_filename(filename):
    # Replace invalid characters with underscores
    sanitized = re.sub(r'[\\/*?:"<>|]', '_', filename)
    return sanitized

# Copy icon to assets folder and return the local path
def copy_icon(icon_url, game_title):
    # Extract the filename from the URL
    icon_filename = os.path.basename(icon_url)
    # Check if the icon exists in the recreate/icons folder
    local_icon_path = f"icons/{icon_filename}"
    if os.path.exists(local_icon_path):
        # Copy the icon to the assets folder
        shutil.copy(local_icon_path, f"recreate/assets/icons/{icon_filename}")
        return f"assets/icons/{icon_filename}"
    else:
        print(f"Warning: Icon {icon_filename} not found in recreate/icons folder. Using remote URL: {icon_url}")
        return icon_url

# Generate the index.html file
def generate_index(games, categories):
    template = Template(index_template)
    # Sort games by is_featured
    games.sort(key=lambda x: (not x.get('is_featured', False), x['title']))
    with open("recreate/index.html", "w") as f:
        f.write(template.render(games=games, categories=categories, domain=DOMAIN))

# Generate category HTML files
def generate_category_pages(games, categories):
    template = Template(category_template)
    os.makedirs("recreate/categories", exist_ok=True)
    for category in categories:
        category_games = [game for game in games if game['categories'] == category]
        # Sort games by is_featured
        category_games.sort(key=lambda x: (not x.get('is_featured', False), x['title']))
        with open(f"recreate/categories/{category.lower()}.html", "w") as f:
            f.write(template.render(games=category_games, categories=categories, category=category, domain=DOMAIN))

# Generate individual game HTML files
def generate_game_pages(games):
    template = Template(game_template)
    for game in games:
        sanitized_title = sanitize_filename(game['title'].replace(' ', '_').lower())
        game['sanitized_title'] = sanitized_title
        filename = f"recreate/games/{sanitized_title}.html"
        with open(filename, "w") as f:
            f.write(template.render(game=game, domain=DOMAIN))

# Main execution
if __name__ == "__main__":
    # Read games from data.json
    try:
        with open("recreate/data.json", "r") as f:
            games = json.load(f)
        # Preprocess: add sanitized_title and local_icon to each game
        for game in games:
            game['sanitized_title'] = sanitize_filename(game['title'].replace(' ', '_').lower())
            game['local_icon'] = copy_icon(game['icon'], game['title'])
        # Extract unique categories
        categories = sorted(list(set(game['categories'] for game in games)))
        generate_index(games, categories)
        generate_category_pages(games, categories)
        generate_game_pages(games)
        print("Static site generated successfully!")
    except FileNotFoundError:
        print("data.json not found. Please run fetch_games.py first.") 
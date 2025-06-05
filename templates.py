# Template for the index page
index_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="keywords" content="School, Learning, Apps, School Website, Learn, Application, Site">
  <meta name="description" content="Learn and have fun!">
  <meta name="language" content="English">
  <meta property="og:image" content="{{ domain }}/assets/img/duck.webp">
  <title>Game Compilation</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f0f0f0;
      display: flex;
    }
    .sidebar {
      width: 200px;
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      margin-right: 20px;
      position: fixed;
      height: 100vh;
      overflow-y: auto;
    }
    .sidebar h2 {
      margin-top: 0;
      color: #333;
    }
    .sidebar ul {
      list-style: none;
      padding: 0;
    }
    .sidebar li {
      margin: 10px 0;
    }
    .sidebar a {
      text-decoration: none;
      color: #333;
      font-weight: bold;
    }
    .sidebar a:hover {
      color: #007bff;
    }
    .content {
      flex: 1;
      margin-left: 220px;
    }
    h1 {
      text-align: center;
      color: #333;
    }
    .search-container {
      text-align: center;
      margin-bottom: 20px;
    }
    .search-container input {
      padding: 10px;
      width: 300px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .games-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
      padding: 20px;
    }
    .game-card {
      background: white;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      overflow: hidden;
      transition: transform 0.3s;
    }
    .game-card:hover {
      transform: translateY(-5px);
    }
    .game-card img {
      width: 100%;
      height: 150px;
      object-fit: cover;
    }
    .game-card h2 {
      padding: 10px;
      margin: 0;
      font-size: 1.2em;
      text-align: center;
    }
    .game-card a {
      text-decoration: none;
      color: inherit;
    }
  </style>
</head>
<body>
  <div class="sidebar">
    <h2>Categories</h2>
    <ul>
      <li><a href="index.html">All</a></li>
      {% for category in categories %}
      <li><a href="categories/{{ category.lower() }}.html">{{ category }}</a></li>
      {% endfor %}
    </ul>
  </div>
  <div class="content">
    <h1>Game Compilation</h1>
    <div class="search-container">
      <input type="text" id="searchInput" placeholder="Search games..." onkeyup="searchGames()">
    </div>
    <div class="games-grid" id="gamesGrid">
      {% for game in games %}
      <div class="game-card">
        <a href="games/{{ game.sanitized_title }}.html">
          <img src="{{ game.local_icon }}" alt="{{ game.title }}">
          <h2>{{ game.title }}</h2>
        </a>
      </div>
      {% endfor %}
    </div>
  </div>
  <script>
    function searchGames() {
      const input = document.getElementById('searchInput');
      const filter = input.value.toUpperCase();
      const gamesGrid = document.getElementById('gamesGrid');
      const gameCards = gamesGrid.getElementsByClassName('game-card');

      for (let i = 0; i < gameCards.length; i++) {
        const title = gameCards[i].getElementsByTagName('h2')[0].innerText;
        if (title.toUpperCase().indexOf(filter) > -1) {
          gameCards[i].style.display = "";
        } else {
          gameCards[i].style.display = "none";
        }
      }
    }
  </script>
</body>
</html>
"""

# Template for category pages
category_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="keywords" content="School, Learning, Apps, School Website, Learn, Application, Site">
  <meta name="description" content="Learn and have fun!">
  <meta name="language" content="English">
  <meta property="og:image" content="{{ domain }}/assets/img/duck.webp">
  <title>{{ category }} Games</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f0f0f0;
      display: flex;
    }
    .sidebar {
      width: 200px;
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      margin-right: 20px;
      position: fixed;
      height: 100vh;
      overflow-y: auto;
    }
    .sidebar h2 {
      margin-top: 0;
      color: #333;
    }
    .sidebar ul {
      list-style: none;
      padding: 0;
    }
    .sidebar li {
      margin: 10px 0;
    }
    .sidebar a {
      text-decoration: none;
      color: #333;
      font-weight: bold;
    }
    .sidebar a:hover {
      color: #007bff;
    }
    .content {
      flex: 1;
      margin-left: 220px;
    }
    h1 {
      text-align: center;
      color: #333;
    }
    .search-container {
      text-align: center;
      margin-bottom: 20px;
    }
    .search-container input {
      padding: 10px;
      width: 300px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .games-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
      padding: 20px;
    }
    .game-card {
      background: white;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      overflow: hidden;
      transition: transform 0.3s;
    }
    .game-card:hover {
      transform: translateY(-5px);
    }
    .game-card img {
      width: 100%;
      height: 150px;
      object-fit: cover;
    }
    .game-card h2 {
      padding: 10px;
      margin: 0;
      font-size: 1.2em;
      text-align: center;
    }
    .game-card a {
      text-decoration: none;
      color: inherit;
    }
  </style>
</head>
<body>
  <div class="sidebar">
    <h2>Categories</h2>
    <ul>
      <li><a href="../index.html">All</a></li>
      {% for cat in categories %}
      <li><a href="{{ cat.lower() }}.html">{{ cat }}</a></li>
      {% endfor %}
    </ul>
  </div>
  <div class="content">
    <h1>{{ category }} Games</h1>
    <div class="search-container">
      <input type="text" id="searchInput" placeholder="Search games..." onkeyup="searchGames()">
    </div>
    <div class="games-grid" id="gamesGrid">
      {% for game in games %}
      <div class="game-card">
        <a href="../games/{{ game.sanitized_title }}.html">
          <img src="{% if game.local_icon.startswith('http') %}{{ game.local_icon }}{% else %}../{{ game.local_icon }}{% endif %}" alt="{{ game.title }}">
          <h2>{{ game.title }}</h2>
        </a>
      </div>
      {% endfor %}
    </div>
  </div>
  <script>
    function searchGames() {
      const input = document.getElementById('searchInput');
      const filter = input.value.toUpperCase();
      const gamesGrid = document.getElementById('gamesGrid');
      const gameCards = gamesGrid.getElementsByClassName('game-card');

      for (let i = 0; i < gameCards.length; i++) {
        const title = gameCards[i].getElementsByTagName('h2')[0].innerText;
        if (title.toUpperCase().indexOf(filter) > -1) {
          gameCards[i].style.display = "";
        } else {
          gameCards[i].style.display = "none";
        }
      }
    }
  </script>
</body>
</html>
"""

# Template for individual game pages
game_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="keywords" content="School, Learning, Apps, School Website, Learn, Application, Site">
  <meta name="description" content="Learn and have fun!">
  <meta name="language" content="English">
  <meta property="og:image" content="{{ domain }}/assets/img/duck.webp">
  <title>{{ game.title }}</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f0f0f0;
    }
    .game-container {
      max-width: 800px;
      margin: 0 auto;
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    h1 {
      text-align: center;
      color: #333;
    }
    iframe {
      width: 100%;
      height: 600px;
      border: none;
      border-radius: 8px;
      frameborder: 0;
      title: "Full-width iframe";
    }
  </style>
</head>
<body>
  <div class="game-container">
    <h1>{{ game.title }}</h1>
    <iframe src="{{ game.link }}" allowfullscreen frameborder="0" title="Full-width iframe"></iframe>
  </div>
</body>
</html>
""" 
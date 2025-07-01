# Snake-Water-Gun Web Game

This is a simple web-based version of the classic Snake-Water-Gun game, built using Python (Flask) for the backend and HTML + JavaScript for the frontend.

---

## Features

- Play Snake-Water-Gun against the computer
- Simple and clean web interface
- Random computer moves every round
- Built with Flask (Python) and vanilla JavaScript

---

## Project Structure
```
snake_water_gun/
├── main.py # Flask backend with game logic
└── templates/
└── index.html # Frontend interface
```
yaml
Copy
Edit

---

## How to Run Locally

### 1. Clone or download the repository

```bash
git clone <your-repo-url>
cd snake_water_gun
```

2. Install Flask (if not already installed)
```bash
Copy
Edit
pip install flask
```
4. Run the application
```bash
Copy
Edit
python main.py
```
5. Open in your browser
Visit the following URL:
```
cpp
Copy
Edit
http://127.0.0.1:5000
```
How to Play
Select Snake, Water, or Gun from the dropdown.

Click the "Play" button.

The computer randomly selects a move.

The result (win/lose/draw) is displayed on the page.

Game Rules
Snake drinks Water → Snake wins

Water drowns Gun → Water wins

Gun kills Snake → Gun wins

Same choice → Draw

Technologies Used
Python 3

Flask

HTML

CSS

JavaScript













from flask import render_template


base_variables = {
    "page": {
        "base_title": "cafe",
        "lang": 'en-US',
        "title": 'Cafe'
    },

    "links": ["INDEX","HOME", "ABOUT", "MENU", "TEAM"]
}

def index():
    data = base_variables
    data['page']['title'] = "index page !"
    return render_template("index.html", data=data)

def home():
    data = base_variables
    data['page']['title'] = "home page !"
    return render_template("home.html", data=data)
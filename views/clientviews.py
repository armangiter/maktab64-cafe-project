from flask import render_template,request
from models import *
from models import cashier, category, menu_items, order_item, orders, table, reciepts


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

def about():
    data = base_variables
    data['page']['title'] = "About page !"
    return render_template("about.html", data=data)

def menu():
    if request.method == 'GET':
        category_dict = category.CategoryModels.all_categories()
        menu_dict = menu_items.MenuItems.all_menu_item()
        data = base_variables
        data['page']['title'] = "menu page !"
        return render_template('menupage', category_dict=category_dict, menu_dict=menu_dict,
                               data=data)
    else:
        json_data = request.get_json()
        if json_data['action'] == "add":
            menu_items.MenuItems(name=json_data['name'], price=json_data['price'], category=json_data['category'],
                                discount=json_data['discount'],serv_time=json_data['serv_time'], st_cooking_time=json_data['st_cooking_time'])
        elif json_data['action'] == 'delete':
            menu_items.MenuItems.delete_item(json_data['id'])


def team():
    data = base_variables
    data['page']['title'] = "team page !"
    return render_template("team.html", data=data)
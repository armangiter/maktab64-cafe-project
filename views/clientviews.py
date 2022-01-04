from flask import render_template, request
from models import cashier, category, menu_items, order_item, orders, table, reciepts

base_variables = {
    "page": {
        "base_title": "cafe",
        "lang": 'en-US',
        "title": 'Cafe'
    },

    "links": ["INDEX", "HOME", "ABOUT", "MENU", "TEAM"]
}


def home():
    if request.method == 'GET':
        data = base_variables
        data['page']['title'] = "Home page !"
        return render_template('home.html', data=data)


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
        return render_template('menu.html', category_dict=category_dict, menu_dict=menu_dict,
                               data=data)


def team():
    data = base_variables
    data['page']['title'] = "team page !"
    return render_template("team.html", data=data)


def order():
    if request.method == "POST":
        menu_dict = list(menu_items.MenuItems.all_menu_item().keys())
        req = request.form.get
        for i in menu_dict:
            if req(i) != 0:
                orders.Order(req('table'), req(str(i)))
                order_dict = list(orders.Order.all_orders().keys())
                o = order_dict[len(order_dict) - 1]
                order_item.OrderItem(o, i)
        return render_template('home.html')

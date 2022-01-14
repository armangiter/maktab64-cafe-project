from flask import render_template, request, render_template_string, jsonify
from models import cashier, category, menu_items, order_item, orders, table, reciepts

base_variables = {
    "page": {
        "base_title": "cafe",
        "lang": 'en-US',
        "title": 'Cafe'
    },

    "links": ["INDEX", "HOME", "ABOUT", "MENU", "TEAM"]
}


def index():
    if request.method == 'GET':
        return render_template('Customer/index.html')


def home():
    if request.method == 'GET':
        data = base_variables
        data['page']['title'] = "Home page !"
        return jsonify({'data': render_template('Customer/home.html', data=data)})


def about():
    if request.method == 'GET':
        data = base_variables
        data['page']['title'] = "About page !"
        return jsonify({'data': render_template("Customer/about.html", data=data)})


def menu():
    if request.method == 'GET':
        category_dict = category.CategoryModels.read_all()
        menu_dict = menu_items.MenuItems.read_all()
        data = base_variables
        data['page']['title'] = "menu page !"
        return jsonify({'data': render_template('Customer/menu.html', category_dict=category_dict, menu_dict=menu_dict,
                                                data=data)})


def team():
    if request.method == "GET":
        data = base_variables
        data['page']['title'] = "team page !"
        return jsonify({'data': render_template("Customer/team.html", data=data)})


def order():
    if request.method == "POST":
        menu_dict = list(menu_items.MenuItems.read_all().keys())
        req = request.form.get
        for i in menu_dict:
            if req(i) != 0:
                orders.Order(req('table'), req(str(i)))
                order_dict = list(orders.Order.read_all().keys())
                o = order_dict[len(order_dict) - 1]
                order_item.OrderItem(o, i)
        return render_template('Customer/index.html')


def all_():
    if request.method == 'GET':
        category_dict = category.CategoryModels.read_all()
        menu_dict = menu_items.MenuItems.read_all()
        return jsonify({'data': render_template('Customer/all.html', category_dict=category_dict, menu_dict=menu_dict)})


def cafe():
    if request.method == 'GET':
        category_dict = category.CategoryModels.read_all()
        menu_dict = menu_items.MenuItems.read_all()
        return jsonify(
            {'data': render_template('Customer/cafe.html', category_dict=category_dict, menu_dict=menu_dict)})


def food():
    if request.method == 'GET':
        category_dict = category.CategoryModels.read_all()
        menu_dict = menu_items.MenuItems.read_all()
        return jsonify(
            {'data': render_template('Customer/food.html', category_dict=category_dict, menu_dict=menu_dict)})


def breakfast():
    if request.method == 'GET':
        category_dict = category.CategoryModels.read_all()
        menu_dict = menu_items.MenuItems.read_all()
        return jsonify(
            {'data': render_template('Customer/breakfast.html', category_dict=category_dict, menu_dict=menu_dict)})

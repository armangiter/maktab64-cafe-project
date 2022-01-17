from flask import render_template, request, render_template_string, jsonify, make_response
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
    if request.method == "GET":
        co = request.cookies.to_dict()
        table_id = co['table']
        cart_dict = {}
        total_price = 0
        i = 1
        for k in co:
            if k != "table":
                orders.Order(table_id, co[k])
                order_id = max(orders.Order.read_all().keys())
                order_item.OrderItem(order_id, k)
                i += 1
                item = menu_items.MenuItems.read(f'{k}')
                total_price += item['price'] * int(co[k])
                cart_dict[f'{i}'] = item
        reciepts.Receipt(table_id, total_price, total_price)
        return render_template('Customer/checkout.html', total_price=total_price)


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


def cart():
    if request.method == "GET":
        table_dict = table.TableModels.read_all()
        co = request.cookies.to_dict()
        cart_dict = {}
        total_price = 0
        total_quantity = 0
        i = 1
        for k in co:
            if co != "table":
                i += 1
                item = menu_items.MenuItems.read(f'{k}')
                item['quantity'] = int(co[k])
                total_quantity += int(co[k])
                item['t_price'] = item['price'] * int(co[k])
                total_price += item['t_price']
                cart_dict[f'{i}'] = item
        return jsonify(
            {'data': render_template('Customer/cart_control.html', cart_dict=cart_dict, total_price=total_price,
                                     total_quantity=total_quantity, table_dict=table_dict)})

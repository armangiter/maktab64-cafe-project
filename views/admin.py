from models import *
from flask import Flask
from flask import redirect, url_for, request, render_template, escape, render_template_string, Response, jsonify
from models import cashier, category, menu_items, order_item, orders, table, reciepts
import json


def login():
    print("login")
    if request.method == "POST":
        cashier_dict = cashier.CashierModels.read_all()
        for c in cashier_dict:
            if escape(request.form.get('phone')) == cashier_dict[c]['phone'] and \
                    escape(request.form.get('password')) == cashier_dict[c]['password']:
                return render_template('cashier/adminpage2.html', data=cashier_dict[c])
    elif request.method == 'GET':
        return render_template('cashier/login.html')


def register():
    if request.method == 'GET':
        return render_template('cashier/login.html')
    elif request.method == 'POST':
        cashier.CashierModels(escape(request.form.get('firstname')), escape(request.form.get('lastname')),
                              escape(request.form.get('phone')),
                              escape(request.form.get('password')), escape(request.form.get('email')))
        return render_template('cashier/login.html')
    return None


def admin_page():
    if request.method == 'GET':
        category_dict = category.CategoryModels.read_all()
        menu_dict = menu_items.MenuItems.read_all()
        order_dict = orders.Order.read_all()
        order_item_dict = order_item.OrderItem.read_all()
        table_dict = table.TableModels.read_all()
        receipts_dict = reciepts.Receipt.read_all()
        return render_template('cashier/adminpage2.html', category_dict=category_dict, menu_dict=menu_dict,
                               order_dict=order_dict, order_item_dict=order_item_dict, table_dict=table_dict,
                               receipts_dict=receipts_dict, )
    return None


def order():
    if request.method == "GET":
        menu_dict = menu_items.MenuItems.read_all()
        order_dict = orders.Order.read_all()
        order_item_dict = order_item.OrderItem.read_all()
        return jsonify({'data': render_template('cashier/orders.html', menu_dict=menu_dict, order_dict=order_dict,
                                                order_item_dict=order_item_dict)})
    elif request.method == 'POST':
        value_status = request.form['status']
        id_order = request.form['id_order']
        orders.Order.update('status', id_order, value_status)
        return render_template('cashier/orders.html')


def receipt():
    if request.method == 'GET':
        receipts_dict = reciepts.Receipt.read_all()
        return jsonify({'data': render_template('cashier/recipts.html', receipts_dict=receipts_dict)})
    return None


def menu_item():
    if request.method == 'GET':
        menu_dict = menu_items.MenuItems.read_all()
        return jsonify({'data': render_template('cashier/menuitems.html', menu_dict=menu_dict)})
    elif request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        description = request.form['description']
        category = request.form['category']
        discount = request.form['discount']
        serv_time = request.form['serv_time']
        st_cooking_time = request.form['st_cooking_time']
        menu_items.MenuItems(name, price, image, description, category, discount, serv_time, st_cooking_time)
        menu_dict = menu_items.MenuItems.read_all()
        return jsonify({'data': render_template('cashier/menuitems.html', menu_dict=menu_dict)})
    elif request.method == 'DELETE':
        id_delete = request.form["id_delete"]
        menu_items.MenuItems.delete(id_delete)
        return jsonify({'data': render_template('cashier/menuitems.html')})


def categories():
    if request.method == 'POST':
        title = request.form['title']
        root = request.form['root']
        category.CategoryModels(title, root)
        category_dict = category.CategoryModels.read_all()
        return jsonify({'data': render_template('cashier/category.html', category_dict=category_dict)})
    elif request.method == 'GET':
        category_dict = category.CategoryModels.read_all()
        return jsonify({'data': render_template('cashier/category.html', category_dict=category_dict)})
    elif request.method == 'DELETE':
        id_delete = request.form["id_delete"]
        category.CategoryModels.delete(id_delete)
        category_dict = category.CategoryModels.read_all()
        return jsonify({'data': render_template('cashier/category.html', category_dict=category_dict)})


def about():
    if request.method == 'GET':
        return render_template('Customer/about.html')


def team():
    if request.method == "GET":
        return render_template('Customer/team.html')


def tables():
    if request.method == 'GET':
        table_dict = table.TableModels.read_all()
        orders_dict = orders.Order.read_all()
        return jsonify({'data': render_template('cashier/table.html', table_dict=table_dict, orders=orders_dict)})


def dashboard():
    if request.method == 'GET':
        reciept_dict = reciepts.Receipt.read_all()
        item_order = order_item.OrderItem.read_all()
        menu_dict = menu_items.MenuItems.read_all()
        order_dict = orders.Order.read_all()
        top_items = {}
        top_five = []
        for i in item_order:
            name = menu_dict[item_order[i]['item_id']]['name']
            if i in top_items:
                ...
            top_items[name] = int(order_dict[item_order[i]['order_id']]['number'])

        for r in reciept_dict:
            top_five.append(reciept_dict[r]['total_price'])
        top_five.sort()
        top_five = top_five[-1:-6:-1]
        return render_template('cashier/dashbord.html', top_five=top_five)

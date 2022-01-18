from models import *
from flask import Flask
from flask import redirect, url_for, request, render_template, escape, render_template_string, Response, jsonify
from models import cashier, category, menu_items, order_item, orders, table, reciepts
import json
from collections import Counter


def login():
    reciept_dict = reciepts.Receipt.read_all()
    item_order = order_item.OrderItem.read_all()
    menu_dict = menu_items.MenuItems.read_all()
    order_dict = orders.Order.read_all()
    top_items = {}
    top_five = []
    total_income = 0
    for i in item_order:
        name = menu_dict[item_order[i]['item_id']]['name']
        if name in top_items:
            top_items[name] += int(order_dict[item_order[i]['order_id']]['number'])
        else:
            top_items[name] = int(order_dict[item_order[i]['order_id']]['number'])
    top_items = dict(Counter(top_items).most_common(5))
    for r in reciept_dict:
        top_five.append(reciept_dict[r]['total_price'])
        total_income += reciept_dict[r]['final_price']
    top_five.sort()
    top_five = top_five[-1:-6:-1]
    top_items_v = list(top_items.values())
    top_items_k = list(top_items.keys())
    if request.method == "POST":
        cashier_dict = cashier.CashierModels.read_all()
        for c in cashier_dict:
            if escape(request.form.get('phone')) == cashier_dict[c]['phone'] and \
                    escape(request.form.get('password')) == cashier_dict[c]['password']:
                return render_template('cashier/adminpage2.html', data=cashier_dict[c], top_five=top_five,
                                       top_items_v=top_items_v,
                                       top_items_k=top_items_k, total_income=total_income)
        return render_template('cashier/login.html', wrong='wrong phone or pass')
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
        return render_template('cashier/adminpage2.html')
    return None


def order():
    print('order1')
    if request.method == "GET":
        menu_dict = menu_items.MenuItems.read_all()
        order_dict = orders.Order.read_all()
        order_item_dict = order_item.OrderItem.read_all()
        return jsonify({'data': render_template('cashier/orders.html', menu_dict=menu_dict, order_dict=order_dict,
                                                order_item_dict=order_item_dict)})
    elif request.method == 'POST':
        print('order')
        value_status = request.form['status']
        id_order = request.form['id_order']
        print(value_status)
        orders.Order.update('status', id_order, value_status)
        order_dict = orders.Order.read_all()
        return jsonify({'data': render_template('cashier/orders.html', order_dict=order_dict)})


def receipt():
    if request.method == 'POST':
        status = 'Paid'
        table_id = request.form['table_id']
        reciepts.Receipt.update('status', table_id, status)
        receipts_dict = reciepts.Receipt.read_all()
        return jsonify({'data': render_template('cashier/recipts.html', receipts_dict=receipts_dict)})
    elif request.method == 'GET':
        receipts_dict = reciepts.Receipt.read_all()
        return jsonify({'data': render_template('cashier/recipts.html', receipts_dict=receipts_dict)})


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
        menu_dict = menu_items.MenuItems.read_all()
        return jsonify({'data': render_template('cashier/menuitems.html', menu_dict=menu_dict)})


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
        total_income = 0
        for i in item_order:
            name = menu_dict[item_order[i]['item_id']]['name']
            if name in top_items:
                top_items[name] += int(order_dict[item_order[i]['order_id']]['number'])
            else:
                top_items[name] = int(order_dict[item_order[i]['order_id']]['number'])
        top_items = dict(Counter(top_items).most_common(5))
        for r in reciept_dict:
            top_five.append(reciept_dict[r]['total_price'])
            total_income += reciept_dict[r]['final_price']
        top_five.sort()
        top_five = top_five[-1:-6:-1]
        top_items_v = list(top_items.values())
        top_items_k = list(top_items.keys())
        return render_template('cashier/dashbord.html', top_five=top_five, top_items_v=top_items_v,
                               top_items_k=top_items_k, total_income=total_income)

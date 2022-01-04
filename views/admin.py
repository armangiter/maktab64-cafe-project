from models import *
from flask import Flask
from flask import redirect, url_for, request, render_template, escape, render_template_string, Response
from models import cashier, category, menu_items, order_item, orders, table, reciepts


def login():
    if request.method == "POST":
        cashier_dict = cashier.CashierModels.all_cashiers()
        for c in cashier_dict:
            if escape(request.form.get('phone')) == cashier_dict[c]['phone'] and \
                    escape(request.form.get('password')) == cashier_dict[c]['password']:
                return render_template('adminpage2.html', data=c)
    elif request.method == 'GET':
        return render_template('login.html')


def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        cashier.CashierModels(escape(request.form.get('firstname')), escape(request.form.get('lastname')),
                              escape(request.form.get('phone')),
                              escape(request.form.get('password')), escape(request.form.get('email')))
        return render_template('login.html')
    return None


def admin_page():
    if request.method == 'GET':
        category_dict = category.CategoryModels.all_categories()
        menu_dict = menu_items.MenuItems.all_menu_item()
        order_dict = orders.Order.all_orders()
        order_item_dict = order_item.OrderItem.all_order_items()
        table_dict = table.TableModels.all_table()
        receipts_dict = reciepts.Receipts.all_receipts()
        return render_template('adminpage2.html', category_dict=category_dict, menu_dict=menu_dict,
                               order_dict=order_dict,
                               order_item_dict=order_item_dict, table_dict=table_dict, receipts_dict=receipts_dict)
    return None


def order():
    if request.method == "GET":
        menu_dict = menu_items.MenuItems.all_menu_item()
        order_dict = orders.Order.all_orders()
        order_item_dict = order_item.OrderItem.all_order_items()
        return render_template('orders.html', menu_dict=menu_dict, order_dict=order_dict, order_item_dict=order_item_dict)
    return None


def receipt():
    if request.method == 'GET':
        receipts_dict = reciepts.Receipts.all_receipts()
        return render_template('recipts.html', receipts_dict=receipts_dict)
    return None


def menu_item():
    if request.method == 'POST':
        req = request.form.get
        menu_items.MenuItems(req('name'), req('price'), req('image'), req('description'), req('category'))
        return render_template('menuitems.html')
    elif request.method == 'GET':
        return render_template('menuitems.html')


def categories():
    if request.method == 'GET':
        category_dict = category.CategoryModels.all_categories()
        return render_template('category.html', category_dict=category_dict)
    elif request.method == 'POST':
        req = request.form.get
        category.CategoryModels(req('title'), req('root'))
        return render_template('category.html')


def about():
    if request.method == 'GET':
        return render_template('about.html')


def team():
    if request.method == "GET":
        return render_template('team.html')

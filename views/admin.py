from models import *
from flask import Flask
from flask import redirect, url_for, request, render_template, escape, render_template_string, Response
from models import cashier, category, menu_items, order_item, orders, table, reciepts


def login():
    if request.method == "POST":
        cashier_dict = cashier.CashierModels.all_cashiers()
        for c in cashier_dict:
            if escape(request.form.get('phone')) == c['phone'] and \
                    escape(request.form.get('password')) == c['password']:
                return render_template('admin_page', data=c)
    elif request.method == 'GET':
        return render_template('login')


def register():
    if request.method == 'GET':
        return render_template('register')
    elif request.method == 'POST':
        cashier.CashierModels(escape(request.form.get('firstname')), escape(request.form.get('lastname')),
                              escape(request.form.get('phone')),
                              escape(request.form.get('password')), escape(request.form.get('email')))
        return render_template('login')
    return None


def admin_page():
    if request.method == 'GET':
        category_dict = category.CategoryModels.all_categories()
        menu_dict = menu_items.MenuItems.all_menu_item()
        order_dict = orders.Order.all_orders()
        order_item_dict = order_item.OrderItem.all_order_items()
        table_dict = table.TableModels.all_table()
        receipts_dict = reciepts.Receipts.all_receipts()
        return render_template('admin_page', category_dict=category_dict, menu_dict=menu_dict, order_dict=order_dict,
                               order_item_dict=order_item_dict, table_dict=table_dict, receipts_dict=receipts_dict)
    return None


def order():
    if request.method == "GET":
        menu_dict = menu_items.MenuItems.all_menu_item()
        order_dict = orders.Order.all_orders()
        order_item_dict = order_item.OrderItem.all_order_items()
        return render_template('orders', menu_dict=menu_dict, order_dict=order_dict, order_item_dict=order_item_dict)
    return None


def receipt():
    if request.method == 'GET':
        receipts_dict = reciepts.Receipts.all_receipts()
        return render_template('receipt', receipts_dict=receipts_dict)
    return None


def menu_item():
    if request.method == 'POST':
        req = request.form.get
        menu_items.MenuItems(req('name'), req('price'), req('category'),)

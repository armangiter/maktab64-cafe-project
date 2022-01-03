from models import *
from flask import Flask
from flask import redirect, url_for, request, render_template, escape, render_template_string, Response
from models import cashier, category, menu_items, order_item, orders, table, reciepts


def login():
    if request.method == "POST":
        cashier_dict = cashier.CashierModels.all_cashiers()
        for c in cashier_dict:
            if request.form.get('phone') == c['phone'] and request.form.get('password') == c['password']:
                return render_template('admin_page', data=c)
    elif request.method == 'GET':
        return render_template('register')


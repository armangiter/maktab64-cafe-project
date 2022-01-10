from flask import Flask
from views import clientviews, admin

app = Flask(__name__)

app.add_url_rule('/', 'index', clientviews.home, methods=['GET'])
app.add_url_rule('/menu', 'menu', clientviews.menu)
app.add_url_rule('/menuitem', 'menuitem', admin.menu_item, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', admin.register, methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', admin.login, methods=['GET', 'POST'])
app.add_url_rule('/adminpage', 'adminpage', admin.admin_page, methods=['GET', 'POST'])
app.add_url_rule('/orders', 'orders', admin.order, methods=['GET', 'POST'])
app.add_url_rule('/category', 'category', admin.categories, methods=['GET', 'POST'])
app.add_url_rule('/about', 'about', admin.about, methods=['GET'])
app.add_url_rule('/team', 'team', admin.team, methods=['GET'])
app.add_url_rule('/order', 'order', admin.order, methods=['GET', 'POST'])
app.add_url_rule('/receipt', 'receipt', admin.receipt)
app.add_url_rule('/creat_order', 'creat_order', clientviews.order, methods=['GET', 'POST'])
app.add_url_rule('/all', 'all', clientviews.all_, methods=['POST', 'GET'])
app.add_url_rule('/home_main')
if __name__ == '__main__':
    app.run()

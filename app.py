from flask import Flask
from views import clientviews, admin

app = Flask(__name__)

app.add_url_rule('/', 'index', clientviews.index, methods=['GET'])
app.add_url_rule('/home', 'home', clientviews.home, methods=['GET', 'POST'])
app.add_url_rule('/menu', 'menu', clientviews.menu)
app.add_url_rule('/menuitem', 'menuitem', admin.menu_item, methods=['GET', 'POST', 'DELETE'])
app.add_url_rule('/register', 'register', admin.register, methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', admin.login, methods=['GET', 'POST'])
app.add_url_rule('/adminpage', 'adminpage', admin.admin_page, methods=['GET', 'POST'])
app.add_url_rule('/orders', 'orders', admin.order, methods=['GET', 'POST'])
app.add_url_rule('/category', 'category', admin.categories, methods=['GET', 'POST', 'DELETE'])
app.add_url_rule('/about', 'about', clientviews.about, methods=['GET'])
app.add_url_rule('/team', 'team', clientviews.team, methods=['GET'])
app.add_url_rule('/order', 'order', clientviews.order, methods=['GET', 'POST'])
app.add_url_rule('/receipt', 'receipt', admin.receipt, methods=["GET", 'POST'])
app.add_url_rule('/creat_order', 'creat_order', clientviews.order, methods=['GET', 'POST'])
app.add_url_rule('/all', 'all', clientviews.all_, methods=['POST', 'GET'])
app.add_url_rule('/cafe', 'cafe', clientviews.cafe, methods=['POST', 'GET'])
app.add_url_rule('/food', 'food', clientviews.food, methods=['POST', 'GET'])
app.add_url_rule('/breakfast', 'breakfast', clientviews.breakfast, methods=['POST', 'GET'])
app.add_url_rule('/table', 'table', admin.tables, methods=['GET', 'POST'])
app.add_url_rule('/cart', 'cart', clientviews.cart, methods=['GET', 'POST'])
app.add_url_rule('/Dashboard', 'Dashboard', admin.dashboard, methods=['GET'])
if __name__ == '__main__':
    app.run()

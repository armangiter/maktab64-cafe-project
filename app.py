from flask import Flask
from views import clientviews, admin

app = Flask(__name__)

app.add_url_rule('/', 'home', clientviews.home, methods=['GET'])
app.add_url_rule('/menu', 'menu', clientviews.menu)
app.add_url_rule('/menuitem', 'menuitem', admin.menu_item, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', admin.register, methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', admin.login, methods=['GET', 'POST'])
app.add_url_rule('/adminpage', 'adminpage', admin.admin_page, methods=['GET', 'POST'])
app.add_url_rule('/orders', 'orders', admin.order, methods=['GET', 'POST'])
if __name__ == '__main__':
    app.run()

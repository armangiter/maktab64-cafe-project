from flask import Flask
from views import clientviews, admin

app = Flask(__name__)

app.add_url_rule('/', 'home', clientviews.home)
if __name__ == '__main__':
    app.run()

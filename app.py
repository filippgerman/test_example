from flask import Flask

from router import order

app = Flask(__name__)
app.register_blueprint(order)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
from flask import render_template
from app import app
from models.order_list import orders

@app.route('/order')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/order/<index>')
def index_count(index):
    index_position = orders[int(index)]
    return render_template('order.html', title='Index', orders=index_position)
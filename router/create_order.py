from flask import Blueprint

from model.order.order import Order
from flask_pydantic import validate

from service.create_order import create_order

order = Blueprint('order', __name__)


@order.route('/order', methods=['POST'])
@validate()
def index(body: Order):
    return create_order(body)

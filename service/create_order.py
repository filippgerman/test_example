from model.order.order import Order


def create_order(order: Order):
    return f"Заказ создан. {order.delivery_date} ожидайте посылку"

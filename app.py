from datetime import date
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def get_all():
    search_query = request.args.get('q', '')
    res = requests.get('https://dummyjson.com/products')
    res_json = res.json()['products']
    if search_query:
        res_json = [product for product in res_json if search_query.lower() in product['title'].lower()]
    return render_template('components/card.html', product_list=res_json)


@app.route('/products_detail')
def get_product_detail():
    pid = request.args.get('id')
    res = requests.get(f"https://dummyjson.com/products/{pid}")
    res_json = res.json()
    return render_template('layout/detail.html', product_detail=res_json)


@app.route('/checkout')
def checkout():
    pid = request.args.get('id')
    res = requests.get(f"https://fakestoreapi.com/products/{pid}")
    res_json = res.json()
    return render_template('layout/confirm_booking.html', product_detail=res_json)


@app.route('/confirm_checkout', methods=['POST'])
def confirm_checkout():
    pid = request.form.get('id')
    res = requests.get(f"https://dummyjson.com/products/{pid}")
    product = res.json()

    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    quantity = request.form.get('quantity')

    if quantity is None or quantity == '':
        quantity = 1
    else:
        quantity = int(quantity)

    total_price = product['price'] * quantity

    msg = (
        "<b>🕵️‍♂️🔍 [ Black Market Order ] 🔍🕵️‍♂️</b>\n"
        "<b>👤 Alias:</b> <code>{name}</code>\n"
        "<b>📞 Contact:</b> <code>{phone}</code>\n"
        "<b>✉️ Email:</b> <code>{email}</code>\n"
        "<b>🏠 Drop Location:</b> <code>{address}</code>\n"
        "<b>📅 Transaction Date:</b> <code>{date}</code>\n"
        "<b>====================</b>\n"
        "<b>💀 Order Details 💀</b>\n"
        "<b>📦 Item:</b> <code>{product_name}</code>\n"
        "<b>🔢 Quantity:</b> <code>{quantity}</code>\n"
        "<b>💲 Unit Price:</b> <code>${price}</code>\n"
        "<b>💰 Total Amount:</b> <code>${total_price}</code>\n"
    ).format(
        name=name,
        phone=phone,
        email=email,
        address=address,
        date=date.today(),
        product_name=product['title'],
        quantity=quantity,
        price=product['price'],
        total_price=total_price
    )

    send_notification(msg)

    return redirect(url_for('get_all'))


def send_notification(msg):
    bot_token = '7445107367:AAHkS9es6Yj_4AAqThoHdk-3cp8qXXdwBW4'
    chat_id = '@ranfabotbot1'

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={requests.utils.quote(msg)}&parse_mode=HTML"
    res = requests.get(url)
    return res


if __name__ == '__main__':
    app.run()

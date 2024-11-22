import random
from flask import Flask,render_template,redirect,request
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,
                      PasswordField,EmailField,validators)

import flask_wtf
import wtforms
from database import *

app=Flask(__name__)
app.config['SECRET_KEY'] = '1212'

@app.route("/")
def main():
    perfumes = select_all()
    return render_template('index.html',perfumes=perfumes)

@app.route("/filtir/",methods=['POST'])
def filtir():

      min_price=  request.form['min']
      max_price = request.form['max']
      perfumes= select_price(min_price,max_price)
      return render_template('products.html',perfumes=perfumes)


@app.route("/products/")
def products():
    perfumes = select_all()
    return render_template('products.html',perfumes=perfumes)

@app.route("/ingradient/<ingradient>/")
def ingradients(ingradient):
        products= select_ingradients(ingradient)
        return render_template('ingradient.html', products=products)


@app.route("/names/",methods=['POST'])
def names():
    # if request.method=='post':
        search=request.form['search']
        print(search)
        perfumes= select_name(search)

        return render_template('products.html', perfumes=perfumes)
    # else:
    #    return redirect('/products/')



@app.route("/categories/<categoria>/",methods=['GET','POST'])
def categories(categoria):
        change = categoria
        if change == 'flowers':
            picture= 'flowers.jpeg'
            products = select_categoria('Квіти')
        elif change == 'fruits':
            picture = 'Designer (2).jpeg'
            products = select_categoria('Фрукти|Ягоди')
        elif change == 'nature':
            picture = 'Designer (28).jpeg'
            products = select_categoria('Природа')
        elif change == 'fall':
            picture = 'Designer (29).jpeg'
            products = select_categoria('Осінь')
        else:
            products = select_all()
        return render_template('categories.html', products=products,picture=picture)


@app.route("/shares/")
def shares():
    perfumes = select_all()
    random_products = random.choice(perfumes)
    price = random_products[-1] - random_products[-1] * 0.2
    return render_template('shares.html',
                           random_products = random_products,price=price)

@app.route("/basket/")
def basket():
    user_products = select_all_basket()
    price = 0
    if user_products:
        for i in user_products:
            price += i[6]
    else:
        price=0
    return render_template('basket.html',
                           user_products=user_products,price=price)

@app.route('/add_to_basket/<int:id>/')
def add_to_basket(id):
    product = select_product(id)
    add_product_basket(categoria=product[1], img=product[2],
                       name=product[3], description=product[4],ingradients=product[5],
                       price=product[6])
    return redirect('/basket/')

@app.route('/delete/<int:id>/')
def delete(id):
    delete_product_basket(id)
    return redirect('/basket/')


@app.route("/details/<int:id>/")
def details(id):
    perfume = select_product(id)
    ingradients=perfume[5].split(', ')
    return render_template('details.html',perfume=perfume,ingradients=ingradients)

@app.route("/add_basket_details/<int:price>/<int:id>/")
def add_basket_details(price,id):
    product = select_product(id)
    add_product_basket(categoria=product[1], img=product[2],
                       name=product[3], description=product[4],ingradients=product[5],
                       price=price)
    return redirect('/basket/')

@app.route("/details/<int:id>/<ml>/")
def details_2(id,ml):
    perfume = select_product(id)
    ingradients=perfume[5].split(', ')
    price=perfume[6]
    if ml== '50':
       price= perfume[6]
    if ml== '100':
       price= perfume[6]*2
    if ml== '200':
       price= perfume[6]*4
    return render_template('details.html',perfume=perfume,ingradients=ingradients,price=price)

@app.route('/price_1/')
def price_1():
    products=select_price_min()
    return render_template('products.html',perfumes=products)

@app.route('/price_2/')
def price_2():
    products=select_price_max()
    return render_template('products.html',perfumes=products)

class BuyForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("ім'я",
                                 validators=[wtforms.validators.DataRequired(),
                                         wtforms.validators.Length(min=1)])
    surname = wtforms.StringField('прізвище',
                                 validators=[wtforms.validators.DataRequired(),
                                         wtforms.validators.Length(min=1)])
    city = wtforms.StringField('місто доставки',
                                 validators=[wtforms.validators.DataRequired(),
                                         wtforms.validators.Length(min=1)])
    address = wtforms.SelectField('Оберіть спосіб доставки')
    pay = wtforms.SelectField('Оберіть спосіб оплати')
    Submit= wtforms.SubmitField('Замовити')

@app.route('/buy/', methods=['GET', 'POST'])
def buy():
    form=BuyForm()
    form.address.choices = [("нова пошта", "нова пошта"), ("укр пошта", "укр пошта"), ("кур'єр", "кур'єр")]
    form.pay.choices = [("готівка", "готівка"), ("картка", "картка")]
    if request.method == "POST":
        return f'Ваше замовлення оформлено!'
    return render_template('buy.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
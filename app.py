

from flask import *
# create a flask application

app = Flask(__name__)
app.secret_key = 'A+4#s_T%P8g0@o?6'
from crypto import verify_password, hash_password


import pymysql
connection = pymysql.connect(host='localhost', user='root',password='',
                                 database='ecom')



@app.route('/')
def home():
    # Connect to database
    # Create a cursor to execute SQL Query
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products limit 4")
    # AFter executing the query above, get all rows
    deals = cursor.fetchall()

    cursor.execute("SELECT * FROM products")
    # AFter executing the query above, get all rows
    brands = cursor.fetchall()

    return render_template('index.html', deals=deals)

# 1. starts here
@app.route('/topdeals')
def index():
    cur = connection.cursor()
    cur.execute("SELECT DISTINCT product_brand FROM products")
    brands = cur.fetchall()

    cur = connection.cursor()
    cur.execute("SELECT DISTINCT product_category FROM products")
    categories = cur.fetchall()

    cur = connection.cursor()
    cur.execute("SELECT DISTINCT color FROM products")
    colors = cur.fetchall()
    # 2. goes to top deals html
    return render_template('topdeals.html', brands=brands, categories=categories, colors = colors)


# 5. fetches all the products and returns a json array
@app.route("/fetchrecords1",methods=["POST","GET"])
def fetchrecords1():
    cur = connection.cursor()
    if request.method == 'POST':
        # category
        name = request.form['insert_string']
        my_result = tuple(map(str, name.split(',')))

        # brand
        name2 = request.form['insert_string2']
        my_result2 = tuple(map(str, name2.split(',')))

        # discount
        name3 = request.form['insert_string3']
        my_result3 = tuple(map(str, name3.split(',')))

        print(my_result)
        print(my_result2)
        print(my_result3)

        if len(name) == 0 and len(name2) == 0 and len(name3) == 0:
            print('here')
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_cost ORDER BY product_id ASC")
            productlist = cur.fetchall()
            print(productlist)
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and not my_result2[0] and not my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand IN %s",
                [my_result])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and  my_result2[0] and not my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and product_category IN %s",
                [my_result,my_result2])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and my_result3[0] and not my_result2[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and color IN %s",
                [my_result, my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and my_result2[0] and  my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and product_category IN %s and color IN %s",
                [my_result, my_result2,my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        #categories
        elif my_result2[0] and not my_result[0] and not my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_category IN %s",
                [my_result2])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result2[0] and  my_result[0] and not my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_category  IN %s and product_brand IN %s",
                [my_result2,my_result])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result2[0] and  my_result3[0] and not my_result[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_category IN %s and color IN %s",
                [my_result2,my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result[0] and my_result2[0] and  my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and product_category IN %s and color IN %s",
                [my_result, my_result2,my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        #color
        elif my_result3[0] and not my_result[0] and not my_result2[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE color IN %s",
                [my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result3[0] and my_result[0] and not my_result2[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE color IN %s and product_brand IN %s",
                [my_result3, my_result])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result3[0] and my_result2[0] and not my_result[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE color IN %s and product_category  IN %s",
                [my_result3, my_result2])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

        elif my_result3[0] and my_result2[0] and my_result3[0]:
            cur = connection.cursor()
            cur.execute(
                "SELECT * FROM products WHERE product_brand  IN %s and product_category IN %s and color IN %s",
                [my_result, my_result2, my_result3])
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})
        else:
            cur.execute("SELECT * FROM products  ORDER BY product_id ASC")
            productlist = cur.fetchall()
            return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

    else:
        cur.execute("SELECT * FROM products ORDER BY product_id ASC")
        productlist = cur.fetchall()
        # this json response productlist mapped to  response.html
        return jsonify({'htmlresponse': render_template('response.html', productlist=productlist)})

@app.route('/single/<product_id>')
def single(product_id):

            # Connect to database
            connection = pymysql.connect(host='localhost', user='root', password='',
                                         database='ecom')

            # Create a cursor to execute SQL Query
            cursor = connection.cursor()
            #below %s is a placeholder o make sure that the id is actually detected
            cursor.execute('SELECT * FROM products WHERE product_id= %s ', (product_id))
            # AFter executing the query above, to get one row
            row = cursor.fetchone()

            # after getting the row forward it to single.html for users to access it
            return render_template('single.html', row=row)


from werkzeug.security import generate_password_hash, check_password_hash
# shopping Cart
@app.route('/add', methods=['POST'])
def add_product_to_cart():
        _quantity = int(request.form['quantity'])
        _code = request.form['code']
        # validate the received values
        if _quantity and _code and request.method == 'POST':
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM products WHERE product_id= %s", _code)
            row = cursor.fetchone()
            #An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together

            itemArray = {row['product_id']: {'product_name': row['product_name'], 'product_id': row['product_id'], 'quantity': _quantity, 'product_cost': row['product_cost'],
                              'image_url': row['image_url'], 'total_price': _quantity * row['product_cost'],
                                             'product_brand': row['product_brand']}}
            print((itemArray))


            all_total_price = 0
            all_total_quantity = 0
            session.modified = True
            #if there is an item already
            if 'cart_item' in session:
                #check if the product you are adding is already there
                if row['product_id'] in session['cart_item']:

                    for key, value in session['cart_item'].items():
                        #check if product is there
                        if row['product_id'] == key:
                            #take the old quantity  which is in session with cart item and key quantity
                            old_quantity = session['cart_item'][key]['quantity']
                            #add it with new quantity to get the total quantity and make it a session
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            #now find the new price with the new total quantity and add it to the session
                            session['cart_item'][key]['total_price'] = total_quantity * row['product_cost']

                else:
                    #a new product added in the cart.Merge the previous to have a new cart item with two products
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)


                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price

            else:
                #if the cart is empty you add the whole item array
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + _quantity
                #get total price by multiplyin the cost and the quantity
                all_total_price = all_total_price + _quantity * row['product_cost']


            #add total quantity and total price to a session
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            return redirect(url_for('.cart'))
        else:
            return 'Error while adding item to cart'




@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/customer_checkout')
def customer_checkout():
    if check_customer():
            return redirect('/cart')
    else:
        return redirect('/customer_login')

# uuid generator
from  order_gen import random_string_generator
#checkout route
@app.route('/proceed_checkout', methods = ['POST','GET'])
def proceed_checkout():
    if check_customer():
        if 'cart_item' in  session:
            if request.method == 'POST':
                mpesa_code = request.form['mpesa_code']
                all_total_price = 0
                all_total_quantity = 0
                # Need to check database******************
                order_code = random_string_generator()
                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    product_id = session['cart_item'][key]['product_id']
                    product_name = session['cart_item'][key]['product_name']
                    product_cost = session['cart_item'][key]['product_cost']

                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
                    print('Individual qqty',individual_quantity)
                    print('Individual price',individual_price)
                    print('product_id', product_id)
                    print('product name', product_name)
                    print('Total qtty', all_total_quantity)
                    print('Total price', all_total_price)
                    print("=================")
                    email = session['tel']
                    #session
                    if not email:
                        flash('Sorry, Error Occured during checkout, Try Again', 'danger')
                        return redirect('/customer_login')
                    elif not individual_price or not individual_quantity or not product_id or not product_name or not all_total_price or not all_total_quantity:
                        flash('Sorry, Error Occured during checkout, Try Again', 'danger')
                        return redirect('/cart')
                    else:
                        try:
                            sql = 'INSERT INTO `orders`(`product_name`, `product_qtty`, `product_cost`, `email`, `order_code`, `mpesa_confirmation`, `individual_total`, `all_total_price`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                            cursor = connection.cursor()
                            cursor.execute(sql, (product_name, individual_quantity, product_cost, email, order_code, mpesa_code, individual_price, all_total_price))
                            connection.commit()

                        except Exception as e:
                            print(e)
                            flash('Sorry, Error occured during checkout, Please try again','danger')
                            return redirect('/cart')

                print('================')
                print('Total qtty', all_total_quantity)
                print('Total price', all_total_price)
                try:
                    sql2 = 'update orders set all_total_price = %s where order_code = %s'
                    cursor = connection.cursor()
                    #it updates all the products to have the same price in the same order in the all total price column
                    cursor.execute(sql2,(all_total_price, order_code))
                    connection.commit()
                    flash('Your Order is Complete, Please check your Orders in Your Profile','success')
                    session.pop('cart_item', None)
                    session.pop('all_total_quantity', None)
                    session.pop('all_total_price', None)
                    print('here')
                    return redirect(url_for('cart'))
                except:
                    flash('Sorry, Error occured during checkout, Please try again','danger')
                    session.pop('cart_item', None)
                    session.pop('all_total_quantity', None)
                    session.pop('all_total_price', None)
                    return redirect('/cart')
            else:
                return redirect('/cart')
        else:
            return redirect('/cart')
    else:
        flash('You must be logged in to Make a Purchase, Please Login', 'warning')
        return redirect('/customer_login')

@app.route('/customer_login', methods = ['POST','GET'])
def customer_login():
    if check_customer():
        return redirect('/')
    else:
        if request.method == "POST":
            phone = request.form['tel']
            password = request.form['password']
            active = 'Yes'
            #check if email exists
            sql = "select * from customers where tel = %s and active = %s"
            cursor = connection.cursor()
            cursor.execute(sql,(phone, active))

            if cursor.rowcount == 0:
                flash("Phone does not Exist", "danger")
                return redirect('/customer_login')
            else:
                row = cursor.fetchone()
                hashed_password = row[4]
                #verify
                status = verify_password(hashed_password, password)
                if status == True:
                    #create session
                    session['tel'] = row[6]
                    session['customer_id'] = row[0]
                    session['fname'] = row[1]
                    session['lname'] = row[2]
                    return redirect('/cart')
                elif status == False:
                   flash("Wrong Credentials","danger")
                   return redirect('/customer_login')
                else:
                    flash("Something went wrong", "danger")
                    return redirect('/customer_login')
        else:
            return render_template('customer_login.html')
import re


@app.route('/logout')
def logout():


    if check_customer():
        session.pop('customer_id')
        session.pop('tel')
        session.pop('fname')
        session.pop('lname')
        session.clear()
        return redirect('/customer_login')
    else:
        session.clear()
        return redirect('/customer_login')


@app.route("/customer_register", methods = ['POST','GET'])
def customer_register():
    if request.method == "POST":
            fname = request.form['fname']
            lname = request.form['lname']

            email = request.form['email']
            password = request.form['password']
            password1 = request.form['password1']

            tel = request.form['tel']


            if password!=password1:
                flash("Password do not match!","warning")
                return redirect('/customer_register')

            elif len(password1) < 8:
                flash("Password MUSt be 8 characters!", "warning")
                return redirect('/customer_register')

            elif not re.search("[0-9]", password):
                flash("Password MUSt have at least a number!", "warning")
                return redirect('/customer_register')

            else:
                cursor = connection.cursor()
                # check if phone already exists
                sql0 = 'select * from customers where tel = %s'
                cursor.execute(sql0, (tel))
                if cursor.rowcount > 0:
                    flash('Phone Already in use', 'warning')
                    return redirect('/customer_register')
                else:
                    sql = "INSERT INTO `customers`( `fname`, `lname`,  `email`, `password`, `tel`) VALUES (%s,%s,%s,%s,%s)"
                    try:
                        cursor.execute(sql, (
                        fname, lname,email, hash_password(password), tel ))
                        connection.commit()
                        # send sms
                        from sms import sending
                        sending(tel, fname)
                        flash('Registration Successfull, Please Login', 'info')
                        return redirect('/customer_login')
                    except:
                        flash('Registration Failed', 'error')
                    return render_template('customer_register.html', )
    else:

        return render_template('customer_register.html', )



def check_customer():
    if 'customer_id' in session:
        return True
    else:
        return False



@app.route('/empty')
def empty_cart():
    try:
        if 'cart_item' in session or 'all_total_quantity' in session or 'all_total_price' in session:
            session.pop('cart_item', None)
            session.pop('all_total_quantity', None)
            session.pop('all_total_price', None)
            return redirect(url_for('.cart'))
        else:
            return redirect(url_for('.cart'))

    except Exception as e:
        print(e)



@app.route('/delete/<string:code>')
def delete_product(code):
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True
        for item in session['cart_item'].items():
            if item[0] == code:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(session['cart_item'][key]['quantity'])
                        individual_price = float(session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break

        if all_total_quantity == 0:
            session.clear()
        else:
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price

        # return redirect('/')
        return redirect(url_for('.cart'))
    except Exception as e:
        print(e)



#set is list in a list


def array_merge( first_array , second_array ):
     if isinstance( first_array , list) and isinstance( second_array , list ):
      return first_array + second_array
     #takes the new product add to the existing and merge to have one array with two products
     elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
      return dict( list( first_array.items() ) + list( second_array.items() ) )
     elif isinstance( first_array , set ) and isinstance( second_array , set ):
      return first_array.union( second_array )
     return False




if __name__ == '__main__':
    app.run(debug=True)
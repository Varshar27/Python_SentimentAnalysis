"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import *
from textblob import TextBlob
from werkzeug.utils import secure_filename
from FlaskWebProject1 import app 
import uuid
import  os
import pymysql



def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.
 
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app.secret_key = 'random string'
UPLOAD_FOLDER = 'FlaskWebProject1/static/uploads'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db =pymysql.connect("localhost","root","","csa")
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    ) 
@app.route('/msg')
def msg():
    """Renders the home page."""
    return render_template(
        'msg.html',
        title='Home Page',
        year=datetime.now().year,
    ) 

@app.route('/thanks', methods=["GET", "POST"])
def thanks():
        return render_template(
        'thank.html')

@app.route('/cart')
def cart():
    if 'email' not in session :
        return  redirect('/login')
    cursor = db.cursor() 
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()

    sql = "SELECT b.prd_price_id,a.name,a.sku,a.image,a.description,b.price,c.country FROM products as a inner join product_price as b on b.prod_id=a.product_id inner join country as c on b.country=c.con_id"
    cursor.execute(sql)
    products = cursor.fetchall()

    return render_template(
        'cart.html',
        title='Cart Page',
        products=products,
        categories=categories,
        category='0',
        year=datetime.now().year,
    ) 

@app.route('/postfeedback', methods=["GET", "POST"])
def postfeedback():
    id = request.form['id'] 
    qus0 = request.form['qus0'] 
    if qus0=='1' :
        qus5 = request.form['qus5']
        qus1=qus2=qus3=0
    else :
        qus1 = request.form['qus1']
        qus2 = request.form['qus2']
        qus3 = request.form['qus3']
        qus5=0
       
    qus4 = request.form['qus4']    
    qus6 = request.form['qus6']
    blob = TextBlob(qus6)
    polarity=0
    for sentence in blob.sentences:
        polarity = sentence.sentiment.polarity
    blob = TextBlob(qus6)
    subjectivity=0
    for sentence in blob.sentences:
        subjectivity = sentence.sentiment.subjectivity
    qry ="insert into customerfeedback (qus1,qus2,qus3,qus4,qus5,qus6,qus7,polarity,confidence,salesid) values ('"+str(qus0)+"','"+str(qus1)+"','"+str(qus2)+"','"+str(qus3)+"','"+str(qus4)+"','"+str(qus5)+"','"+str(qus6)+"','"+str(polarity)+"','"+str(subjectivity)+"','"+str(id)+"')";
    cursor = db.cursor()
    cursor.execute(qry)
    db.commit()
    return render_template(
        'thanks.html') 
@app.route('/postcart', methods=["GET", "POST"])
def postcart():
     
    action = request.form['action']
    if action == 'Search' :
        category = request.form['category']
        cursor = db.cursor() 
        sql = "SELECT * FROM categories"
        cursor.execute(sql)
        categories = cursor.fetchall() 
        where =''
        if category !='':
            where ='where a.category='+str(int(category))
        sql = "SELECT b.prd_price_id,a.name,a.sku,a.image,a.description,b.price,c.country FROM products as a inner join product_price as b on b.prod_id=a.product_id inner join country as c on b.country=c.con_id "+where
        cursor.execute(sql)
        products = cursor.fetchall()
        return render_template(
            'cart.html',
            title='Cart Page',
            categories=categories,
            category=category,
            products=products) 
    else :
        user = session['user'][0][0]
        chk = request.form.getlist('chk')
        strm='';
        for row in chk :          
            strm = strm +str(int(row))+","
        qry ="insert into sales (cusid,salesitems) values ('"+str(user)+"','"+strm+"')";
        cursor = db.cursor()
        cursor.execute(qry)
        id = cursor.lastrowid
        db.commit()
        return render_template(
        'postcart.html',
        id=id) 

   
@app.route('/product')
def product():
    """Renders the home page."""
    cursor = db.cursor()
    sql = "SELECT * FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    return render_template(
        'productlist.html',
        title='Product',
        products=products,
        year=datetime.now().year,
    )



@app.route('/dashboard')
def dashboard():
    cursor = db.cursor() 
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()

    sql = "SELECT * FROM country"
    cursor.execute(sql)
    countries = cursor.fetchall()


    return render_template(
        'dashboard.html',
        categories=categories,
        countries=countries,
        year=datetime.now().year,
    )
@app.route('/report1')
def report1(): 
    nogp=0 
    cursor = db.cursor()  
    sql = "SELECT *   FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    return render_template(
        'report1.html' ,
        products=products,
    )
@app.route('/postreport1', methods=["GET", "POST"])
def postreport1():  
    cursor = db.cursor()  
    froms = request.form['fromt']
    tos = request.form['tot']
    sku = request.form['sku']
    nogp=0
    sql='SELECT c.country,COUNT(*) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` where d.qus1=1 and DATE(a.date) >= "'+str(froms)+'" and DATE(a.date) <= "'+str(tos)+'" and  b.prod_id = '+str(sku)+'  GROUP by c.country';
    cursor.execute(sql)
    newcus = cursor.fetchall()
    datanewcus="[";

    for row in newcus :
        datanewcus =datanewcus +'["'+row[0]+'",'+str(int(row[1]))+"],"

    datanewcus = datanewcus.rstrip(',')+"]"
    
    sql='SELECT c.country,COUNT(*) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` where d.qus1=0  and DATE(a.date) >= "'+str(froms)+'" and DATE(a.date) <= "'+str(tos)+'" and  b.prod_id = '+str(sku)+'  GROUP by c.country';
    cursor.execute(sql)
    existingcus = cursor.fetchall() 


    dataexistingcus="[";

    for row in existingcus :
        dataexistingcus =dataexistingcus +'["'+row[0]+'",'+str(int(row[1]))+"],"
    sql = "SELECT *   FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    dataexistingcus = dataexistingcus.rstrip(',')+"]"
    return render_template(
        'report1.html', 
        sku =sku,
        nogp=nogp,
        products=products,
        dataexistingcus=dataexistingcus,
        datanewcus=datanewcus 
    )
@app.route('/report5')
def report5(): 
    nogp=0 
    cursor = db.cursor()  
    sql = "SELECT *   FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    return render_template(
        'report5.html',
        products=products
    )
@app.route('/postreport5', methods=["GET", "POST"])
def postreport5():
    cursor = db.cursor()   
    nogp=0
    sku = request.form['sku'] 
    sql='SELECT c.country,avg(d.qus6) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` where b.prod_id='+sku+' GROUP by c.country';
    cursor.execute(sql)
    newcus = cursor.fetchall()
    datanewcus="[";

    for row in newcus :
        datanewcus =datanewcus +'["'+row[0]+'",'+str(int(row[1]))+"],"

    datanewcus = datanewcus.rstrip(',')+"]"
    

    cursor = db.cursor()  
    sql = "SELECT *   FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    
    return render_template(
        'report5.html', 
        sku=sku,
        nogp=nogp,
        products=products,
        datanewcus=datanewcus 
    )
@app.route('/report2')
def report2(): 
    nogp=0 
    cursor = db.cursor()  
    sql = "SELECT *   FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    return render_template(
        'report2.html',
        products=products
    )
@app.route('/postreport2', methods=["GET", "POST"])
def postreport2():  
    cursor = db.cursor()   
    nogp=0
    sku = request.form['sku'] 
    sql='SELECT c.country,avg(d.qus5) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` where b.prod_id='+sku+' GROUP by c.country';
    cursor.execute(sql)
    newcus = cursor.fetchall()
    datanewcus="[";

    for row in newcus :
        datanewcus =datanewcus +'["'+row[0]+'",'+str(int(row[1]))+"],"

    datanewcus = datanewcus.rstrip(',')+"]"
    

    sql='SELECT avg(`price`) FROM `product_price` WHERE `prod_id`='+sku+' GROUP BY `prod_id`';
    cursor.execute(sql)
    avg = cursor.fetchall()
    sql='SELECT c.country , ((b.`price`-'+str(avg[0][0])+')*(11-avg(d.qus3))*(avg(d.qus2)-1))/'+str(avg[0][0])+' FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country  INNER JOIN customerfeedback as d on d.salesid=a.`salesid` where b.prod_id='+sku+' group by c.country'
    cursor.execute(sql)
    newvfm = cursor.fetchall()

    ndatanewcus="[";

    for row in newvfm :
        ndatanewcus =ndatanewcus +'{ "name":"'+row[0]+'","data":['+str(int(row[1]))+"]},"

    ndatanewcus = ndatanewcus.rstrip(',')+"]"

    sql = "SELECT *   FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()

    return render_template(
        'report2.html', 
        sku=sku,
        nogp=nogp, 
        products=products,
        datanewcus=datanewcus,
        ndatanewcus=ndatanewcus
    )

@app.route('/report3')
def report3(): 
    nogp=0 
    cursor = db.cursor()  
    sql = "SELECT *   FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    return render_template(
        'report3.html' ,
        products=products
    )
@app.route('/postreport3', methods=["GET", "POST"])
def postreport3():
    cursor = db.cursor()  
    sku = request.form['sku'] 
    nogp=0 
    sql='SELECT * FROM country';
    cursor.execute(sql)
    country = cursor.fetchall()
    dataarray='['
    for cons in country :

        data="[";
        for x in range(5):
            if x==0:
                where='d.polarity <-2'
            if x==1:
                where='d.polarity  between -2 and -1'
            if x==2:
                where='d.polarity  between -1 and 1'            
            if x==3:
                where='d.polarity  between 1 and 2'
            if x==4:
                where='d.polarity <2'

            sql='SELECT COUNT(*) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` where '+where+' and c.con_id='+str(cons[0])+' and b.prod_id='+sku+' GROUP by c.country';
            cursor.execute(sql)
            result = cursor.fetchall() 
            if result==():
                data=data+'0,'
            else:
                data=data+str(result[0][0])+','
        data = data.rstrip(',')+"]"
        dataarray=dataarray+'{ "name":"'+cons[1]+'","data":'+data+'},'
    dataarray = dataarray.rstrip(',')+"]"

    sdataarray='['
    for cons in country :

        data="[";
        for x in range(5):
            if x==0:
                where='d.confidence <-2'
            if x==1:
                where='d.confidence  between -2 and -1'
            if x==2:
                where='d.confidence  between -1 and 1'            
            if x==3:
                where='d.confidence  between 1 and 2'
            if x==4:
                where='d.confidence <2'

            sql='SELECT COUNT(*) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` where '+where+' and c.con_id='+str(cons[0])+' and b.prod_id='+sku+' GROUP by c.country';
            cursor.execute(sql)
            result = cursor.fetchall() 
            if result==():
                data=data+'0,'
            else:
                data=data+str(result[0][0])+','
        data = data.rstrip(',')+"]"
        sdataarray=sdataarray+'{ "name":"'+cons[1]+'","data":'+data+'},'
    sdataarray = sdataarray.rstrip(',')+"]"

    sql = "SELECT *   FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()


    return render_template(
        'report3.html', 
        sku=sku,
        nogp=nogp,  
        dataarray=dataarray,
        sdataarray=sdataarray,
        products=products
    )
@app.route('/report6')
def report6(): 
    nogp=0 
    cursor = db.cursor()  
    sql = "SELECT *   FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()
    return render_template(
        'report6.html' ,
        categories=categories
    )
@app.route('/postreport6', methods=["GET", "POST"])
def postreport6():
    cursor = db.cursor()   
    nogp=0
    sku = request.form['sku'] 
    sql='SELECT c.country,COUNT(*) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` inner join products as pd on b.prod_id =pd.product_id inner join categories as ct on pd.category= ct.catid WHERE ct.catid='+sku+' GROUP by c.country';
    cursor.execute(sql)
    newcus = cursor.fetchall()
    datanewcus="[";

    for row in newcus :
        datanewcus =datanewcus +'["'+row[0]+'",'+str(int(row[1]))+"],"

    datanewcus = datanewcus.rstrip(',')+"]"
     
    sql = "SELECT *   FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()
    return render_template(
        'report6.html', 
        sku=sku,
        nogp=nogp,
        categories=categories,
        datanewcus=datanewcus 
    )

@app.route('/report4')
def report4(): 
    nogp=0 
    cursor = db.cursor()  
    sql = "SELECT *   FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()
    return render_template(
        'report4.html' ,
        categories=categories
    )
@app.route('/postreport4', methods=["GET", "POST"])
def postreport4():
    cursor = db.cursor()  
    sku = request.form['sku'] 
    nogp=0 
    sql='SELECT * FROM country';
    cursor.execute(sql)
    country = cursor.fetchall()
    dataarray='['
    for cons in country :

        data="[";
        for x in range(5):
            if x==0:
                where='d.polarity <-2'
            if x==1:
                where='d.polarity  between -2 and -1'
            if x==2:
                where='d.polarity  between -1 and 1'            
            if x==3:
                where='d.polarity  between 1 and 2'
            if x==4:
                where='d.polarity <2'

            sql='SELECT COUNT(*) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` inner join products as pd on b.prod_id =pd.product_id inner join categories as ct on pd.category= ct.catid where '+where+' and c.con_id='+str(cons[0])+' and ct.catid='+sku+' GROUP by c.country';
            cursor.execute(sql)
            result = cursor.fetchall() 
            if result==():
                data=data+'0,'
            else:
                data=data+str(result[0][0])+','
        data = data.rstrip(',')+"]"
        dataarray=dataarray+'{ "name":"'+cons[1]+'","data":'+data+'},'
    dataarray = dataarray.rstrip(',')+"]"


    sdataarray='['
    for cons in country :

        data="[";
        for x in range(5):
            if x==0:
                where='d.confidence <-2'
            if x==1:
                where='d.confidence  between -2 and -1'
            if x==2:
                where='d.confidence  between -1 and 1'            
            if x==3:
                where='d.confidence  between 1 and 2'
            if x==4:
                where='d.confidence <2'

            sql='SELECT COUNT(*) FROM `sales` as a inner join product_price as b on FIND_IN_SET(b.prd_price_id,a.salesitems) INNER JOIN country as c on c.con_id=b.country INNER JOIN customerfeedback as d on d.salesid=a.`salesid` inner join products as pd on b.prod_id =pd.product_id inner join categories as ct on pd.category= ct.catid where '+where+' and c.con_id='+str(cons[0])+' and ct.catid='+sku+' GROUP by c.country';
            cursor.execute(sql)
            result = cursor.fetchall() 
            if result==():
                data=data+'0,'
            else:
                data=data+str(result[0][0])+','
        data = data.rstrip(',')+"]"
        sdataarray=sdataarray+'{ "name":"'+cons[1]+'","data":'+data+'},'
    sdataarray = sdataarray.rstrip(',')+"]"

    sql = "SELECT *   FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()


    return render_template(
        'report4.html', 
        sku=sku,
        nogp=nogp,  
        dataarray=dataarray,
        sdataarray=sdataarray,
        categories=categories
    )
@app.route('/logout')
def logout():
    session.clear()
    return  redirect('/login')

@app.route('/category')
def category():
    cursor = db.cursor() 
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()
    return render_template(
       'category.html' ,
       categories=categories  
    )
@app.route('/postcategory', methods=["GET", "POST"])
def postcategory():
     name = request.form['name']
     qry="insert into categories (catname)values('"+name+"')"
     cursor = db.cursor()
     cursor.execute(qry)
     db.commit()
     return redirect('/category')
@app.route('/subcategory')
def subcategory():
    """Renders the home page."""
    cursor = db.cursor() 
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()   
    sql = "SELECT a.*,b.catname FROM subcategories as a inner join categories as b on a.catid=b.catid"
    cursor.execute(sql)
    subcategories = cursor.fetchall() 
    return render_template(
        'subcategory.html',
        categories=categories,
        subcategories=subcategories
    )
@app.route('/postsubcategory', methods=["GET", "POST"])
def postsubcategory():
     name = request.form['name']
     category = request.form['category']
     qry="insert into subcategories (name,catid)values('"+name+"','"+str(category)+"')"
     cursor = db.cursor()
     cursor.execute(qry)
     db.commit()
     return redirect('/subcategory')
@app.route('/addproduct')
def addproduct():
    """Renders the home page."""
    cursor = db.cursor()
    path =os.path.dirname(app.instance_path)
    sql = "SELECT * FROM categories"
    cursor.execute(sql)
    categories = cursor.fetchall()

    sql = "SELECT * FROM country"
    cursor.execute(sql)
    countries = cursor.fetchall()
    return render_template(
        'product.html',
        categories=categories,
        countries=countries,
        year=datetime.now().year,
    )

@app.route("/addItem", methods=["GET", "POST"])
def addItem():
    if request.method == "POST":
        name = request.form['name']
        sku = request.form['sku'] 
        description = request.form['description'] 
        categoryId = request.form['category']
        subcategoryId = request.form['subcategory'] 
        #Uploading image procedure
        image = request.files['image']
        if image and allowed_file(image.filename):
            filename = my_random_string(6)+secure_filename(image.filename)
            image.save(os.path.join(os.path.dirname(app.instance_path),app.config['UPLOAD_FOLDER'], filename))
        imagename = filename
        price = request.form['price']
        price1 = request.form['price1']
        price2 = request.form['price2']
        country = request.form['country']
        country1 = request.form['country1']
        country2 = request.form['country2']
        qry ="insert into products(name,sku,image,description,category,subcategory) values('"+name+"','"+sku+"','"+imagename+"','"+description+"','"+str(categoryId)+"','"+str(subcategoryId)+"')"
        cursor = db.cursor()
        cursor.execute(qry)
        id = cursor.lastrowid
        qry ="insert into product_price (price,country,prod_id)values('"+str(price)+"','"+str(country)+"','"+str(id)+"')"
        cursor.execute(qry)
        qry ="insert into product_price (price,country,prod_id)values('"+str(price1)+"','"+str(country1)+"','"+str(id)+"')"
        cursor.execute(qry)
        qry ="insert into product_price (price,country,prod_id)values('"+str(price2)+"','"+str(country2)+"','"+str(id)+"')"
        cursor.execute(qry)
        db.commit()

        return redirect('/addproduct')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )
@app.route('/login')
def login():
    """Renders the contact page."""
    return render_template(
        'login.html',
        title='Login' 
    )
@app.route('/loginpost', methods = ['POST'])
def loginpost():
    email = request.form['email']
    password = request.form['password']
    cursor = db.cursor()
    sql = "SELECT * FROM users where email='"+email+"' and password='"+password+"'"
    cursor.execute(sql)
    users = cursor.fetchall()
    if  len(users) !=0:
        session['user'] = users
        session['email'] = email
        type=users[0][3]
        if int(type)!=0:  
            return redirect('/dashboard')
        else:  
            return redirect('/cart')

    """Renders the contact page."""
    return render_template(
        'login.html',
        title='Login',
        error="Invalid Login"
    )


@app.route('/registeration')
def registeration():
    """Renders the contact page."""
    sql = "SELECT * FROM country"
    cursor = db.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()
    return render_template(
        'register.html',
        title='Contact',
        success='op',
        countries=countries
    )
@app.route('/register', methods = ['POST'])
def register():
    name = request.form['name']
    address = request.form['address']
    zipcode = request.form['zipcode']
    email = request.form['email']
    password = request.form['password']
    city = request.form['city']
    state = request.form['state']
    country = request.form['country'] 
    
    qry="insert into users (name,address,zipcode,email,password,city,state,country)values('"+name+"','"+address+"','"+zipcode+"','"+email+"','"+password+"','"+city+"','"+state+"','"+str(country)+"')"
    cursor = db.cursor()
    cursor.execute(qry)
    db.commit()

    sql = "SELECT * FROM country"
    cursor = db.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()

    success='ok'
    return render_template(
        'register.html',
        title='Register',
        success=success,
        countries=countries
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/result', methods = ['POST', 'GET']) # /result route, allowed request methods; POST, and GET
def predict():
	if request.method == 'POST': 
		result = request.form['Name'] # fetches text from <input name = "Name"> from index.html
		blob = TextBlob(result)
		for sentence in blob.sentences:
			result = sentence.sentiment.polarity # result = polarity value subjectivity
		return render_template('index.html', result = result) # renders template: index.html with argument result = polarity value calculated
	else:
		return render_template('index.html')	






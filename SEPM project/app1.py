from flask import Flask, render_template, request,redirect, url_for,session
#import integrated
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root0104",
  database="webscraping"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM products")
print("Connection Established")

result = mycursor.fetchall()

#for row in result:
  #print(row)

mydb.close()
app = Flask(__name__)
@app.route('/')
def index():
    if request.method == 'POST':
        print("====================================")
        print("I am in index")
        print("====================================")
        search_term = request.form['search']
        print(search_term)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root0104",
            database="webscraping"
        )
        mycursor = mydb.cursor()
        #search_term = search_term+"%"
        mycursor.execute("SELECT * FROM products WHERE PRODUCT_NAME = %s",(search_term,))
        result1=mycursor.fetchall()
        print(result1)
        for row in result1:
            a_url=row[1]
            f_url=row[2]
        return a_url, f_url
    
@app.route('/search', methods=['POST'])
def search():
    print("====================================")
    print("I am is search")
    print("====================================")
    amazon_url, flipkart_url =index()
    

    print(flipkart_url)
    from amazon_scrape import print_data
    from flipkart_scrape import print_data1

    
    a_producttitle,a_price,a_review,a_availability, a_rating=print_data(amazon_url)
    f_product_name,f_price,f_review,f_availability,f_rating=print_data1(flipkart_url)

    #result1= integrated.
    print("test")
    
        
    
    
    return render_template('search.html', a_producttitle=a_producttitle, a_price=a_price, a_review=a_review, a_availability=a_availability, a_rating=a_rating,f_product_name=f_product_name,f_price=f_price,f_review=f_review, f_availability=f_availability,f_rating=f_rating)





if __name__ == '__main__':
    app.run(debug=True)

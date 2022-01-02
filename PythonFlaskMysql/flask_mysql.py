from flask import Flask, request, jsonify
import pymysql

class_db = pymysql.connect(user='root', passwd='1234', host='127.0.0.1', db='classicmodels', charset='utf8')

app = Flask(__name__)
@app.route('/')
@app.route('/get', methods=['GET'])
def get():
    limit = request.args.get('limit')
    cursor = class_db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/new', methods=['POST'])
def post():
    data = request.json
    print(data)
    cursor = class_db.cursor(pymysql.cursors.DictCursor)
    sql = '''INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    cursor.execute(sql, (data['customerNumber'], data['customerName'], data['contactLastName'], data['contactFirstName'], data['phone'], data['addressLine1'], data['addressLine2'], data['city'], data['state'], data['postalCode'], data['country']))

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
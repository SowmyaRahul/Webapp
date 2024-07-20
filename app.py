from flask import Flask, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Environment variables for RDS connection
RDS_HOST = os.getenv('RDS_HOST', 'your-rds-endpoint')
RDS_USER = os.getenv('RDS_USER', 'your-username')
RDS_PASSWORD = os.getenv('RDS_PASSWORD', 'your-password')
RDS_DB = os.getenv('RDS_DB', 'your-database')

app.config['MYSQL_HOST'] = RDS_HOST
app.config['MYSQL_USER'] = RDS_USER
app.config['MYSQL_PASSWORD'] = RDS_PASSWORD
app.config['MYSQL_DB'] = RDS_DB

mysql = MySQL(app)


def get_db_connection():
    return mysql.connector.connect(
        host=RDS_HOST,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )


@app.route('/health')
def home():
    return "Hello, Flask with RDS!"

@app.route('/users')
def users():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users')  # Assuming you have a table named 'users'
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')
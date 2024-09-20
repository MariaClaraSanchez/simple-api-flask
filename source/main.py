from flask import Flask, jsonify
from db.connection import Mysql

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_user():
    mysql_instance = Mysql()
    users = mysql_instance.get_itens(query='SELECT * FROM USERS')
    mysql_instance.close_connection()
    response = {
        'users': users
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
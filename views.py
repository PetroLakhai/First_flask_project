from flask import Markup, render_template
from flask.json import jsonify


from app import app


@app.route("/test")
def button():
    return Markup(
        "<form action='http://127.0.0.1:5000/template' method='get'><button type='submit'>LIST</button></form>"
    )


@app.route("/json", methods=['GET', 'POST'])
def json_route():
    return jsonify({'name': 'Petro', 'LastName': 'Lakhai'})


@app.route("/template")
def template():
    res = [
        {'computer': 'Apple', 'processor': 'intel-i3', 'price': 45000},
        {'computer': 'Dell', 'processor': 'intel-i7', 'price': 40000},
        {'computer': 'Lenovo', 'processor': 'intel-i5', 'price': 33000},
        {'computer': 'Samsung', 'processor': 'intel-i5', 'price': 28000}
    ]

    return render_template('hello.html', name='computer_data', result=res, if_price=0)
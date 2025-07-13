from flask import Flask, request, render_template
import boto3
from datetime import datetime
import uuid

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Expenses')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = {
            'id': str(uuid.uuid4()),
            'category': request.form['category'],
            'amount': float(request.form['amount']),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        table.put_item(Item=item)
        return "Expense recorded!"
    return render_template('form.html')
app.run(host='0.0.0.0', port=80)

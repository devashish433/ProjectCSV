from flask import Flask, render_template, request
from os import system
import pandas as pd
import requests
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        data =[]
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        return render_template('data.html', data=data)

@app.route('/data/<int:transaction_id>', methods=['GET', 'POST'])
def row_detail(transaction_id=0):
    data = []
    datac = []
    datam = []
    total = 0
    with open('ford_escort.csv') as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            data.append(row[int(transaction_id)])
        data_count = len(data) - 1
        data.pop(0)
        data_max = max(data)
        data_min = min(data)
        for ele in range(0, len(data)):
            if isinstance(ele, int):
            # adding the element to the total
                total += int(ele)

    return render_template('data.html', data=data, datac = data_count, datamax = data_max, datamin = data_min, data_sum = total)

# 0 - name
# 1 - age
# 2 - gender
# 3 - class

@app.route('/data/append', methods=['GET', 'POST'])
def appenddata():
    
    return render_template('append.html')


@app.route('/data/<int:transaction_row>/<int:transaction_col>', methods=['GET', 'POST'])
def data_number(transaction_row, transaction_col):
    with open('main.csv') as fd:
        # os.system('data.html.{}'.format(PlayfileDir))
        data = []
        reader=csv.reader(fd)
        rows = list(fd)
        data.write(rows[int(transaction_row)][int(transaction_col)])
    return render_template('candidate.html', data=data)

# @app.route('/csvup', methods=['GET'])
# def upload():
#     data = pd.read_csv (r'main2.csv')   
#     df = pd.DataFrame(data)
#     return render_template('csvup.html', aa=df)


if __name__ == "__main__":
    app.run(debug=True)
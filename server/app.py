from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load your dataset
df = pd.read_csv('/Users/sanchitajindal/Coding/data_visualization/server/data.csv')


@app.route('/columns', methods=['POST'])
def get_columns():
    columns = df.columns.tolist()
    print(columns)
    return jsonify(columns)

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    chart_type = data['chartType']
    x_column = data['xColumn']
    y_column = data['yColumn']

    if chart_type == 'bar':
        result = df[[x_column, y_column]].dropna().to_dict(orient='records')
    elif chart_type == 'pie':
        result = df[[x_column, y_column]].dropna().to_dict(orient='records')
    elif chart_type == 'stacked_bar':
        result = df[[x_column, y_column]].dropna().to_dict(orient='records')
    else:
        result = {}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

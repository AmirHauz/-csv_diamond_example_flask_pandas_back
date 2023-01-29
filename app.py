import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MY_FILE = 'diamond.csv'
MY_FILE_ID = 'dimond_with_id.csv'

def load_data():
    df = pd.read_csv(MY_FILE)
    return df.to_dict(orient='records')


def add_id():
    df = pd.read_csv(MY_FILE)
    df.insert(0, 'ID', range(1, 1 + len(df)))
    df.to_csv(MY_FILE_ID, index=False)

def remove_id():
    df = pd.read_csv(MY_FILE_ID)
    df = df.drop(columns=['ID'])
    df.to_csv(MY_FILE, index=False)

def load_data_id():
    add_id()
    df = pd.read_csv(MY_FILE_ID)
    return df.to_dict(orient='records')



def get_headers():
    f = pd.read_csv(MY_FILE)
    return df.columns.values.tolist()

def get_headers_id():
    df = pd.read_csv(MY_FILE_ID)
    return df.columns.values.tolist()

@app.route('/diamond', methods=['POST'])
def new_diamond():
    data = request.get_json()
    df = pd.read_csv(MY_FILE)
    df = df.append(data, ignore_index=True)
    df.to_csv(MY_FILE, index=False)
    return data

@ app.route('/diamond', methods=['GET'])
@ app.route('/diamond/<int:diamond_id>', methods=['GET'])
def read_diamond(diamond_id = -1):
    add_id()
    df = pd.read_csv(MY_FILE_ID)
    if (diamond_id == -1):
        return df.to_dict(orient='records')
    else:
        return df[df['ID'] == diamond_id].to_dict(orient='records')

@app.route('/diamond/<int:diamond_id>', methods=['PUT'])
def update_diamond(diamond_id):
    input_data = request.get_json()
    df = pd.read_csv(MY_FILE_ID)
    df.loc[df['ID'] == diamond_id, list(input_data.keys())] = list(input_data.values())
    df.to_csv(MY_FILE_ID, index=False)
    remove_id()
    return input_data

@app.route('/diamond/<int:diamond_id>', methods=['DELETE'])
def delete_diamond(diamond_id):
    df = pd.read_csv(MY_FILE_ID)
    df = df[df.ID != diamond_id]
    df.to_csv(MY_FILE_ID, index=False)
    remove_id()

    return jsonify({'message': diamond_id})




if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

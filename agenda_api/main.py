from flask import *
import json

app = Flask(__name__)

# doc : https://flask.palletsprojects.com/en/2.1.x/

my_agendas = {
    '1': {
        '1': {'name': 'Clotilde', 'phone_number': '0606060606'},
        '2': {'name': 'Michel', 'phone_number': '0101010101'},
        '3': {'name': 'Jean', 'phone_number': '0202020202'},
    },
    '2': {
        '1': {'name': 'A', 'phone_number': '0303030303'},
        '2': {'name': 'B', 'phone_number': '0404040404'},
        '3': {'name': 'C', 'phone_number': '0505050505'},
    }
}


@app.route('/', methods=['GET'])
def root():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded to the home page'}
    return data_set


@app.route('/agendas/<user_id>')
def agenda(user_id):
    try:
        return my_agendas[user_id]
    except KeyError:
        return 'This user does not exist.'


@app.route('/agendas/<user_id>/contacts/<contact_id>')
def contact(user_id, contact_id):
    response = agenda(user_id)
    try:
        return response[contact_id]
    except KeyError:
        return 'This contact does not exist.'


if __name__ == '__main__':
    app.run(port=7777)

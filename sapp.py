from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

parking_spaces = [{'id': 1, 'status': 'free'}, {'id': 2, 'status': 'free'}, {'id': 3, 'status': 'free'}]

# loading data with starting
with open('parking_spaces.json', 'w') as f:
    json.dump(parking_spaces, f)

# sending inform about parking
@app.route('/parking_info', methods=['GET'])
def get_parking_info():
    free_spaces = sum(1 for space in parking_spaces if space['status'] == 'free')
    parking_info = {
        'free_spaces': free_spaces,
        'total_spaces': len(parking_spaces)
    }
    return jsonify(parking_info)

@app.route('/parking/free_spaces', methods=['GET'])
def get_free_spaces():
    free_spaces = [{'id': space['id'], 'status': space['status']} for space in parking_spaces if space['status'] == 'free']
    return jsonify(free_spaces)

@app.route('/parking/free_spaces_with_id', methods=['GET'])
def get_free_spaces_with_id():
    free_spaces = [{'id': space['id'], 'status': space['status']} for space in parking_spaces if space['status'] == 'free']
    return jsonify(free_spaces)

# reserve parking
@app.route('/parking/reserve', methods=['POST'])
def reserve_parking_space():
    data = request.get_json()
    space_id = data.get('id')
    name = data.get('name')
    phone = data.get('phone')
    
    print(f"Received data: {data}")

    if space_id is None:
        return 'Space id is missing', 400

    space = next((space for space in parking_spaces if space['id'] == space_id), None)

    if space is None:
        return 'Space not found', 404

    if space['status'] != 'free':
        return 'Space is already occupied', 409

    space['status'] = 'reserved'
    space['name'] = name
    space['phone'] = phone

    print(f"Successfully reserved parking space {space_id} for {name} ({phone})")

    # Save the updated parking spaces data to file
    with open('parking_spaces.json', 'w') as f:
        json.dump(parking_spaces, f)

    return f"Successfully reserved parking space {space_id} for {name} ({phone})"

    return 'Space reserved successfully', 200

# sending info about reserving parking place
@app.route('/parking/cancel', methods=['POST'])
def cancel_parking_reservation():
    data = request.get_json()
    space_id = data.get('id')

    if space_id is None:
        return 'Space id is missing', 400

    space = next((space for space in parking_spaces if space['id'] == space_id), None)

    if space is None:
        return 'Space not found', 404

    if space['status'] != 'reserved':
        return 'Space is not reserved', 409

    space['status'] = 'free'
    space.pop('name', None)
    space.pop('phone', None)

    # Save the updated parking spaces data to file
    with open('parking_spaces.json', 'w') as f:
        json.dump(parking_spaces, f)

    return 'Reservation canceled successfully', 200

if __name__ == '__main__':
    app.run(port=8002)
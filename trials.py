import serial
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get('/')
def index():
    return 'Hello, this is the homepage!'


@app.post('/command')
def receive_command():
    data = request.get_json()  # Get JSON data from the request
    if 'action' in data:
        serial_port = '/dev/ttyUSB0'  # Replace this with your specific serial port
        baud_rate = 9600
        ser = serial.Serial(serial_port, baud_rate)
        ser.open()
        data_to_send = data["action"]
        ser.write(data_to_send.encode())  # Ensure the data is encoded as bytes before sending
        ser.close()
        return jsonify({'message': f'Submitted {data_to_send}'})
    else:
        return jsonify({'error': 'Invalid data format'}), 400  # Bad request status code


if __name__ == '__main__':
    app.run(port=8000, debug=True)

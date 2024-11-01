from flask import Flask, jsonify
from test_api import forecast  # Import the forecast function
import os

app = Flask(_name_)

@app.route('/forecast', methods=['GET'])
def forecast_route():
    # Call the forecast function and return its response as JSON
    result = forecast()
    return jsonify(result)

if _name_ == '_main_':
    port =int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, jsonify
from forecast_module import forecast  # Import the forecast function

app = Flask(_name_)

@app.route('/forecast', methods=['GET'])
def forecast_route():
    # Call the forecast function and return its response as JSON
    result = forecast()
    return jsonify(result)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
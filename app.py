from flask import Flask, jsonify
from test_api import forecast
from Peso import forecast_peso
from Yen import forecast_yen  # Import the forecast function
import os
from gpt_api import get_recom, pol_jp, ek_jp, gen_jp, pol_ph, ek_ph, gen_ph

from test_sql import get_db, ExampleTable

from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

from test_sql import init_db
init_db()

app = Flask(__name__)

@app.route('/forecast', methods=['GET'])
def forecast_route():
    # Call the forecast function and return its response as JSON
    result = forecast()
    return result

@app.route('/forecast_ph', methods=['GET'])
def forecast_ph():
    # Call the forecast function and return its response as JSON
    result = forecast_peso()
    return result

@app.route('/forecast_jp', methods=['GET'])
def forecast_jp():
    # Call the forecast function and return its response as JSON
    result = forecast_yen()
    return result

# Route to get all entries in the example table
@app.route('/data', methods=['GET'])
def get_data():
    db: Session = next(get_db())
    items = db.query(ExampleTable).all()
    data = [{"id": item.id, "name": item.name, "value": item.value} for item in items]
    return jsonify(data)

# Route to add a new entry
@app.route('/data', methods=['POST'])
def add_data():
    db: Session = next(get_db())
    new_data = request.get_json()
    item = ExampleTable(name=new_data['name'], value=new_data['value'])
    db.add(item)
    db.commit()
    db.refresh(item)
    return jsonify({"id": item.id, "name": item.name, "value": item.value}), 201

@app.route('/politik_ph', methods=['GET'])
def get_ph_pol():
    result = pol_ph()
    return result

@app.route('/ekonomi_ph', methods=['GET'])
def get_ph_ekon():
    result = ek_ph()
    return result

@app.route('/general_ph', methods=['GET'])
def get_ph_general():
    result = gen_ph()
    return result

@app.route('/politik_jp', methods=['GET'])
def get_jp_pol():
    result = pol_jp()
    return result

@app.route('/ekonomi_jp', methods=['GET'])
def get_jp_ekon():
    result = ek_jp()
    return result

@app.route('/general_jp', methods=['GET'])
def get_jp_general():
    result = gen_jp()
    return result


if __name__ == '__main__':
    port =int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
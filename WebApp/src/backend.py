from flask import Flask, render_template, jsonify
app = Flask(__name__)
    
import sys
import json
import psycopg2

from flask import Flask, render_template, jsonify
app = Flask(__name__)

import sys
import json
import psycopg2

app = Flask(__name__)
# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="vpnosint_db",
        user="vpnosint_user",
        password="labtrash337",
        host="localhost"
    )
    return conn


# Analyst view
@app.route('/analyst')
def analyst():
    """ """
    return render_template("analyst.html")


# Aggregate View
## Company Profile API


# Example route to render the profile view
@app.route('/company/<int:company_id>')
def company_profile(company_id):
    # You would query your database to fetch the specific company data here
    return render_template('company_profile.html')

# Example route to render the profile view
@app.route('/web_artifact')
def web_artifact():
    # You would query your database to fetch the specific company data here
    return render_template('web_artifact.html')

# API endpoint to fetch the company data
@app.route('/api/vpn-company/<int:company_id>')
def get_company_data(company_id):
    # Fetch data from your database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT latitude,longitude,address,business_name,incorporation_date FROM vpnosint_business_db WHERE id={company_id};')
    locations = cur.fetchall()
    business_name = locations[0][3]
    print(locations)

    """
    id, domain_name, address, latitude, longitude, business_id, registration_date, registrar, registrar_abuse_email, registrar_phone, registrant_name, registrant_organization

    """
    cur.execute(f'SELECT latitude,longitude,address,registration_date,registrar,registrant_name FROM vpnosint_domain_db WHERE business_id={company_id};')
    domain_info = cur.fetchall()
    print(domain_info)
    cur.close()
    conn.close()

    company_data = {
        "name": business_name,
        "locations": [{'lat': loc[0], 'lon': loc[1], "address" : loc[2] } for loc in locations] +\
                [{'lat': loc[0], 'lon': loc[1], "address" : loc[2] } for loc in domain_info],
        "timelineEvents": [{"label": "Incorporation", "date": loc[4]} for loc in locations] +\
                [{"label" : "Domain Registration", "date" : loc[3]} for loc in domain_info],
        "relationships": [{"from": business_name, "to": "Foo",
                           "from": business_name, "to": "Bar"} for loc in domain_info]
    }
    return jsonify(company_data)

# Location API
@app.route('/api/locations')
def get_locations():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT latitude, longitude FROM vpnosint_business_db;')
    locations = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([{'lat': loc[0], 'lng': loc[1]} for loc in locations])

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main() # app.run(debug=True)

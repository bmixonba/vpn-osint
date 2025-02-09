from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, url_for
app = Flask(__name__)
    
import sys
import json
import psycopg2
import os

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

@app.route('/api/submit_business', methods=['POST'])
def submit_business():
    """
    Create a new business

    database schema for table. 
    vpnosint_db=# d vpnosint_business_db
                                                Table "public.vpnosint_business_db"
           Column       |            Type             | Collation | Nullable |                     Default                      
    --------------------+-----------------------------+-----------+----------+--------------------------------------------------
     id                 | integer                     |           | not null | nextval('vpnosint_business_db_id_seq'::regclass)
     business_name      | character varying(255)      |           | not null | 
     address            | text                        |           |          | 
     latitude           | double precision            |           |          | 
     longitude          | double precision            |           |          | 
     incorporation_date | timestamp without time zone |           |          | 

    Api submission from front end.
    api/submit_business/
        data={'company_id': '-1', 'company_name': 'Test VPN Company', 'address': 'Some funky address', 'latitude': '123123', 'longitude': '123123', 'incorporation_date': '2025-02-05T16:30'}
    """
    data = request.json
    print(f"RAN - api/submit_business/")
    business_name = data['company_name']
    address = data['address']
    latitude = data['latitude']
    longitude = data['longitude']
    incorporation_date = data['incorporation_date']
    print(f"\business_name={business_name}, address={address}, latitude={latitude}, longitude={longitude}, incorporation_date={incorporation_date}")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO vpnosint_business_db (business_name, address, latitude, longitude, incorporation_date) VALUES (%s, %s, %s, %s, %s)',
                (business_name, address, latitude, longitude, incorporation_date))
    conn.commit()
    cur.close()
    conn.close()

    """
    """
    return jsonify({'ok' : True, "statusText" : "Company Successfully Added."}) 

@app.route('/submit_social_media', methods=['POST'])
def submit_social_media():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO user_data (name, email, message) VALUES (%s, %s, %s)',
                (name, email, message))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('analyst'))

"""
"""
# Aggregate View
## Company Profile API


# Example route to render the profile view
@app.route('/company/<int:company_id>')
def company_profile(company_id):
    # You would query your database to fetch the specific company data here
    return render_template('company_profile.html')

# Example route to render the profile view
@app.route('/web_artifact/<int:company_id>')
def web_artifact():
    return render_template('web_artifact.html')

# Example route to render the profile view
@app.route('/vpn_company_webpages/<int:company_id>')
def vpn_company_webpages():
    # You would query your database to fetch the specific company data here

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(f'SELECT * FROM vpnosint_webpage_db WHERE company_id={company_id};')

    locations = cur.fetchall()
    return render_template('web_artifact.html')

# API endpoint to fetch the company data
@app.route('/api/vpn-company/<int:company_id>')
def get_company_data(company_id):
    # Fetch data from your database
    if company_id == -1:
        print(f"get_company_data - 1 - {company_id}")
        return jsonify({})

    else:
        print(f"get_company_data - 2 - {company_id}")
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

@app.route('/network-data', methods=['GET'])
def network_data():
    data = {
        "nodes": [
            {"data": {"id": "vpn1", "label": "Lemon Clove"}},
            {"data": {"id": "vpn2", "label": "Autumn Breeze"}},
            {"data": {"id": "vpn3", "label": "Innovative Connecting"}},
            {"data": {"id": "person1", "label": "Kathleen S. Fennessy"}},
        ],
        "edges": [
            {"data": {"source": "vpn1", "target": "person1", "label": "Copyright"}},
            {"data": {"source": "vpn1", "target": "vpn3", "label": "Undisclosed Partnership"}},
            {"data": {"source": "vpn1", "target": "vpn2", "label": "Undisclosed Partnership"}},
        ]
    }
    return jsonify(data)

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

# APK API
@app.route('/api/vpn_apk/int:apk_id')
def get_vpn_apk():
    """ """
    conn = get_db_connection()
    cur = conn.cursor()


SOURCE_CODE_PATH = "./decompiled_apk"

@app.route('/source-files')
def list_source_files():
    """List all source code files in the decompiled APK directory."""
    files = []
    for root, _, filenames in os.walk(SOURCE_CODE_PATH):
        for filename in filenames:
            if filename.endswith('.java') or filename.endswith('.xml'):  # Include Java/XML files
                relative_path = os.path.relpath(os.path.join(root, filename), SOURCE_CODE_PATH)
                files.append(relative_path)
    return jsonify(files)

@app.route('/source-code/<path:filename>')
def get_source_code(filename):
    """Serve the content of a specific source file."""
    return send_from_directory(SOURCE_CODE_PATH, filename)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/example_index')
def example_index():
    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch data for the Form View (e.g., list of companies)
    cur.execute('SELECT id, business_name FROM vpnosint_business_db;')
    companies = [[-1, "New"]] + cur.fetchall()

    # Fetch data for the Analyst View (e.g., specific company details)
    # company_id = request.args.get('company_id', default=1, type=int)  # Default to first company
    # cur.execute('SELECT * FROM companies WHERE id = %s;', (company_id,))
    company_details = [50,"VPN Company",80] # cur.fetchone()

    # Fetch data for the Company-Specific Information View (e.g., categories of information)
    # cur.execute('SELECT category, COUNT(*) as count FROM company_info WHERE company_id = %s GROUP BY category;', (company_id,))
    company_categories = ["Proxy","Accelerator","VPN"] # cur.fetchall()

    # Fetch data for the Global View (e.g., aggregate information about all companies)
    # cur.execute('SELECT COUNT(*) as total_companies FROM companies;')
    total_companies = 3 # cur.fetchone()[0]

    # cur.execute('SELECT AVG(revenue) as avg_revenue FROM companies;')
    avg_revenue = 500000000 # cur.fetchone()[0]

    # cur.close()
    # conn.close()

    return render_template(
        'example_index.html',
        companies=companies,
        company_details=company_details,
        company_categories=company_categories,
        total_companies=total_companies,
        avg_revenue=avg_revenue
    )

@app.route('/api/update_business/<int:company_id>', methods=['PUT'])
def update_business(company_id):
    """Update existing company information.

    """
    #  conn = get_db_connection()
    # cur = conn.cursor()
    print(f"RAN - api/update_company/{company_id}")
    return redirect(url_for('example_index'))

@app.route('/api/delete_company/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    if company_id == -1:
        return jsonify({'status' : 200, "statusText" : "Nothing to delete."})
    else:
        print(f"/api/delete_company/{company_id}={type(company_id)}")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM vpnosint_business_db WHERE id = %s;',(company_id,));
        conn.commit()
        cur.close()
        conn.close()

        print(f"api/delete_company/{company_id}")
        return jsonify({'ok' : True, "statusText" : "Company Successfully Deleted."}) 



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main() # app.run(debug=True)

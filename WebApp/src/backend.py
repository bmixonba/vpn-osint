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
        password="<password>",
        host="localhost"
    )
    return conn


# Analyst view
@app.route('/analyst')
def analyst():
    """ """
    return render_template("analyst.html")

# BEGIN: Business Transparency CRUD API endpoints

@app.route('/api/create_business', methods=['POST'])
def create_business():
    """
    Create a new business
    """
    data = request.json
    print(f"data={data}")
    print(f"RAN - api/create_business/")
    keys = []
    vals = []
    company_id = data['company_id']
    print(f"company_id={company_id}, type(company_id)={type(company_id)}")
    if company_id == -1 or company_id == '-1':
        if 'company_name' in data and len(data['company_name']) > 0:
            business_name = data['company_name']
            keys.append("business_name")
            vals.append(f"'{business_name}'")
        if 'address' in data and len(data['address']) > 0:
            address = data['address']
            keys.append("address")
            vals.append(f"'{address}'")
        if 'latitude' in data and len(data['latitude']) > 0:
            latitude = data['latitude']
            keys.append("latitude")
            vals.append(latitude)
        if 'longitude' in data and len(data['longitude']) > 0:
            longitude = data['longitude']
            keys.append("longitude")
            vals.append(longitude)
        if 'incorporation_date' in data and len(data['incorporation_date']) > 0:
            incorporation_date = data['incorporation_date']
            keys.append(f"'{incorporation_date}'")
            vals.append(incorporation_date)
        keys = ','.join(keys)
        vals = ','.join(vals)
        cmd = f"INSERT INTO vpnosint_business_db ({keys}) VALUES ({vals})"
        print(f"cmd={cmd}")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(cmd)
        conn.commit()
        cur.close()
        conn.close()

        """
        """
        return jsonify({'ok' : True, "statusText" : "Company Successfully Added."}) 
    else:
        return jsonify({"ok" : False, "statusText" : "Cannot create existing company" })


@app.route('/api/update_business/<int:company_id>', methods=['PUT'])
def update_business(company_id):
    """Update existing company information.

    notes:

    RAN - api/update_company/11
    RAN - data={'company_id': '11', 'company_name': 'Test business 1 update', 'address': '', 'latitude': '', 'longitude': '', 'incorporation_date': ''}

    """
    data = request.json
    print(f"RAN - api/update_company/{company_id}")
    print(f"RAN - data={data}")

    update_cmd = []
    company_id = data["company_id"]
    print(f"company_id={company_id}, type(company_id)={type(company_id)}")
    if company_id == -1 or company_id == '-1':
        return jsonify({"ok" : False, "statusText" : "Cannot update unknown company" })
    else:
        if 'company_name' in data and len(data['company_name']) > 0:
            business_name = data['company_name']
            tmp = f"business_name='{business_name}'"
            update_cmd.append(tmp)
        if 'address' in data and len(data['address']) > 0:
            address = data['address']
            tmp = f"address='{address}'"
            update_cmd.append(tmp)
        if 'latitude' in data and len(data['latitude']) > 0:
            latitude = data['latitude']
            tmp = f"latitude={latitude}"
            update_cmd.append(tmp)

        if 'longitude' in data and len(data['longitude']) > 0:
            longitude = data['longitude']
            tmp = f"longitude={longitude}"
            update_cmd.append(tmp)
        if 'incorporation_date' in data and len(data['incorporation_date']) > 0:
            incorporation_date = data['incorporation_date']
            tmp = f"incorporation_date='{incorporation_date}'"
            update_cmd.append(tmp)
        update_cmd = ','.join(update_cmd)
        cmd = f"UPDATE vpnosint_business_db SET {update_cmd} WHERE id={company_id};"
        print(f"cmd={cmd}")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(cmd)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"ok" : True, "statusText" : "Company Successfully Updated."}) 

@app.route('/api/delete_business/<int:company_id>', methods=['DELETE'])
def delete_business(company_id):
    if company_id == -1:
        return jsonify({'status' : 200, "statusText" : "Nothing to delete."})
    else:
        print(f"/api/delete_business/{company_id}={type(company_id)}")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM vpnosint_business_db WHERE id = %s;',(company_id,));
        conn.commit()
        cur.close()
        conn.close()

        print(f"api/delete_company/{company_id}")
        return jsonify({'ok' : True, "statusText" : "Company Successfully Deleted."}) 


# END: Business Transparency CRUD API endpoints

# BEGIN - CRUD for social media transparency
@app.route('/api/create_social_media', methods=['POST'])
def create_social_media():
    """
    Create a new Social Media,

    Model:

    vpnosint_business_to_twitter_db

    POST Request structure

    company_id

    """
    data = request.json
    print(f"data={data}")
    print(f"RAN - api/create_social_media/")
    keys = []
    vals = []
    company_id = data['company_id']
    print(f"api/create_social_media/, company_id={company_id}, type(company_id)={type(company_id)}")
    if company_id == -1 or company_id == '-1':
        """
        

        """
        keys = []
        vals = []
        if 'x_profile_name' in data and len(data['x_profile_name']) > 0:
            x_profile_name = data['x_profile_name']
            keys.append("x_profile_name")
            vals.append(f"'{x_profile_name}'")
        if 'x_follower_count' in data and len(data['x_follower_count']) > 0:
            x_follower_count = data['x_follower_count']
            keys.append("x_follower_count")
            vals.append(f"{x_follower_count}")
        if 'x_following_count' in data and len(data['x_following_count']) > 0:
            x_following_count = data['x_following_count']
            keys.append("x_following_count")
            vals.append(x_following_count)
        if 'x_location' in data and len(data['x_location']) > 0:
            x_location = data['x_location']
            keys.append("x_location")
            vals.append(x_location)
        if 'x_joined_date' in data and len(data['x_joined_date']) > 0:
            x_joined_date = data['x_joined_date']
            keys.append(f"'{x_joined_date}'")
            vals.append(x_joined_date)
            """
            fb_profile_name
            fb_follower_count
            fb_location
            fb_joined_date
            """

        keys = ','.join(keys)
        vals = ','.join(vals)
        
        cmd = f"INSERT INTO vpnosint_business_to_twitter_db ({keys}) VALUES ({vals})"
        print(f"cmd={cmd}")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(cmd)
        keys = []
        vals = []
        if 'fb_profile_name' in data and len(data['fb_profile_name']) > 0:
            fb_profile_name = data['fb_profile_name']
            keys.append("fb_profile_name")
            vals.append(f"'{fb_profile_name}'")
        if 'fb_follower_count' in data and len(data['fb_follower_count']) > 0:
            fb_follower_count = data['fb_follower_count']
            keys.append("fb_follower_count")
            vals.append(f"{fb_follower_count}")
        if 'fb_location' in data and len(data['fb_location']) > 0:
            fb_location = data['fb_location']
            keys.append("fb_location")
            vals.append(fb_location)
        if 'fb_joined_date' in data and len(data['fb_joined_date']) > 0:
            fb_joined_date = data['fb_joined_date']
            keys.append(f"'{fb_joined_date}'")
            vals.append(fb_joined_date)
        keys = ','.join(keys)
        vals = ','.join(vals)
        cmd = f"INSERT INTO vpnosint_business_to_facebook_db ({keys}) VALUES ({vals})"
        cur.execute(cmd)
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'ok' : True, "statusText" : "Company Successfully Added."}) 
    else:
        return jsonify({"ok" : False, "statusText" : "Cannot create existing company" })

@app.route('/api/update_social_media/<int:company_id>', methods=['PUT','POST'])
def update_social_media(company_id):
    """
    Create a new Social Media,

    Model:

    First, check if the data is there, if it's not, create it and then add it
    """
    data = request.json
    print(f"/api/update_social_media - data={data}")
    return jsonify({"ok": True})


# END - CRUD for social media transparency
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

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main() # app.run(debug=True)

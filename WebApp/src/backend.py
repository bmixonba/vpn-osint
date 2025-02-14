from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, url_for
import datetime

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
            keys.append('incorporation_date')
            vals.append(f"'{incorporation_date}'")
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

    RAN - api/update_business/11
    RAN - data={'company_id': '11', 'company_name': 'Test business 1 update', 'address': '', 'latitude': '', 'longitude': '', 'incorporation_date': ''}

    """
    data = request.json
    print(f"RAN - api/update_business/{company_id}")
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

@app.route('/api/create_open_corporates', methods=['POST'])
def create_open_corporates():
    """ """
    data = request.json
    print(f"RAN - api/create_open_corporates/{company_id}")
    return _create_open_corporates(data)

def _create_open_corporates(data):
    """
    Create a new business
    """
    data = request.json
    company_id = data['company_id']
    print(f"RAN _create_open_corporates(data={data})")
    keys = []
    vals = []
    """
    company_id: document.getElementById('companySubmit').value,
    oc_query_string: document.getElementById('oc_query_string').value,
    oc_url: document.getElementById('oc_url').value,
    oc_company_number: document.getElementById('oc_company_number').value,
    oc_status: document.getElementById('oc_status').value,
    oc_incorporation_date: document.getElementById('oc_incorporation_date').value,
    oc_company_type: document.getElementById('oc_company_type').value,
    oc_jurisdiction: document.getElementById('oc_jurisdiction').value,
    oc_registered_address_name: document.getElementById('oc_registered_address_name').value,
    oc_registered_address_street: document.getElementById('oc_registered_address_street').value,
    oc_registered_address_city: document.getElementById('oc_registered_address_city').value,
    oc_registered_address_state: document.getElementById('oc_registered_address_state').value,
    oc_registered_address_country: document.getElementById('oc_registered_address_country').value,
    oc_registered_address_zip: document.getElementById('oc_registered_address_zip').value,
    oc_director_officer: document.getElementById('oc_director_officer').value,
    oc_data_source_last_updated: document.getElementById('oc_data_source_last_updated').value,
    oc_data_source_last_changed: document.getElementById('oc_data_source_last_changed').value,
    oc_data_source_url: document.getElementById('oc_data_source_url').value

    """
    print(f"RAN _create_open_corporates(data={data}), company_id={company_id}, type(company_id)={type(company_id)}")
    update_called = data["update_called"]
    if update_called or (company_id == -1 or company_id == '-1'):

        runCmd = False
        print(f"IF == TRUE : 1. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_query_string' in data and len(data['oc_query_string']) > 0:
            oc_query_string = data['oc_query_string']
            keys.append("oc_query_string")
            vals.append(f"'{oc_query_string}'")
            runCmd = True
        print(f"IF == TRUE : 2. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_url' in data and len(data['oc_url']) > 0:
            oc_url = data['oc_url']
            keys.append("oc_url")
            vals.append(f"'{oc_url}'")
            runCmd = True
        print(f"IF == TRUE : 3. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_company_number' in data and len(data['oc_company_number']) > 0:
            oc_company_number = data['oc_company_number']
            keys.append("oc_company_number")
            vals.append(oc_company_number)
            runCmd = True
        print(f"IF == TRUE : 4. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_status' in data and len(data['oc_status']) > 0:
            oc_status = data['oc_status']
            keys.append("oc_status")
            vals.append(f"'{oc_status}'")
            runCmd = True
        print(f"IF == TRUE : 5. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_incorporation_date' in data and len(data['oc_incorporation_date']) > 0:
            oc_incorporation_date = data['oc_incorporation_date']
            keys.append('oc_incorporation_date')
            vals.append(f"'{oc_incorporation_date}'")
            runCmd = True
        print(f"IF == TRUE : 6. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_company_type' in data and len(data['oc_company_type']) > 0:
            oc_company_type = data['oc_company_type']
            keys.append("oc_company_type")
            vals.append(f"'{oc_company_type}'")
            runCmd = True
        print(f"IF == TRUE : 7. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_jurisdication' in data and len(data['oc_jurisdication']) > 0:
            oc_jurisdication = data['oc_jurisdication']
            keys.append("oc_jurisdication")
            vals.append(f"'{oc_jurisdication}'")
            runCmd = True
        print(f"IF == TRUE : 8. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_registered_address_name' in data and len(data['oc_registered_address_name']) > 0:
            oc_registered_address_name = data['oc_registered_address_name']
            keys.append("oc_registered_address_name")
            vals.append(f"'{oc_registered_address_name}'")
            runCmd = True
        print(f"IF == TRUE : 9. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_registered_address_street' in data and len(data['oc_registered_address_street']) > 0:
            oc_registered_address_street = data['oc_registered_address_street']
            keys.append("oc_registered_address_street")
            vals.append(f"'{oc_registered_address_street}'")
            runCmd = True
        print(f"IF == TRUE : 10. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_registered_address_city' in data and len(data['oc_registered_address_city']) > 0:
            oc_registered_address_city = data['oc_registered_address_city']
            keys.append("oc_registered_address_city")
            vals.append(f"'{oc_registered_address_city}'")
            runCmd = True
        print(f"IF == TRUE : 11. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_registered_address_state' in data and len(data['oc_registered_address_state']) > 0:
            oc_registered_address_state = data['oc_registered_address_state']
            keys.append("oc_registered_address_state")
            vals.append(f"'{oc_registered_address_state}'")
            runCmd = True
        print(f"IF == TRUE : 12. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_registered_address_country' in data and len(data['oc_registered_address_country']) > 0:
            oc_registered_address_country = data['oc_registered_address_country']
            keys.append("oc_registered_address_country")
            vals.append(f"'{oc_registered_address_country}'")
            runCmd = True
        print(f"IF == TRUE : 13. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_registered_address_zip' in data and len(data['oc_registered_address_zip']) > 0:
            oc_registered_address_zip = data['oc_registered_address_zip']
            keys.append("oc_registered_address_zip")
            vals.append(f"{oc_registered_address_zip}")
            runCmd = True
        print(f"IF == TRUE : 14. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_director_officer' in data and len(data['oc_director_officer']) > 0:
            oc_director_officer = data['oc_director_officer']
            keys.append("oc_director_officer")
            vals.append(f"'{oc_director_officer}'")
            runCmd = True
        print(f"IF == TRUE : 15. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_data_source_last_updated' in data and len(data['oc_data_source_last_updated']) > 0:
            oc_data_source_last_updated = data['oc_data_source_last_updated']
            keys.append("oc_data_source_last_updated")
            vals.append(f"'{oc_data_source_last_updated}'")
            runCmd = True
        print(f"IF == TRUE : 16. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_data_source_last_changed' in data and len(data['oc_data_source_last_changed']) > 0:
            oc_data_source_last_changed = data['oc_data_source_last_changed']
            keys.append("oc_data_source_last_changed")
            vals.append(f"'{oc_data_source_last_changed}'")
            runCmd = True
        print(f"IF == TRUE : 17. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_data_source_url' in data and len(data['oc_data_source_url']) > 0:
            oc_data_source_url = data['oc_data_source_url']
            keys.append("oc_data_source_url")
            vals.append(f"'{oc_data_source_url}'")
            runCmd = True

        print(f"IF == TRUE : 18. company_id={company_id}, type(company_id)={type(company_id)}")
        if runCmd:
            keys.append("business_id")
            vals.append(f"'{company_id}'")
            oc_timestamp = datetime.datetime.now().isoformat()
            keys.append("oc_timestamp")
            vals.append(f"'{oc_timestamp}'")

        print(f"IF == TRUE : 19. company_id={company_id}, type(company_id)={type(company_id)}")
        keys = ','.join(keys)
        vals = ','.join(vals)
        cmd = f"INSERT INTO vpnosint_business_open_corporates_db ({keys}) VALUES ({vals})"
        print(f"cmd={cmd}")

        conn = get_db_connection()
        cur = conn.cursor()
        if runCmd:
            cur.execute(cmd)
            conn.commit()
        cur.close()
        conn.close()
        return jsonify({'ok' : True, "statusText" : "Open Corporates Info Successfully Added."}) 
    else:
        print(f"ELSE == TRUE : 5. company_id={company_id}, type(company_id)={type(company_id)}")
        return jsonify({"ok" : False, "statusText" : "Open Corporates Info create existing company" })


@app.route('/api/update_open_corporates/<int:company_id>', methods=['PUT'])
def update_open_corporates(company_id):
    """Update existing company information.

    notes:

    RAN - api/update_open_corporates/11
    RAN - data={'company_id': '11', 'company_name': 'Test business 1 update', 'address': '', 'latitude': '', 'longitude': '', 'incorporation_date': ''}

    """
    data = request.json
    print(f"RAN 1. api/update_open_corporates/{company_id}")
    print(f"RAN 2. data={data}")

    update_cmd = []
    company_id = data["company_id"]
    print(f"company_id={company_id}, type(company_id)={type(company_id)}")
    if company_id == -1 or company_id == '-1':
        print(f"RAN if 3. api/update_open_corporates/{company_id}")
        return jsonify({"ok" : False, "statusText" : "Cannot update unknown company" })
    else:
        try:
            print(f"RAN else 3. api/update_open_corporates/{company_id}")
            conn = get_db_connection()
            cur = conn.cursor()
            oc_check_query = """
                SELECT EXISTS (
                    SELECT 1 FROM  vpnosint_business_open_corporates_db WHERE business_id = %s
                );
            """

            print(f"RAN else 4. api/update_open_corporates/{company_id}")
            cur.execute(oc_check_query, (company_id,))
            oc_exists = cur.fetchone()[0]  # Fetch the result (True or False)

            print(f"RAN else 5. api/update_open_corporates/{company_id}, oc_exists={oc_exists} ")
            keys = []
            vals = []
            if not oc_exists:
                print(f"RAN 6. api/update_open_corporates/{company_id}, if not oc_exists={not oc_exists}")
                data["update_called"] = True
                return _create_open_corporates(data)
            else:
                print(f"RAN 7. api/update_open_corporates/{company_id}, else not oc_exists={not oc_exists}")
                runCmd = False
                update_cmd = []
                if 'oc_query_string' in data and len(data['oc_query_string']) > 0:
                    oc_query_string = data['oc_query_string']
                    tmp = f"oc_query_string='{oc_query_string}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_url' in data and len(data['oc_url']) > 0:
                    oc_url = data['oc_url']
                    tmp = f"oc_url='{oc_url}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_company_number' in data and len(data['oc_company_number']) > 0:
                    oc_company_number = data['oc_company_number']
                    keys.append("oc_company_number")
                    vals.append(oc_company_number)
                    tmp = f"oc_company_number={oc_company_number}"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_status' in data and len(data['oc_status']) > 0:
                    oc_status = data['oc_status']
                    tmp = f"oc_status='{oc_status}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_incorporation_date' in data and len(data['oc_incorporation_date']) > 0:
                    oc_incorporation_date = data['oc_incorporation_date']
                    tmp = f"oc_incorporation_date='{oc_incorporation_date}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_company_type' in data and len(data['oc_company_type']) > 0:
                    oc_company_type = data['oc_company_type']
                    tmp = f"oc_company_type='{oc_company_type}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_jurisdication' in data and len(data['oc_jurisdication']) > 0:
                    oc_jurisdication = data['oc_jurisdication']
                    tmp = f"oc_jurisdication='{oc_jurisdication}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_registered_address_name' in data and len(data['oc_registered_address_name']) > 0:
                    oc_registered_address_name = data['oc_registered_address_name']
                    tmp = f"oc_registered_address_name='{oc_registered_address_name}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_registered_address_street' in data and len(data['oc_registered_address_street']) > 0:
                    oc_registered_address_street = data['oc_registered_address_street']
                    tmp = f"oc_registered_address_street='{oc_registered_address_street}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_registered_address_city' in data and len(data['oc_registered_address_city']) > 0:
                    oc_registered_address_city = data['oc_registered_address_city']
                    tmp = f"oc_registered_address_city='{oc_registered_address_city}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_registered_address_state' in data and len(data['oc_registered_address_state']) > 0:
                    oc_registered_address_state = data['oc_registered_address_state']
                    tmp = f"oc_registered_address_state='{oc_registered_address_state}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_registered_address_country' in data and len(data['oc_registered_address_country']) > 0:
                    oc_registered_address_country = data['oc_registered_address_country']
                    tmp = f"oc_registered_address_country='{oc_registered_address_country}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_registered_address_zip' in data and len(data['oc_registered_address_zip']) > 0:
                    oc_registered_address_zip = data['oc_registered_address_zip']
                    tmp = f"oc_registered_address_zip='{oc_registered_address_zip}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_director_officer' in data and len(data['oc_director_officer']) > 0:
                    oc_director_officer = data['oc_director_officer']
                    tmp = f"oc_director_officer='{oc_director_officer}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_data_source_last_updated' in data and len(data['oc_data_source_last_updated']) > 0:
                    oc_data_source_last_updated = data['oc_data_source_last_updated']
                    tmp = f"oc_data_source_last_updated='{oc_data_source_last_updated}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_data_source_last_changed' in data and len(data['oc_data_source_last_changed']) > 0:
                    oc_data_source_last_changed = data['oc_data_source_last_changed']
                    tmp = f"oc_data_source_last_changed='{oc_data_source_last_changed}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_data_source_url' in data and len(data['oc_data_source_url']) > 0:
                    oc_data_source_url = data['oc_data_source_url']
                    tmp = f"oc_data_source_url='{oc_data_source_url}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if runCmd: 
                    oc_timestamp = datetime.datetime.now().isoformat()
                    tmp = f"oc_timestamp='{oc_timestamp}'"
                    update_cmd.append(tmp)
                    tmp = f"business_id='{company_id}'"
                    update_cmd.append(tmp)

                update_cmd = ','.join(update_cmd)
                cmd = f"UPDATE vpnosint_business_open_corporates_db SET {update_cmd} WHERE business_id={company_id};"
                print(f"cmd={cmd}")
                print(f"RAN - api/update_open_corporates/{company_id}, else not oc_exists={not oc_exists}, runCmd={runCmd}")

                if runCmd: 
                    cur.execute(cmd)
                    conn.commit()

            cur.close()
            conn.close()
            return jsonify({"ok" : True, "statusText" : "Open Corporates Info Successfully Updated."}) 
        except Exception as e:
           print(f"RAN - Exception - {e} - api/update_open_corporates/{company_id}")
        finally:
           print(f"RAN - Finally - api/update_open_corporates/{company_id}, if not oc_exists")
           return jsonify({"ok" : False, "statusText" : "Open Corporates Info Failed Updated."}) 

# BEGIN : Open Corporates Trademark Info

@app.route('/api/create_oc_trademarks', methods=['POST'])
def create_oc_trademarks():
    """ TODO: Fix this - Currently, each VPN provider can only have one
    trademark entry. They should be able to have mutliple entries. They should
    also be able to update existing entries. THis should be based on the
    trademark number or something.
    """
    data = request.json
    print(f"RAN - api/create_oc_trademarks/{company_id}")
    return _create_oc_trademarks(data)

def _create_oc_trademarks(data):
    """ 
    rates_trademark_registration_id_seq'::regclass)
     business_id                        | integer                     |           |          | 
     oc_mark_text                       | character varying(255)      |           |          | 
     oc_image_url                       | character varying(255)      |           |          | 
     oc_register                        | character varying(255)      |           |          | 
     oc_nice_classification             | character varying(255)      |           |          | 
     oc_registration_date               | timestamp without time zone |           |          | 
     oc_expiry                          | timestamp without time zone |           |          | 
     oc_trademark_url                   | text                        |           |          | 
     oc_source_url                      | text                        |           |          | 
     oc_holder_name                     | text                        |           |          | 
     oc_holder_address_street           | character varying(255)      |           |          | 
     oc_holder_address_city             | character varying(255)      |           |          | 
     oc_holder_address_state            | character varying(255)      |           |          | 
     oc_holder_address_country          | character varying(255)      |           |          | 
     oc_holder_address_zip              | integer                     |           |          | 
     oc_holder_latitude                 | integer                     |           |          | 
     oc_holder_longitude                | integer                     |           |          | 
     oc_correspondent_name              | text                        |           |          | 
     oc_correspondent_address_street    | character varying(255)      |           |          | 
     oc_correspondent_address_city      | character varying(255)      |           |          | 
     oc_correspondent_address_state     | character varying(255)      |           |          | 
     oc_correspondent_address_country   | character varying(255)      |           |          | 
     oc_correspondent_address_latitude  | integer                     |           |          | 
     oc_correspondent_address_longitude | integer                     |           |          | 
     oc_trademark_notes                 | text                        |           |          | 
     oc_tm_timestamp                    | timestamp without time zone |           |          | 


    """
    data = request.json
    company_id = data['company_id']
    print(f"RAN _create_oc_trademarks(data={data})")
    keys = []
    vals = []
    """
    """
    print(f"RAN _create_oc_trademarks(data={data}), company_id={company_id}, type(company_id)={type(company_id)}")
    update_called = data["update_called"]
    if update_called or (company_id == -1 or company_id == '-1'):

        runCmd = False
        print(f"IF == TRUE : 2. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_mark_text' in data and len(data['oc_mark_text']) > 0:
            oc_mark_text = data['oc_mark_text']
            keys.append("oc_mark_text")
            vals.append(f"'{oc_mark_text}'")
            runCmd = True
        print(f"IF == TRUE : 3. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_image_url' in data and len(data['oc_image_url']) > 0:
            oc_image_url = data['oc_image_url']
            keys.append("oc_image_url")
            vals.append(f"'{oc_image_url}'")
            runCmd = True
        print(f"IF == TRUE : 4. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_register' in data and len(data['oc_register']) > 0:
            oc_register = data['oc_register']
            keys.append("oc_register")
            vals.append(f"'{oc_register}'")
            runCmd = True
        print(f"IF == TRUE : 5. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_nice_classication' in data and len(data['oc_nice_classication']) > 0:
            oc_nice_classication = data['oc_nice_classication']
            keys.append('oc_nice_classication')
            vals.append(f"'{oc_nice_classication}'")
            runCmd = True
        print(f"IF == TRUE : 6. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_expiry' in data and len(data['oc_expiry']) > 0:
            oc_expiry = data['oc_expiry']
            keys.append("oc_expiry")
            vals.append(f"'{oc_expiry}'")
            runCmd = True
        print(f"IF == TRUE : 7. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_trademark_url' in data and len(data['oc_trademark_url']) > 0:
            oc_trademark_url = data['oc_trademark_url']
            keys.append("oc_trademark_url")
            vals.append(f"'{oc_trademark_url}'")
            runCmd = True
        print(f"IF == TRUE : 8. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_source_url' in data and len(data['oc_source_url']) > 0:
            oc_source_url = data['oc_source_url']
            keys.append("oc_source_url")
            vals.append(f"'{oc_source_url}'")
            runCmd = True
        print(f"IF == TRUE : 9. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_holder_name' in data and len(data['oc_holder_name']) > 0:
            oc_holder_name = data['oc_holder_name']
            keys.append("oc_holder_name")
            vals.append(f"'{oc_holder_name}'")
            runCmd = True
        print(f"IF == TRUE : 10. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_holder_address_street' in data and len(data['oc_holder_address_street']) > 0:
            oc_holder_address_street = data['oc_holder_address_street']
            keys.append("oc_holder_address_street")
            vals.append(f"'{oc_holder_address_street}'")
            runCmd = True
        print(f"IF == TRUE : 11. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_holder_address_city' in data and len(data['oc_holder_address_city']) > 0:
            oc_holder_address_city = data['oc_holder_address_city']
            keys.append("oc_holder_address_city")
            vals.append(f"'{oc_holder_address_city}'")
            runCmd = True
        print(f"IF == TRUE : 12. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_holder_address_state' in data and len(data['oc_holder_address_state']) > 0:
            oc_holder_address_state = data['oc_holder_address_state']
            keys.append("oc_holder_address_state")
            vals.append(f"'{oc_holder_address_state}'")
            runCmd = True
        print(f"IF == TRUE : 13. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_holder_address_country' in data and len(data['oc_holder_address_country']) > 0:
            oc_holder_address_country = data['oc_holder_address_country']
            keys.append("oc_holder_address_country")
            vals.append(f"{oc_holder_address_country}")
            runCmd = True
        print(f"IF == TRUE : 14. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_holder_address_zip' in data and len(data['oc_holder_address_zip']) > 0:
            oc_holder_address_zip = data['oc_holder_address_zip']
            keys.append("oc_holder_address_zip")
            vals.append(f"{oc_holder_address_zip}")
            runCmd = True
        print(f"IF == TRUE : 15. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_holder_latitude' in data and len(data['oc_holder_latitude']) > 0:
            oc_holder_latitude = data['oc_holder_latitude']
            keys.append("oc_holder_latitude")
            vals.append(f"{oc_holder_latitude}")
            runCmd = True
        print(f"IF == TRUE : 16. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_holder_longitude' in data and len(data['oc_holder_longitude']) > 0:
            oc_holder_longitude = data['oc_holder_longitude']
            keys.append("oc_holder_longitude")
            vals.append(f"'{oc_holder_longitude}'")
            runCmd = True
        print(f"IF == TRUE : 17. company_id={company_id}, type(company_id)={type(company_id)}")
        if 'oc_correspondent_name' in data and len(data['oc_correspondent_name']) > 0:
            oc_correspondent_name = data['oc_correspondent_name']
            keys.append("oc_correspondent_name")
            vals.append(f"'{oc_correspondent_name}'")
            runCmd = True

        if 'oc_correspondent_address_street' in data and len(data['oc_correspondent_address_street']) > 0:
            oc_correspondent_address_street = data['oc_correspondent_address_street']
            keys.append("oc_correspondent_address_street")
            vals.append(f"'{oc_correspondent_address_street}'")
            runCmd = True
        if 'oc_correspondent_address_city' in data and len(data['oc_correspondent_address_city']) > 0:
            oc_correspondent_address_city = data['oc_correspondent_address_city']
            keys.append("oc_correspondent_address_city")
            vals.append(f"'{oc_correspondent_address_city}'")
            runCmd = True
        if 'oc_correspondent_address_state' in data and len(data['oc_correspondent_address_state']) > 0:
            oc_correspondent_address_state = data['oc_correspondent_address_state']
            keys.append("oc_correspondent_address_state")
            vals.append(f"'{oc_correspondent_address_state}'")
            runCmd = True
        if 'oc_correspondent_address_country' in data and len(data['oc_correspondent_address_country']) > 0:
            oc_correspondent_address_country = data['oc_correspondent_address_country']
            keys.append("oc_correspondent_address_country")
            vals.append(f"'{oc_correspondent_address_country}'")
            runCmd = True
        if 'oc_correspondent_address_latitude' in data and len(data['oc_correspondent_address_latitude']) > 0:
            oc_correspondent_address_latitude = data['oc_correspondent_address_latitude']
            keys.append("oc_correspondent_address_latitude")
            vals.append(f"{oc_correspondent_address_latitude}")
            runCmd = True
        if 'oc_correspondent_address_longitude' in data and len(data['oc_correspondent_address_longitude']) > 0:
            oc_correspondent_address_longitude = data['oc_correspondent_address_longitude']
            keys.append("oc_correspondent_address_longitude")
            vals.append(f"{oc_correspondent_address_longitude}")
            runCmd = True
        if 'oc_trademark_notes' in data and len(data['oc_trademark_notes']) > 0:
            oc_trademark_notes = data['oc_trademark_notes']
            keys.append("oc_trademark_notes")
            vals.append(f"{oc_trademark_notes}")
            runCmd = True


        print(f"IF == TRUE : 18. company_id={company_id}, type(company_id)={type(company_id)}")
        if runCmd:
            keys.append("business_id")
            vals.append(f"'{company_id}'")
            oc_tm_timestamp = datetime.datetime.now().isoformat()
            keys.append("oc_tm_timestamp")
            vals.append(f"'{oc_tm_timestamp}'")

        print(f"IF == TRUE : 19. company_id={company_id}, type(company_id)={type(company_id)}")
        keys = ','.join(keys)
        vals = ','.join(vals)
        cmd = f"INSERT INTO vpnosint_business_open_corporates_trademark_registration_db ({keys}) VALUES ({vals})"
        print(f"cmd={cmd}")

        conn = get_db_connection()
        cur = conn.cursor()
        if runCmd:
            cur.execute(cmd)
            conn.commit()
        cur.close()
        conn.close()
        return jsonify({'ok' : True, "statusText" : "Open Corporates Info Successfully Added."}) 
    else:
        print(f"ELSE == TRUE : 5. company_id={company_id}, type(company_id)={type(company_id)}")
        return jsonify({"ok" : False, "statusText" : "Open Corporates Info create existing company" })


@app.route('/api/update_oc_trademarks/<int:company_id>', methods=['PUT'])
def update_oc_trademarks(company_id):
    """Update existing company information.

    notes:

    RAN - api/update_oc_trademarks/11
    RAN - data={'company_id': '11', 'company_name': 'Test business 1 update', 'address': '', 'latitude': '', 'longitude': '', 'incorporation_date': ''}

    """
    data = request.json
    print(f"RAN 1. api/update_oc_trademarks/{company_id}")
    print(f"RAN 2. data={data}")

    update_cmd = []
    company_id = data["company_id"]
    print(f"company_id={company_id}, type(company_id)={type(company_id)}")
    if company_id == -1 or company_id == '-1':
        print(f"RAN if 3. api/update_oc_trademarks/{company_id}")
        return jsonify({"ok" : False, "statusText" : "Cannot update unknown company" })
    else:
        try:
            print(f"RAN else 3. api/update_oc_trademarks/{company_id}")
            conn = get_db_connection()
            cur = conn.cursor()
            oc_check_query = """
                SELECT EXISTS (
                    SELECT 1 FROM  vpnosint_business_open_corporates_trademark_registration_db WHERE business_id = %s
                );
            """

            print(f"RAN else 4. api/update_oc_trademarks/{company_id}")
            cur.execute(oc_check_query, (company_id,))
            oc_exists = cur.fetchone()[0]  # Fetch the result (True or False)

            print(f"RAN else 5. api/update_oc_trademarks/{company_id}, oc_exists={oc_exists} ")
            keys = []
            vals = []
            if not oc_exists:
                print(f"RAN 6. api/update_oc_trademarks/{company_id}, if not oc_exists={not oc_exists}")
                data["update_called"] = True
                return _create_oc_trademarks(data)
            else:
                print(f"RAN 7. api/update_oc_trademarks/{company_id}, else not oc_exists={not oc_exists}")
                runCmd = False
                update_cmd = []
                if 'oc_mark_text' in data and len(data['oc_mark_text']) > 0:
                    oc_mark_text = data['oc_mark_text']
                    tmp = f"oc_mark_text='{oc_mark_text}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 3. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_image_url' in data and len(data['oc_image_url']) > 0:
                    oc_image_url = data['oc_image_url']
                    tmp = f"oc_image_url='{oc_image_url}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 4. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_register' in data and len(data['oc_register']) > 0:
                    oc_register = data['oc_register']
                    tmp = f"oc_register='{oc_register}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 5. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_nice_classication' in data and len(data['oc_nice_classication']) > 0:
                    oc_nice_classication = data['oc_nice_classication']
                    tmp = f"oc_nice_classication='{oc_nice_classication}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 6. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_expiry' in data and len(data['oc_expiry']) > 0:
                    oc_expiry = data['oc_expiry']
                    tmp = f"oc_expiry='{oc_expiry}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 7. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_trademark_url' in data and len(data['oc_trademark_url']) > 0:
                    oc_trademark_url = data['oc_trademark_url']
                    tmp = f"oc_trademark_url='{oc_trademark_url}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 8. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_source_url' in data and len(data['oc_source_url']) > 0:
                    oc_source_url = data['oc_source_url']
                    tmp = f"oc_source_url='{oc_source_url}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 9. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_holder_name' in data and len(data['oc_holder_name']) > 0:
                    oc_holder_name = data['oc_holder_name']
                    tmp = f"oc_holder_name='{oc_holder_name}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 10. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_holder_address_street' in data and len(data['oc_holder_address_street']) > 0:
                    oc_holder_address_street = data['oc_holder_address_street']
                    tmp = f"oc_holder_address_street='{oc_holder_address_street}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 11. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_holder_address_city' in data and len(data['oc_holder_address_city']) > 0:
                    oc_holder_address_city = data['oc_holder_address_city']
                    tmp = f"oc_holder_address_city='{oc_holder_address_city}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 12. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_holder_address_state' in data and len(data['oc_holder_address_state']) > 0:
                    oc_holder_address_state = data['oc_holder_address_state']
                    tmp = f"oc_holder_address_state='{oc_holder_address_state}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 13. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_holder_address_country' in data and len(data['oc_holder_address_country']) > 0:
                    oc_holder_address_country = data['oc_holder_address_country']
                    tmp = f"oc_holder_address_country='{oc_holder_address_country}'"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 14. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_holder_address_zip' in data and len(data['oc_holder_address_zip']) > 0:
                    oc_holder_address_zip = data['oc_holder_address_zip']
                    tmp = f"oc_holder_address_zip={oc_holder_address_zip}"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 15. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_holder_latitude' in data and len(data['oc_holder_latitude']) > 0:
                    oc_holder_latitude = data['oc_holder_latitude']
                    tmp = f"oc_holder_latitude={oc_holder_latitude}"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 16. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_holder_longitude' in data and len(data['oc_holder_longitude']) > 0:
                    oc_holder_longitude = data['oc_holder_longitude']
                    tmp = f"oc_holder_longitude={oc_holder_longitude}"
                    update_cmd.append(tmp)
                    runCmd = True
                print(f"IF == TRUE : 17. company_id={company_id}, type(company_id)={type(company_id)}")
                if 'oc_correspondent_name' in data and len(data['oc_correspondent_name']) > 0:
                    oc_correspondent_name = data['oc_correspondent_name']
                    tmp = f"oc_correspondent_name='{oc_correspondent_name}'"
                    update_cmd.append(tmp)
                    runCmd = True

                if 'oc_correspondent_address_street' in data and len(data['oc_correspondent_address_street']) > 0:
                    oc_correspondent_address_street = data['oc_correspondent_address_street']
                    tmp = f"oc_correspondent_address_street='{oc_correspondent_address_street}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_correspondent_address_city' in data and len(data['oc_correspondent_address_city']) > 0:
                    oc_correspondent_address_city = data['oc_correspondent_address_city']
                    tmp = f"oc_correspondent_address_city='{oc_correspondent_address_city}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_correspondent_address_state' in data and len(data['oc_correspondent_address_state']) > 0:
                    oc_correspondent_address_state = data['oc_correspondent_address_state']
                    tmp = f"oc_correspondent_address_state='{oc_correspondent_address_state}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_correspondent_address_country' in data and len(data['oc_correspondent_address_country']) > 0:
                    oc_correspondent_address_country = data['oc_correspondent_address_country']
                    tmp = f"oc_correspondent_address_country='{oc_correspondent_address_country}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_correspondent_address_latitude' in data and len(data['oc_correspondent_address_latitude']) > 0:
                    oc_correspondent_address_latitude = data['oc_correspondent_address_latitude']
                    tmp = f"oc_correspondent_address_latitude='{oc_correspondent_address_latitude}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_correspondent_address_longitude' in data and len(data['oc_correspondent_address_longitude']) > 0:
                    oc_correspondent_address_longitude = data['oc_correspondent_address_longitude']
                    tmp = f"oc_correspondent_address_longitude='{oc_correspondent_address_longitude}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'oc_trademark_notes' in data and len(data['oc_trademark_notes']) > 0:
                    oc_trademark_notes = data['oc_trademark_notes']
                    tmp = f"oc_trademark_notes='{oc_trademark_notes}'"
                    update_cmd.append(tmp)
                    runCmd = True

                if runCmd: 
                    oc_tm_timestamp = datetime.datetime.now().isoformat()
                    tmp = f"oc_tm_timestamp='{oc_tm_timestamp}'"
                    update_cmd.append(tmp)
                    tmp = f"business_id='{company_id}'"
                    update_cmd.append(tmp)

                update_cmd = ','.join(update_cmd)
                cmd = f"UPDATE vpnosint_business_open_corporates_trademark_registration_db SET {update_cmd} WHERE business_id={company_id};"
                print(f"cmd={cmd}")
                print(f"RAN - api/update_oc_trademarks/{company_id}, else not oc_exists={not oc_exists}, runCmd={runCmd}")

                if runCmd: 
                    cur.execute(cmd)
                    conn.commit()

            cur.close()
            conn.close()
            return jsonify({"ok" : True, "statusText" : "Open Corporates Trademark Info Successfully Updated."}) 
        except Exception as e:
           print(f"RAN - Exception - {e} - api/update_oc_trademarks/{company_id}")
        finally:
           print(f"RAN - Finally - api/update_oc_trademarks/{company_id}, if not oc_exists")
           return jsonify({"ok" : False, "statusText" : "Open Corporates Trademark Info Failed Updated."}) 

# END: Business Transparency OC Trademark CRUD API endpoints

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
        return jsonify({'ok' : False, 'statusText' : 'Cannot create social media profile if VPN provider doesnt exist first.'})
    else:
        """
        """
        keys = []
        vals = []
        runCmd = False
        if 'x_profile_name' in data and len(data['x_profile_name']) > 0:
            x_profile_name = data['x_profile_name']
            keys.append("profile_name")
            vals.append(f"'{x_profile_name}'")
            runCmd = True
        if 'x_follower_count' in data and len(data['x_follower_count']) > 0:
            x_follower_count = data['x_follower_count']
            keys.append("follower_count")
            vals.append(f"{x_follower_count}")
            runCmd = True
        if 'x_following_count' in data and len(data['x_following_count']) > 0:
            x_following_count = data['x_following_count']
            keys.append("following_count")
            vals.append(x_following_count)
            runCmd = True
        if 'x_location' in data and len(data['x_location']) > 0:
            x_location = data['x_location']
            keys.append("location")
            vals.append(f"'{x_location}'")
            runCmd = True
        if 'x_joined_date' in data and len(data['x_joined_date']) > 0:
            x_joined_date = data['x_joined_date']
            keys.append("joined_date")
            vals.append(f"'{x_joined_date}'")
            runCmd = True
            """
            fb_profile_name
            fb_follower_count
            fb_location
            fb_joined_date
            """

        keys = ','.join(keys)
        vals = ','.join(vals)
        if runCmd: 
            keys.append("business_id")
            vals.append(company_id)
        
        cmd = f"INSERT INTO vpnosint_business_to_twitter_db ({keys}) VALUES ({vals})"
        print(f"cmd={cmd}")

        conn = get_db_connection()
        cur = conn.cursor()
        if runCmd: 
            cur.execute(cmd)
        keys = []
        vals = []
        runCmd = False
        if 'fb_profile_name' in data and len(data['fb_profile_name']) > 0:
            fb_profile_name = data['fb_profile_name']
            keys.append("profile_name")
            vals.append(f"'{fb_profile_name}'")
            runCmd = True
        if 'fb_follower_count' in data and len(data['fb_follower_count']) > 0:
            fb_follower_count = data['fb_follower_count']
            keys.append("follower_count")
            vals.append(f"{fb_follower_count}")
            runCmd = True
        if 'fb_location' in data and len(data['fb_location']) > 0:
            fb_location = data['fb_location']
            keys.append("location")
            vals.append(f"'{fb_location}'")
            runCmd = True
        if 'fb_joined_date' in data and len(data['fb_joined_date']) > 0:
            fb_joined_date = data['fb_joined_date']
            keys.append('joined_date')
            vals.append(f"'{fb_joined_date}'")
            runCmd = True
        keys = ','.join(keys)
        vals = ','.join(vals)
        if runCmd: 
            keys.append("business_id")
            vals.append(company_id)
        print(f"keys={keys}, vals={vals}")
        cmd = f"INSERT INTO vpnosint_business_to_facebook_db ({keys}) VALUES ({vals})"
        if runCmd: 
            cur.execute(cmd)
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'ok' : True, "statusText" : "Company Successfully Added."}) 

@app.route('/api/update_social_media/<int:company_id>', methods=['PUT','POST'])
def update_social_media(company_id):
    """
    Create a new Social Media,

    Model:

    First, check if the data is there, if it's not, create it and then add it
    """
    data = request.json
    company_id = data['company_id']
    print(f"api/update_social_media/, company_id={company_id}, type(company_id)={type(company_id)}")
    if company_id == -1 or company_id == '-1':
        return jsonify({'ok' : False, 'statusText' : 'Cannot update social media provil for unknown VPN provider.'})
    else:
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            twitter_check_query = """
                SELECT EXISTS (
                    SELECT 1 FROM  vpnosint_business_to_twitter_db WHERE business_id = %s
                );
            """
            # Execute the query
            cur.execute(twitter_check_query, (company_id,))
            twitter_exists = cur.fetchone()[0]  # Fetch the result (True or False)

            keys = []
            vals = []
            if not twitter_exists:
                print(f"Entry with ID {company_id} doesn't exists.")

                runCmd = False
                if 'x_profile_name' in data and len(data['x_profile_name']) > 0:
                    x_profile_name = data['x_profile_name']
                    keys.append("profile_name")
                    vals.append(f"'{x_profile_name}'")
                    runCmd = True
                if 'x_follower_count' in data and len(data['x_follower_count']) > 0:
                    x_follower_count = data['x_follower_count']
                    keys.append("follower_count")
                    vals.append(f"{x_follower_count}")
                    runCmd = True
                if 'x_following_count' in data and len(data['x_following_count']) > 0:
                    x_following_count = data['x_following_count']
                    keys.append("following_count")
                    vals.append(x_following_count)
                    runCmd = True
                if 'x_location' in data and len(data['x_location']) > 0:
                    x_location = data['x_location']
                    keys.append("location")
                    vals.append(f"'{x_location}'")
                    runCmd = True
                if 'x_joined_date' in data and len(data['x_joined_date']) > 0:
                    x_joined_date = data['x_joined_date']
                    keys.append("joined_date")
                    vals.append(f"'{x_joined_date}'")
                    runCmd = True
                    """
                    fb_profile_name
                    fb_follower_count
                    fb_location
                    fb_joined_date
                    """
                if runCmd: 
                    keys.append("business_id")
                    vals.append(company_id)

                keys = ','.join(keys)
                vals = ','.join(vals)
                
                cmd = f"INSERT INTO vpnosint_business_to_twitter_db ({keys}) VALUES ({vals});"
                print(f"cmd={cmd}")

                if runCmd: 
                    cur.execute(cmd)
                    conn.commit()
            else:
                """ There is an existing entry, so we just need to update stuff."""
                runCmd = False
                update_cmd = []
                if 'x_profile_name' in data and len(data['x_profile_name']) > 0:
                    x_profile_name = data['x_profile_name']
                    tmp = f"profile_name='{x_profile_name}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'x_follower_count' in data and len(data['x_follower_count']) > 0:
                    x_follower_count = data['x_follower_count']
                    tmp = f"follower_count='{x_follower_count}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'x_following_count' in data and len(data['x_following_count']) > 0:
                    x_following_count = data['x_following_count']
                    tmp = f"following_count='{x_following_count}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'x_location' in data and len(data['x_location']) > 0:
                    x_location = data['x_location']
                    tmp = f"x_location='{x_location}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'x_joined_date' in data and len(data['x_joined_date']) > 0:
                    x_joined_date = data['x_joined_date']
                    tmp = f"joined_date='{x_joined_date}'"
                    update_cmd.append(tmp)
                    runCmd = True
                
                if runCmd: 
                    tmp = f"business_id='{company_id}'"
                    update_cmd.append(tmp)

                update_cmd = ','.join(update_cmd)
                cmd = f"UPDATE vpnosint_business_to_twitter_db SET {update_cmd} WHERE business_id={company_id};"
                print(f"cmd={cmd}")

                if runCmd: 
                    cur.execute(cmd)
                    conn.commit()
                
            keys = []
            vals = []
            runCmd = False

            facebook_check_query = """
                SELECT EXISTS (
                    SELECT 1 FROM  vpnosint_business_to_facebook_db WHERE business_id = %s
                );
            """
            cur.execute(facebook_check_query, (company_id,))
            facebook_exists = cur.fetchone()[0]  # Fetch the result (True or False)

            if not facebook_exists:
                if 'fb_profile_name' in data and len(data['fb_profile_name']) > 0:
                    fb_profile_name = data['fb_profile_name']
                    keys.append("profile_name")
                    vals.append(f"'{fb_profile_name}'")
                    runCmd = True
                if 'fb_follower_count' in data and len(data['fb_follower_count']) > 0:
                    fb_follower_count = data['fb_follower_count']
                    keys.append("follower_count")
                    vals.append(f"{fb_follower_count}")
                    runCmd = True
                if 'fb_location' in data and len(data['fb_location']) > 0:
                    fb_location = data['fb_location']
                    keys.append("location")
                    vals.append(f"'{fb_location}'")
                    runCmd = True
                if 'fb_joined_date' in data and len(data['fb_joined_date']) > 0:
                    fb_joined_date = data['fb_joined_date']
                    keys.append('joined_date')
                    vals.append(f"'{fb_joined_date}'")
                    runCmd = True
                if runCmd: 
                    keys.append("business_id")
                    vals.append(company_id)

                keys = ','.join(keys)
                vals = ','.join(vals)
                print(f"keys={keys}, vals={vals}")
                cmd = f"INSERT INTO vpnosint_business_to_facebook_db ({keys}) VALUES ({vals});"
                if runCmd: 
                    cur.execute(cmd)
                conn.commit()
            else:
                """ There is an existing entry, so we just need to update stuff."""
                runCmd = False
                update_cmd = []
                if 'fb_profile_name' in data and len(data['fb_profile_name']) > 0:
                    fb_profile_name = data['fb_profile_name']
                    tmp = f"profile_name='{fb_profile_name}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'fb_follower_count' in data and len(data['fb_follower_count']) > 0:
                    fb_follower_count = data['fb_follower_count']
                    tmp = f"follower_count='{fb_follower_count}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'fb_following_count' in data and len(data['fb_following_count']) > 0:
                    fb_following_count = data['fb_following_count']
                    tmp = f"following_count='{fb_following_count}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'fb_location' in data and len(data['fb_location']) > 0:
                    fb_location = data['fb_location']
                    tmp = f"location='{fb_location}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'fb_joined_date' in data and len(data['fb_joined_date']) > 0:
                    fb_joined_date = data['fb_joined_date']
                    tmp = f"joined_date='{fb_joined_date}'"
                    update_cmd.append(tmp)
                    runCmd = True
                
                if runCmd: 
                    tmp = f"business_id='{company_id}'"
                    update_cmd.append(tmp)
                update_cmd = ','.join(update_cmd)
                cmd = f"UPDATE vpnosint_business_to_facebook_db SET {update_cmd} WHERE business_id={company_id};"
                print(f"cmd={cmd}")

                if runCmd: 
                    cur.execute(cmd)
                conn.commit()
        except Exception as e:
            print(f"Error checking entry: {e}")
        finally:
            # Close the cursor and connection
            cur.close()
            conn.close()

        return jsonify({'ok' : True, "statusText" : "Company Successfully Added."}) 

# END - CRUD for social media transparency

# BEGIN - CRUD for Network/Domain information

@app.route('/api/create_domain_network', methods=['PUT','POST'])
def create_domain_network():
    """ """
    return jsonify({"ok" : False, "statusText" : "Unimplemented API"})

def _create_domain_network(data):
    """Create a domain/network provifil
    """
    print(f"data={data}")
    print(f"RAN - api/create_domain_network")
    keys = []
    vals = []
    company_id = data['company_id']
    print(f"api/create_domain_network/, company_id={company_id}, type(company_id)={type(company_id)}")
    if company_id == -1 or company_id == '-1':
        return jsonify({'ok' : False,
                        'statusText' : 'Cannot create domain/network profile if VPN provider doesnt exist first.'})
    else:
        """
        """
        keys = []
        vals = []
        runCmd = False
        if 'domain_name' in data and len(data['domain_name']) > 0:
            domain_name = data['domain_name']
            keys.append("domain_name")
            vals.append(f"'{domain_name}'")
            runCmd = True
        if 'domain_address' in data and len(data['domain_address']) > 0:
            domain_address = data['domain_address']
            keys.append("address")
            vals.append(f"'{domain_address}'")
            runCmd = True
        if 'domain_latitude' in data and len(data['domain_latitude']) > 0:
            domain_latitude = data['domain_latitude']
            keys.append("latitude")
            vals.append(domain_latitude)
            runCmd = True
        if 'domain_longitude' in data and len(data['domain_longitude']) > 0:
            domain_longitude = data['domain_longitude']
            keys.append("longitude")
            vals.append(f"{domain_longitude}")
            runCmd = True
        if 'domain_registration_date' in data and len(data['domain_registration_date']) > 0:
            domain_registration_date = data['domain_registration_date']
            keys.append("registration_date")
            vals.append(f"'{domain_registration_date}'")
            runCmd = True
        if 'domain_registrar' in data and len(data['domain_registrar']) > 0:
            domain_registrar = data['domain_registrar']
            keys.append("registrar")
            vals.append(f"'{domain_registrar}'")
            runCmd = True
        if 'domain_registrar_abuse_email' in data and len(data['domain_registrar_abuse_email']) > 0:
            registrar_abuse_email = data['domain_registrar_abuse_email']
            keys.append("registrar_abuse_email")
            vals.append(f"'{registrar_abuse_email}'")
            runCmd = True
        if 'domain_registrar_phone' in data and len(data['domain_registrar_phone']) > 0:
            registrar_phone = data['domain_registrar_phone']
            keys.append("registrar_phone")
            vals.append(f"'{registrar_phone}'")
            runCmd = True
        if 'domain_registrant_name' in data and len(data['domain_registrant_name']) > 0:
            registrant_name = data['domain_registrant_name']
            keys.append("registrant_name")
            vals.append(f"'{registrant_name}'")
            runCmd = True
        if 'domain_registrant_organization' in data and len(data['domain_registrant_organization']) > 0:
            registrant_organization = data['domain_registrant_organization']
            keys.append("registrant_organization")
            vals.append(f"'{registrant_organization}'")
            runCmd = True

        if runCmd: 
            keys.append("business_id")
            vals.append(company_id)
        keys = ','.join(keys)
        vals = ','.join(vals)
        
        cmd = f"INSERT INTO vpnosint_domain_db ({keys}) VALUES ({vals});"
        print(f"cmd={cmd}")

        conn = get_db_connection()
        cur = conn.cursor()
        if runCmd: 
            cur.execute(cmd)
        keys = []
        vals = []
        runCmd = False
        if 'fb_profile_name' in data and len(data['fb_profile_name']) > 0:
            fb_profile_name = data['fb_profile_name']
            keys.append("profile_name")
            vals.append(f"'{fb_profile_name}'")
            runCmd = True
        if 'fb_follower_count' in data and len(data['fb_follower_count']) > 0:
            fb_follower_count = data['fb_follower_count']
            keys.append("follower_count")
            vals.append(f"{fb_follower_count}")
            runCmd = True
        if 'fb_location' in data and len(data['fb_location']) > 0:
            fb_location = data['fb_location']
            keys.append("location")
            vals.append(f"'{fb_location}'")
            runCmd = True
        if 'fb_joined_date' in data and len(data['fb_joined_date']) > 0:
            fb_joined_date = data['fb_joined_date']
            keys.append('joined_date')
            vals.append(f"'{fb_joined_date}'")
            runCmd = True
        keys = ','.join(keys)
        vals = ','.join(vals)
        print(f"keys={keys}, vals={vals}")
        cmd = f"INSERT INTO vpnosint_business_to_facebook_db ({keys}) VALUES ({vals})"
        if runCmd: 
            cur.execute(cmd)
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'ok' : True, "statusText" : "Company Successfully Added."}) 

@app.route('/api/update_domain_network/<int:company_id>', methods=['PUT','POST'])
def update_domain_network(company_id):
    """ Update domain/network information 

    vpnosint_db=# d vpnosint_domain_db;
                                                   Table "public.vpnosint_domain_db"
             Column          |            Type             | Collation | Nullable |                    Default                     
    -------------------------+-----------------------------+-----------+----------+------------------------------------------------
     id                      | integer                     |           | not null | nextval('vpnosint_domain_db_id_seq'::regclass)
     domain_name             | character varying(255)      |           | not null | 
     address                 | text                        |           |          | 
     latitude                | double precision            |           |          | 
     longitude               | double precision            |           |          | 
     business_id             | integer                     |           |          | 
     registration_date       | timestamp without time zone |           |          | 
     registrar               | character varying(256)      |           |          | 
     registrar_abuse_email   | character varying(255)      |           |          | 
     registrar_phone         | character varying(255)      |           |          | 
     registrant_name         | character varying(255)      |           |          | 
     registrant_organization | character varying(255)      |           |          | 
    Indexes:
        "vpnosint_domain_db_pkey" PRIMARY KEY, btree (id)
    Foreign-key constraints:
        "fk_business" FOREIGN KEY (business_id) REFERENCES vpnosint_business_db(id) ON DELETE CASCADE
    """

    data = request.json
    company_id = data['company_id']
    print(f"api/update_social_media/, company_id={company_id}, type(company_id)={type(company_id)}")
    if company_id == -1 or company_id == '-1':
        return jsonify({'ok' : False, 'statusText' : 'Cannot update social media provil for unknown VPN provider.'})
    else:
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            domain_check_query = """
                SELECT EXISTS (
                    SELECT 1 FROM  vpnosint_domain_db WHERE business_id = %s
                );
            """
            # Execute the query
            cur.execute(domain_check_query, (company_id,))
            domain_exists = cur.fetchone()[0]  # Fetch the result (True or False)

            keys = []
            vals = []
            if not domain_exists:
                print(f"Entry with ID {company_id} doesn't exists.")
                return _create_domain_network(data)
            else:
                """ There is an existing entry, so we just need to update stuff."""
                runCmd = False
                update_cmd = []
                if 'domain_name' in data and len(data['domain_name']) > 0:
                    domain_name = data['domain_name']
                    tmp = f"domain_name='{domain_name}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_address' in data and len(data['domain_address']) > 0:
                    domain_address = data['domain_address']
                    tmp = f"address='{domain_address}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_latitude' in data and len(data['domain_latitude']) > 0:
                    domain_latitude = data['domain_latitude']
                    tmp = f"latitude='{domain_latitude}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_longitude' in data and len(data['domain_longitude']) > 0:
                    domain_longitude = data['domain_longitude']
                    tmp = f"longitude='{domain_longitude}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_registration_date' in data and len(data['domain_registration_date']) > 0:
                    registration_date = data['domain_registration_date']
                    tmp = f"registration_date='{registration_date}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_registrar' in data and len(data['domain_registrar']) > 0:
                    domain_registrar = data['domain_registrar']
                    tmp = f"registrar='{domain_registrar}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_registrar_abuse_email' in data and len(data['domain_registrar_abuse_email']) > 0:
                    domain_registrar_abuse_email = data['domain_registrar_abuse_email']
                    tmp = f"registrar_abuse_email='{domain_registrar_abuse_email}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_registrar_phone' in data and len(data['domain_registrar_phone']) > 0:
                    domain_registrar_phone = data['domain_registrar_phone']
                    tmp = f"registrar_phone='{domain_registrar_phone}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_registrant_name' in data and len(data['domain_registrant_name']) > 0:
                    domain_registrant_name = data['domain_registrant_name']
                    tmp = f"registrant_name='{domain_registrant_name}'"
                    update_cmd.append(tmp)
                    runCmd = True
                if 'domain_registrant_organization' in data and len(data['domain_registrant_organization']) > 0:
                    domain_registrant_organization = data['domain_registrant_organization']
                    tmp = f"registrant_organization='{domain_registrant_organization}'"
                    update_cmd.append(tmp)
                    runCmd = True
                
                if runCmd: 
                    tmp = f"business_id='{company_id}'"
                    update_cmd.append(tmp)

                update_cmd = ','.join(update_cmd)
                cmd = f"UPDATE vpnosint_domain_db SET {update_cmd} WHERE business_id={company_id};"
                print(f"cmd={cmd}")

                if runCmd: 
                    cur.execute(cmd)
                    conn.commit()

            # TODO: Implement saving IP addresses and stuff. That might be better done in the reverse engineering section though.    
        except Exception as e:
            print(f"Error checking entry: {e}")
        finally:
            # Close the cursor and connection
            cur.close()
            conn.close()

        return jsonify({'ok' : True, "statusText" : "Company Successfully Added."}) 

@app.route('/api/delete_domain_network/<int:company_id>', methods=['PUT','POST'])
def delete_domain_network(company_id):
    """ TODO: Implement"""
    raise Exception("Unimplemented method.")


# END - CRUD for Network/Domain Information


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

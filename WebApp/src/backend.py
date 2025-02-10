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
    return jsonify({"ok" : True, "statusText" : "Unimplemented API"})

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

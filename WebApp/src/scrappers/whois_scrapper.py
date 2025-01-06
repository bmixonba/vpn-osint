import whois
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# PostgreSQL connection settings
DB_HOST = 'localhost'
DB_NAME = 'whois_db'
DB_USER = 'whois_user'
DB_PASSWORD = 'whois_password'

def connect_to_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def store_whois_info(domain_name):
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        w = whois.whois(domain_name)
        cursor.execute("""
            INSERT INTO whois_info (domain_name, registrar, creation_date, expiration_date, name_servers)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            domain_name,
            w.registrar,
            w.creation_date,
            w.expiration_date,
            ', '.join(w.name_servers)
        ))
        conn.commit()
    except Exception as e:
        print(f"Error storing whois info for {domain_name}: {e}")
    finally:
        cursor.close()
        conn.close()

@app.route('/whois', methods=['POST'])
def api_whois():
    domain_name = request.get_json()['domain_name']
    store_whois_info(domain_name)
    return jsonify({'message': f"Whois info for {domain_name} stored successfully"})

if __name__ == '__main__':
    app.run(debug=True)


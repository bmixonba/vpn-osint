import psycopg2

def main():
    conn = psycopg2.connect(
        dbname="vpnosint_db",
        user="vpnosint_user",
        password="password",
        host="localhost"
    )
    print(f"conn={conn}")

if __name__ == '__main__':
    main()


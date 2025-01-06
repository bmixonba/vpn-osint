import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from nmap import PortScanner
import psycopg2

app = FastAPI()

# PostgreSQL database connection settings
DB_HOST = 'your_db_host'
DB_NAME = 'your_db_name'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'

# Nmap scanner settings
NMAP_SCAN_TIMEOUT = 10

# Create a PostgreSQL connection pool
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()

@app.post("/nmap_scan")
async def nmap_scan(request: Request, domain_or_ip: str):
    """
    Run Nmap scan against the input domain name or IP address and store results in PostgreSQL.
    """
    # Initialize Nmap scanner
    nm = PortScanner()

    try:
        # Run Nmap scan
        scan_results = nm.scan(domain_or_ip, arguments="-sV -p 1-65535")

        # Extract relevant data from Nmap scan results
        data = {
            "domain_or_ip": domain_or_ip,
            "scan_results": {}
        }
        for host in scan_results:
            for proto in scan_results[host]:
                for port in scan_results[host][proto]:
                    data["scan_results"][f"{host}:{port}"] = {
                        "state": scan_results[host][proto][port]["state"],
                        "product": scan_results[host][proto][port]["product"],
                        "version": scan_results[host][proto][port]["version"]
                    }

        # Store data in PostgreSQL
        cur.execute("""
            INSERT INTO nmap_scans (domain_or_ip, scan_results)
            VALUES (%s, %s)
        """, (domain_or_ip, json.dumps(data["scan_results"])))
        conn.commit()

        return JSONResponse(content=data, media_type="application/json")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

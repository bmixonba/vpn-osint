import sys
import json
import requests

import pandas as pd

def read_apk_from_sha256(apikey, sha256):
    params = {
        'apikey': apikey,
        'sha256': sha256
    }
    url = 'https://androzoo.uni.lu/api/download'
    response = requests.get(url, params=params)

# Save the downloaded file with the name specified in the Content-Disposition header
if 'Content-Disposition' in response.headers:
    filename = response.headers['Content-Disposition'].split('filename=')[-1].strip('"')
    with open(filename, 'wb') as f:
        f.write(response.content)
else:
    print('Error: No filename found in response headers')

def do_analysis(config):
    print(f"config={config}")
    infile = config["vpn"]["infile"]
    apikey = config["apikey"]
    print(f"infile={infile}")
    apks = pd.read_csv(infile)
    print(f"apks={apks}")
    print(f"apks.keys()={apks.keys()}")
    for l in apks:
        print(f"l={l}")
        exit(0)

def main():
    """

    1. download an apk
    2. unzip the apk
    3. hash all the files (???)
    4. do static analysis on the app
    4.1. search for embedded certificates 
         (ie., run file command on all files, esp. in assets)
    4.2. build table - app name, file name, file type
         (according to file cmd), sha256 hash, 
    4.3. output of strings command or something...
    5. do dynamic analysis on the app
    5.0. It looks like malware (some anyway) wait some time
         before downloading encrypted stuff that is malicious.
    5.1. 
    5.2. 

    """
    config = sys.argv[1]
    with open(config) as f:
        config = json.load(f)
    do_analysis(config)

if __name__ == '__main__':
    main()

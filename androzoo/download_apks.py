import sys
import json
import requests

import pandas as pd
import os
from os.path import join

SHA256_IDX = 0
APK_NAME_IDX = 5

def read_apk_from_sha256(apikey, apkname, sha256):
    params = {
        'apikey': apikey,
        'sha256': sha256
    }
    url = 'https://androzoo.uni.lu/api/download'
    outprefix = "APKs/VPNs/"
    outfile = join(outprefix, apkname)
    if not os.path.exists(outfile):
        response = requests.get(url, params=params)
        # Save the downloaded file with the name specified in the Content-Disposition header
        if 'Content-Disposition' in response.headers:
            filename = response.headers['Content-Disposition'].split('filename=')[-1].strip('"')
            print(f"filename={filename}")
            print(f"outfile={outfile}")
            with open(outfile, 'wb') as f:
                f.write(response.content)
        else:
            print('Error: No filename found in response headers')
    else:
        print(f'File {outfile} already exists')

def do_analysis(config):
    print(f"config={config}")
    infile = config["vpn"]["infile"]
    apikey = config["apikey"]
    print(f"infile={infile}")
    apks = pd.read_csv(infile)
    print(f"apks={apks}")
    print(f"apks.keys()={apks.keys()}")
    """
    l=['000145E573C0C87D5C2A2E4C1904755D93AC215DAE6BDCAA4C1236D82B6AE621'
         '3AD12813C4AAF90F85D7F4CA76E73BEFC4D5AC09'
         '1D8464C2B6F9E7415E349C4732236571' '1980-01-01 00:00:00' 14270799
         'com.atlasvpn.free.android.proxy.secure' 73 0.0 '2021-06-30 08:38:05'
         9419632 'play.google.com']
    """
    for l in apks.values:
        sha256 = l[SHA256_IDX]
        apkname = l[APK_NAME_IDX]
        print(f"apkname={apkname}, sha256={sha256}")
        read_apk_from_sha256(apikey, apkname, sha256)
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

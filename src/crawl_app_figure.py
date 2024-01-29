import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_vpn_names(url):
    vals = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    appRoot = soup.find('div', id='app-root')
    appRootSpan = appRoot.find_next('span')
    appRootSpanDiv = appRootSpan.find_all_next('div')
    for a in appRootSpanDiv:
        try:
            tmp = a.find('a')
            title = tmp.attrs['title']
            if 'vpn' in title or 'Vpn' in title or 'VPN' in title or 'Proxy' in title:
                vals.append(title)
        except:
            pass

    return list(set(vals))


def get_app_names(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        app_names = []

        print(f"soup={soup}")

        for app_title in soup.find_all('h2', class_='app-title'):
            app_name = app_title.text.strip().lower()

            if 'vpn' in app_name or 'proxy' in app_name:
                app_names.append(app_name)

        return app_names
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    countries = ['taiwan', 'hong-kong', 'nepal', 'pakistan', 'russia', 'vietnam', 'saudi-arabia', 'egypt', 'turkey', 'kazakhstan']
    vpns = pd.DataFrame()
    for c in countries:
        url = 'https://appfigures.com/top-apps/google-play/{}/tools'.format(c)
        foo = get_vpn_names(url)
        print(foo)
        tmp = pd.DataFrame(foo)
        tmp['country'] = c
        vpns = pd.concat([vpns, tmp])
    vpns.to_csv('vpnNames.csv')

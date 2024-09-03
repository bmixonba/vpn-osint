import ssl
import sys


def get_cert(url):
    return ssl.get_server_certificate((url, 443))

def test_get_cert():
    cert = get_cert("www.fastsvpn.com")
    print(f"{cert}")

def main():
    if len(sys.argv) <= 1:
        print(f"{sys.argv[0]} urls.csv")
        print("urls.csv is a text file containing a list of urls without https:// and no leading or trailing slashes.")
        test_get_cert()
        exit()
    urls = []
    print("STARTING")
    with open(sys.argv[1]) as f:
        urls = [l[:-1] for l in f.readlines()]
    for url in urls:
        cert = get_cert(url)
        with open(f"{url}.cert.txt", "w") as f:
            f.write(cert)


if __name__ == '__main__':
    main()

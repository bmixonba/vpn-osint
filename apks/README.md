# !!!WARNING!!!

This repo may contain malicious executables. Threats are unconfirmed, unencrypted, and so one. Clone and 
use at your own risk.

# Analysis

## Color VPN

### Static Analysis

Using the strings to identify potential indicators
```bash
strings libredsocks.so

/Users/WilliamChik/Documents/develop/bypass-ss-android/core/src/main/jni/redsocks/log.c
```


#### Developers

Based on the strings from static analysis, it appears this app was developed on a user
named `WilliamChik`. This is further coroborated when searching github for the string
`User/WilliamChik/Documents/develop/` because the same directory structure is found in
multiple instances of this user's issues.


## XY VPN (Mate VPN)

This VPN is developed by a company called Matrix Mobile PTE LTD and has 100,000,000 downloads according to Google Play.
The privacy policy references `Innovative` (ie, `Innovative Connecting`), which has multiple other VPNs and VPN providers.
This VPN seems to be located in Singapore, and searching the address reveals a link to FireEye (https://partners.fireeye.com/directory/partner/1542355/jtech-pte-ltd)
### Developers

1. Kr328, https://github.com/Kr328
2. Liniweeii
3. xiewenyu (or possibly https://github.com/Yewenyu) : https://github.com/shadowsocks/shadowsocks-rust/issues/797

https://shadowvpn.org/

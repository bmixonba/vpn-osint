# A second look at LetsVPN Apps from Third-party and non-App store locations

## Key Findings

* Investigated 8 LetsVPN clones

* Two of the APKs are msi files, two are "exe" files, and the remaining are APKs files

* One is for the legitimate App, X use obfuscation (shared/imported libraries still contain social network of Code)


## Motivation 

LetsVPN is an app focused primarily on Chinese users. [Crybl](https://cyble.com/blog/new-malware-campaign-targets-letsvpn-users/) 
documented attacks targeting LetsVPN to install malware on the user's device. The legitimate LetsVPN App is developed by LetsGo Networks 
and is focused on Chinese users. According to [AppleCensorship](https://applecensorship.com/app-store-monitor/test/letsvpn) LetsVPN is
also removed from the Chinese App store. 

![Apple Censorship](applecensorship-letsvpn.png)

This makes it an appealing target for impersonation.



## Methodology 

### Domain Discovery 
Using [dnstwist](https://github.com/elceef/dnstwist) and
[urlcrazy](https://github.com/urbanadventurer/urlcrazy) I identified seven domain impersonating `letsvpn.com`.


## Results

### Legit1

This is the legitimate version of the APK.

#### Misc. Info

urls,letsvpn.world domain info, the source for LetsVPN

### Candidate1

This is another legitimate version of the app. The URL redirects  to `letsvpn.world`.
#### Misc. Info
url, letssvpn.com domain info, redirects to letsvpn.world

### Candidate2

Requesting the URL `letsssvpn.com` yields the following impersonated website:

![Fake Website](./Candidate2/letsssvpn.com.definitely-fake.png)

This is a suspicious version of LetsVPN. The download claims to be an APK, but unzipping the files
a Microsoft `MSI` file.

#### Misc. Info
url,letsssvpn.com domain info,

### Candidate3

Requesting the URL `lettsvpn.com` yields the following website:

![Fake Website](./Candidate3/lettsvpn.com.fake.png)

This is another suspicious version of LetsVPN. The download claims to be an APK, but unzipping the files
a Microsoft `MSI` file. This is a different MSI file from `Candidate2`.

### Candidate4

Requesting the URL `letesvpn.com` yields the following page:

![Fake Website](./Candidate4/letesvpn.com-fake.png)

This is another suspicious version of LetsVPN. The download claims to be an APK, but unzipping the files
a Microsoft `MSI` file. This is a different MSI file from `Candidate2`.

### Candidate5

[//]: # vpn type, v2ray, password, 123456, fine location, true

The following candidate is related to the [following report](https://research.checkpoint.com/2023/pandas-with-a-soul-chinese-espionage-attacks-against-southeast-asian-government-entities/)

### Candidate6

Searching for the URL `letsvpn.me` yields a valid website:


![Fake Website](./Candidate6/letsvpn.me.fake.png)

The actual APK name is `com.li.fast`. This decompliled APK is obfuscated as seen in the following image:

![Obfuscated APK](./Candidate6/candidate6-obfuscated.png)

It appears to request minimal permissions, none of which seem too invasive. 

![Permissions](./Candidate6/candidate6-permissions.png)

The code reference multiple URLs related to API calls, one `https://gitee.com/tima123/tg0`.

### Candidate7


### Candidate8

### Candidate9


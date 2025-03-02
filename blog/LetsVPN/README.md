# A second look at LetsVPN Apps from Third-party and non-App store locations

## Key Findings

* LetsVPN has been targeted by censored and impersonated by multiple attackers

* Investigated 14 LetsVPN clones

* Two of the APKs are msi files, two are "exe" files, and the remaining are APKs files

* One APK, Candidate6, uses obfuscation (shared/imported libraries still contain social network of Code)

## Motivation 

LetsVPN is VPN a VPN app is developed by LetsGo Networks and is focused on Chinese users. According to [AppleCensorship](https://applecensorship.com/app-store-monitor/test/letsvpn) LetsVPN is also removed from the Chinese App store. Furthermore, [Crybl](https://cyble.com/blog/new-malware-campaign-targets-letsvpn-users/) documented attacks targeting LetsVPN to install malware on the user's device. While these two events are not connected per se, censorship undoubtable creates a gap in the supply chain that attacker can exploit. To better understand the modern threat of censorship on the VPN ecosystem, this post covers a case study focused on understanding the threat that imposter VPNs pose to Netizens.

![Apple Censorship](./imgs/applecensorship-letsvpn.png)

This makes it an appealing target for impersonation.

## Methodology 

### Domain Discovery 
Using [dnstwist](https://github.com/elceef/dnstwist) and
[urlcrazy](https://github.com/urbanadventurer/urlcrazy) I identified seven domain impersonating `letsvpn.com`.

## Results

### Transparency

#### Domain

#### Website

The website uses Matomo for url tracking. Javascript embedded within the homepage uses the
following endpoint for user tracking and analytrics: https://web.dcobxs.com/matomo.php

This page is clearly designed to impersonate letsvpn.world. The evidence for this is the color scheme,
logos, and graphics similarity.

### Legit1

This is the legitimate version of the APK.

#### Misc. Info

urls,letsvpn.world domain info, the source for LetsVPN

##### Candidate 1

Location, H

#### 


### Candidate1

This is another legitimate version of the app. The URL redirects  to `letsvpn.world`.

#### Misc. Info
url, letssvpn.com domain info, redirects to letsvpn.world

### Candidate2

Requesting the URL `letsssvpn.com` yields the following impersonated website:

![Fake Website](./imgs/letsssvpn.com.definitely-fake.png)

This is a suspicious version of LetsVPN. The download claims to be an APK, but unzipping the files
a Microsoft `MSI` file.

#### Misc. Info
url,letsssvpn.com domain info,

### Candidate3

Requesting the URL `lettsvpn.com` yields the following website:

![Fake Website](./imgs/lettsvpn.com.fake.png)

This is another suspicious version of LetsVPN. The download claims to be an APK, but unzipping the files
a Microsoft `MSI` file. This is a different MSI file from `Candidate2`.

### Candidate4

Requesting the URL `letesvpn.com` yields the following page:

![Fake Website](./imgs/letesvpn.com-fake.png)

This is another suspicious version of LetsVPN. The download claims to be an APK, but unzipping the files
a Microsoft `MSI` file. This is a different MSI file from `Candidate2`.

### Candidate5

[//]: # vpn type, v2ray, password, 123456, fine location, true

The following candidate is related to the [following report](https://research.checkpoint.com/2023/pandas-with-a-soul-chinese-espionage-attacks-against-southeast-asian-government-entities/)

### Candidate6

Searching for the URL `letsvpn.me` yields a valid website:


![Fake Website](./imgs/letsvpn.me.fake.png)

The actual APK name is `com.li.fast`. This decompliled APK is obfuscated as seen in the following image:

![Obfuscated APK](./imgs/candidate6-obfuscated.png)

It appears to request minimal permissions, none of which seem too invasive. 

![Permissions](./imgs/candidate6-permissions.png)

The code reference multiple URLs related to API calls, one `https://gitee.com/tima123/tg0`.

### Candidate7

Searching Baidu for LetsVPN yields the following search results:

![Baidu Recommendation](./imgs/lettsvpn.com-baidu-recommendations.png)

The file downloaded is `pg457.apk`.

After decompiling the code in jadx, the real package name is `com.pangu.c96b73589`

There are some interesting Permissions, such as requesting to download packages and record audio.

![Candidate7 Permissions](./imgs/candidate7-permissions.png)


### Candidate8

Baidu also recommended the following site for LetsVPN, `kuailiavfpns.com`.

![Kuailiavfpns](./imgs/kuailiavfpns.com.png)

The download produces the zip file, `kuaiVPN.zip`. Unzipping the file yields `kuaiVPN.exe`, which is suspicious because
the download should be for an Android APK. It has sha256 `ee5f3eca5753a7b5f8411c3495662807909618739231a0dad2be365c084ea0a9`.
VirusTotal had 24 of 73 sensors return positive results.

![Candidate8 VirusTotal](./imgs/candidate8-virustotal.png)

### Candidate9

The following candidate yields another ZIP file containing a Microsoft MSI file, `KuaiVpn-n.msi`.

### Candidate10

### Candidate11

There is clearly something different about this VPN app versus the others. First, it's an MSI file, not a ZIP file. Second,
it may be a previously unknown malware given that the hash does not show up in VirusTotal.

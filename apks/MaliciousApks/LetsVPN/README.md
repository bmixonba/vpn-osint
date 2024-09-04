# A second look at LetsVPN Apps from Third-party and non-App store locations

## Key Findings

* Investigated 15 LetsVPN clones

* Four of the APKs are msi files, two are "exe" files, and the remaining are
  APKs files.

* One APK, Candidate6, uses obfuscation (shared/imported libraries still
  contain social network of Code)

## Motivation 

This case-study has two goals: explores the impact that censorship has on
circumvention tools, such as VPNs, and, understand the operational
characteristics of adversaries posing as legitimate VPNs. VPN apps are already
an attractive target for attackers because they give the attacker access to
client network data in a raw form. When the censorship leads to censors
blocking VPN apps, the void is inevitably filled with opportunistic
adversaries. For example,  LetsVPN, an app focused primarily on Chinese users,
is unavailable to Chinese users through the Apple app store, according to
[AppleCensorship](https://applecensorship.com/app-store-monitor/test/letsvpn).  

![Apple Censorship](applecensorship-letsvpn.png)

LetsVPN has also been targeted by multiple impersonation attacks according
[Cyble](https://cyble.com/blog/new-malware-campaign-targets-letsvpn-users/) and
[TrendMicro](https://www.trendmicro.com/en_us/research/24/f/behind-the-great-wall-void-arachne-targets-chinese-speaking-user.html).
Neither group directly linked the attacks to censorship, but the coocurrence of
is interesting. The attackers used SEO poisoning and spearphishing on social
media and other channels to trick the user into downloading the backdoored
file. In the documented cases, they backdoored MSI files that contain a dropper
and posess other cababilities. 


# Malware Overview

## Initial Access

SEO poisoning (T1608.006), Spearphishing

### Distribution


## Code Analysis

## Methodology 

### App Discovery 

The first challenge in analyzing impersonated apps is identifying real
instances.  Attackers use many techniques, such as typo-squatting,
spearphishing, and SEO poisoning, but regardless, the users typically clicks on
a link to a imposter website or to the executable download.  Attackers often
use camoflauge to make their domain names look similar to the target
application's by using similar spellings. We identified 15 distinct, active
domain names that distirbute versions of LetsVPN for multiple platforms.  For
automatic discovery, we used [dnstwist](https://github.com/elceef/dnstwist) and
[urlcrazy](https://github.com/urbanadventurer/urlcrazy) and uncovered seven
domain impersonating `letsvpn.com`. For manual discovered, we created domain
variations that were unsupported by either tool. We also searched for the name
``LetsVPN'' using major search engines (Baudi, Yandex, Google, Leo, and
DuckDuckGo) and meta-search engines () and discovered X domains. We uncovered
15 distinct domains actively impersonating LetsVPNs website and distributing
apps.

### Imposter Confirmation 

Attribution is a difficult for a number of reasons. First, unless legaly
compelled, the hosting provider is unlikely to provide information about the
identity of specific website owners. The domain name is often registrered using
an service that redacts identifying information in whois records, and the name
authority assigning the domain name is also unlikely to provide the identify of
the domain owner. This information is still important to know because it can
provide insight about the threat groups operational practices, such as who
hosts their website, where the domain is registered to.  This information can
then be cross referenced and compared with other actors to measure
similiarities and differences.

After identifying active domains, we collect the raw html of the homepage and
whois information. From the website, we collect the privacy policy and terms of
serivce if there is one. From the website, we collect email addresses, physical
addresses, and phone numbers. From whois records, we collect the registrar,
registrant, admin, and tech names, emails, phone numbers, and addresses.  We
collect this information from the legitimate website, which acts as our
control, and the subject website. If there is a high degree of similarity in
the website and whois information, then we conclude the subject website is
likely also owned and operated by the LetsVPN, otherwise, if the website is
similar and the whois information is different, we conclude that the subject
VPN is impersonating the website. We perform additional manual verification by
comparing the favicon and branding content from the legitimate and subject
websites.

### Digital Footprint Analysis

In addition to the information collected for measuring deciet, we also collect
hrefs and other resources from the website. These resources sometimes link to
other hosting platforms where the attacker may host additional information in
support of the current campaign. 

### Code Analysis 

After separating the applications into legitimate or candidate imposter
applications, we perform static and dynamic analysis to extract additional
information that might lead to identifying the actors behind the given
application.

#### Static Analysis

Identifiers left in code can sometimes provide additional clues and information
for comparison. First we exctract ascii strings from application. In the case
of MSI files, we simply run the "strings" command on the file. For APKs, we
first uncompress the APK and then search for strings in the dex files and
lib/*. We also search through the res and assets directories.

## Results


### Legit1

This is the legitimate version of the APK.

#### Misc. Info

urls,letsvpn.world domain info, the source for LetsVPN

### Candidate1

This is another legitimate version of the app. The URL redirects  to
`letsvpn.world`.  #### Misc. Info url, letssvpn.com domain info, redirects to
letsvpn.world

### Candidate2

Requesting the URL `letsssvpn.com` yields the following impersonated website:

![Fake Website](./Candidate2/letsssvpn.com.definitely-fake.png)

This is a suspicious version of LetsVPN. The download claims to be an APK, but
unzipping the files a Microsoft `MSI` file.

#### Possible Threat actor

void archane:
https://thehackernews.com/2024/06/void-arachne-uses-deepfakes-and-ai-to.html

#### Misc. Info

url,letsssvpn.com domain info,

### Candidate3

Requesting the URL `lettsvpn.com` yields the following website:

![Fake Website](./Candidate3/lettsvpn.com.fake.png)

This is another suspicious version of LetsVPN. The download claims to be an APK,
but unzipping the files a Microsoft `MSI` file. This is a different MSI file
from `Candidate2`.

### Candidate4

Requesting the URL `letesvpn.com` yields the following page:

![Fake Website](./Candidate4/letesvpn.com-fake.png)

This is another suspicious version of LetsVPN. The download claims to be an APK,
but unzipping the files a Microsoft `MSI` file. This is a different MSI file
from `Candidate2`.

### Candidate5

[//]: # vpn type, v2ray, password, 123456, fine location, true

The following candidate is related to the [following
report](https://research.checkpoint.com/2023/pandas-with-a-soul-chinese-espionage-attacks-against-southeast-asian-government-entities/)


#### Target Platform

##### Windows

This website provides targets multiple platforms (Android, Windows, and Apple).
The Windows EXE files trigger VirusTotal. 

##### Android

The APK uses v2ray for proxy connections. The v2ray configuration files allow
both outbound and inbound proxy connections. Outbound connections are expected
behavior for VPNss and proxy programs. The configuration file uses the password
`123456` and because the key is hard coded, an attacker could reverse engineer
this binary and eavesdrop on proxied connections. It is anomolous that a proxy
application with this design is configured to permit inbound proxy connections.
This could indicate that an attacker could conscript infected devices into a
network of some kind, either to proxy other peoples traffic, or some other
reason.

I have asked the v2ray community on thissues for additional information and am
awaiting a response.


Finally, the APK is configured to route specific domains and App traffic through
the proxies. 

##### Apple

The DMG is also 




### Candidate6

Searching for the URL `letsvpn.me` yields a valid website:


![Fake Website](./Candidate6/letsvpn.me.fake.png)

The actual APK name is `com.li.fast`. This decompliled APK is obfuscated as seen
in the following image:

![Obfuscated APK](./Candidate6/candidate6-obfuscated.png)

It appears to request minimal permissions, none of which seem too invasive. 

![Permissions](./Candidate6/candidate6-permissions.png)

The code reference multiple URLs related to API calls, one
`https://gitee.com/tima123/tg0`.

### Candidate7

Searching Baidu for LetsVPN yields the following search results:

![Baidu Recommendation](./Candidate7/lettsvpn.com-baidu-recommendations.png)

The file downloaded is `pg457.apk`.

After decompiling the code in jadx, the real package name is
`com.pangu.c96b73589`

There are some interesting Permissions, such as requesting to download packages
and record audio.

![Candidate7 Permissions](./Candidate7/candidate7-permissions.png)


### Candidate8

Baidu also recommended the following site for LetsVPN, `kuailiavfpns.com`.

![Kuailiavfpns](./Candidate8/kuailiavfpns.com.png)

The download produces the zip file, `kuaiVPN.zip`. Unzipping the file yields
`kuaiVPN.exe`, which is suspicious because the download should be for an Android
APK. It has sha256
`ee5f3eca5753a7b5f8411c3495662807909618739231a0dad2be365c084ea0a9`.  VirusTotal
had 24 of 73 sensors return positive results.

![Candidate8 VirusTotal](./Candidate8/candidate8-virustotal.png)

### Candidate9

The following candidate yields another ZIP file containing a Microsoft MSI file,
`KuaiVpn-n.msi`.

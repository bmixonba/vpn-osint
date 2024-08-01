# Introduction 

In this article I will be discussing how I conducted open source intelligence (OSINT) gathering
for multiple VPN products. This project was motiviated by the need to identify potentially risky VPN
apps in the wild. VPNs are increasingly popular with many different communities, from people in countries
with high Internet Freedom indeces, to at-risk communities in countries with repressive governments. These
repressive governments often block VPNs from being downloaded. This creates strong incentive for attackers
to target VPN applications.

VPN apps are consitently being created and advertized online and in App stores and there
are too many for any one person to audit. To address this, we need a way of assessing 
how trustworthy a particular VPN appears to be. Proxy for trustyworthy behavior is transparnecy
which we can infer based on various indicators in the data. This is challenging though because 
there are good reasons for a VPN provider to protect their own identity -- a provider's transparnecy
is inversely related to their own anonymity. Potential users can better judge for themselves whether they
are comfortable with using a particular provider based on these transparnecy indicators.

The first step in this analysis is building a list of VPNs to investigate. VPNs can be identified in several ways.
First, they can be crawled directly from a reputable app market like Google play. Second, they can be identified
based on privacy preserving data collection methods from a live network. Third, they can be identified based on 
which VPNs attackers are actively targetting, either for censorship or for malware implantation. We used all 
three methods to generate a preliminary list of VPNs.

Once the preliminary list is generated, deeper analyses are performed to identify and measure/estimate transparency
indicators. This information is then used to reduce the list down to a manageable size for a more 
comprehensive analysis of the applications. 

# Methods

We now cover the methods used to enumerate VPNs applications, identify transparency indicators, and perform deeper analyses.
We first provide details about the methods we used to discover and enumerate VPN applications and build the initial list.
Next we discuss the methods we used to identify various transparency indicators. Finally, we discuss methods 
used to perform the more comprehensive analysis.

## VPN Discovery & Enumeration

We used three different methods to discover and enumerate VPNs. We refer to the first method as Deductive Discovery.
We refer to the second as inductive discovery. We refer to the third as adversarial discovery.

### Deductive Discovery 

Deductive Discovery is the process of identifying candidate VPN applications using indicators available
from a shallow analysis of indicators related to specific VPNs on app stores, such as inconsistency in their website,
location, and strings in their APK file.

### Inductive Discovery

Inductive discovery refers to data drive techniques, i.e., CryptoSluice, where live network data are analyzed
in a privacy preserving way and apps that are activelly being used generate the list of VPNs. 

### Adversarial Discovery 

Adversarialy Discovery refers to generate candidate VPNs based on VPNs an attacker is actively targetting. Using GreatFire's 
[AppleCensorship](https://applecensorship.com/app-store-monitor/test/letsvpn) platform and technical reports [Cyble](https://cyble.com/blog/new-malware-campaign-targets-letsvpn-users/), we identified that LetsVPN, a chinese focused VPN platform, has been targetted 
both by attackers for impersonation and the Chinese government for removal from the Apple App store.

# Results 

We present high-level results for mutliple VPNs that we determined should be considered for further analysis
due to the risks they present to users.

## Discovery 

### Deductive 
Using Deductive Discovery, we identified a cluster of 10 VPNs from three VPN providers on Google Play. The providers are
Autumn Breeze, Innovative Connecting, and Lemon Clove. A simple string search of their decompressed APK file results
in the ten APK names present in the shared library `libopvpnutil.so`.

### Inductive

Using Inductive Discovery, we identified a VPN accelerator, Kuaifan, that appears to have poor transport layer security.

### Adversarial

Using Adversarial Discovery, we identified that LetsVPN is being targeted by both state and non-state actors for impersonation, censorship, and malware implantation.


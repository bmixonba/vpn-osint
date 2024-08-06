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

# Background

## Threat Types

- Legitimate VPNs - TunnelBear
- Shady/Opaque VPNs - KuaiFan, TurbVPN et al
- Actively Targeted VPNs - LetsVPN


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

## Candidate Analysis

One a set of candidate VPNs has been identified,  

### Static Analysis

### Dyanamic Analysis

# Results 

We present high-level results for mutliple VPNs that we determined should be considered for further analysis
due to the risks they present to users.

## Discovery 

### Deductive 

Using Deductive Discovery, we identified a cluster of 10 VPNs from three VPN providers on Google Play. The providers are
Autumn Breeze, Innovative Connecting, and Lemon Clove. A simple string search of their decompressed APK file results
in the ten APK names present in the shared library `libopvpnutil.so`. More details about these VPNs can be found [here](https://github.com/bmixonba/vpn-osint/blob/main/blog/VPNMonster/README.md)

### Inductive

Using Inductive Discovery, we identified a VPN accelerator, Kuaifan, that appears to have poor transport layer security. More details
about the results for this app are available [here](https://github.com/bmixonba/vpn-osint/blob/main/blog/Kuaifan/Kuaifan.md).

### Adversarial

Using Adversarial Discovery, we identified that LetsVPN is being targeted by both state and non-state actors for impersonation, censorship, and malware implantation. More details about the specific Apps and analysis techniques is covered in the post [here](https://github.com/bmixonba/vpn-osint/blob/main/blog/LetsVPN/README.md).


# Challenges

I have identified four challenges:

1. Finding positive malware samples
2. Automating data collection
3. Communicating the subtlty of VPN provider transparnecy (trustworthines) versus anonymity 
4. Framing and Outreach for current finding 


The first two challanges are technical challenges that we might be able to address by innoviting new solutions.
First, finding confirmed malware and "untrustworthy" VPN applications is neccessary for automating
analysis to find suspicious VPNs because the currently proposed methodology depends on clustering algorithms.
Without confirmed instances to ground-truth, it is more time consuming to manual analyze the VPNs or find
other transparnecy indicators. Much of the malware described online is not easily downloaded. 
We currently address this by performing typo-squatting analysis to identify instances of attackers
actively targetting specific VPN applications. This methodology has the benefit that 
it can identify actively being targetted by adversaries. Second, automatically downloading the data 
is challenging because each page is potentially different. This makes the analysis more fragile since different parsers
are required for each page. It might make more sense to use an existing OSINT Framework, like
Open Cyber Threat Intellegence framework [OpenCTI](https://filigran.io/), and manually entering the data and/or ingesting it automatically whenever possible.

The next two challenges are communications oriented. The first is based on the observation that the current notion
of transparency is based on indicators, such as DNS registrar or code obfuscation that a provider might employe. The provider might
be jutsified in using such techniques. For example, if a VPN provider is based out of a country with a repressive government, 
they will undoubtly need anonymity to protect themselves from targeted attacks. Unforunately, the obfuscation used for provider
anonymity also indicates potential deception/untrustworthiness to a VPN client.

The second communications challenges is in how to frame the current findings. One way to think about identified threats and/or
shady providers is that they are active campaigns targeting users. I am trying to understand the degree to which this overlaps
with projects such as Mobile Surveillance Monitor. My current understanding of that project is that they use different techniques
to measure surveillance and are not focused on VPNs specifically, so this work is complementary. I think the best 
thing to do is to propose my current framing to the community, get their input, reflect, incorporate, and iterate based
on that feedback.




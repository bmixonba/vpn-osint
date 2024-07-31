# Introduction 

VPNs are frequent targets of blocking and remove from app stores because their ability to open closed networks. 
This is one of many reasons that make VPNs high-risk application for users to download. Blocking orders 
from repressive governments add to market pressure that fuels attackers to impersonate legitimate VPN 
services. Unforuntaely, VPN have increased in number and they continue to proliferate and not
every VPN is neccessarily malicious, even if insecure. Identifying candidate VPNs is an important
step in identifying active threats online.

Researchers have identified threats to a number of ways. Mobile Surveillance Monitor uses data from Mobile operators to
identify instances of targetted surveillance using insecurities in mobile network operator protocols like SS7-3G and Diameter-4G.
Citizen Lab has extensively document mercenary spyware targetting civil society for many years and identified 
many actors in the space. Their samples are often submitted by journalists, dissidents, and other at risk peoples.
GreatFire/AppleCensorship identifies applications blocked by Apple app store in China. The VPN-alyzer 
project identify security weaknesses (such as information leaks) in popular VPN software. This
work complements these lines of research by identifying threats faced by VPN clients.

One goal in threat identification is identifying who controls a particular app but VPN apps are in constant 
flux, with VPNs being added to and removed from App stores and the Internet for a myriad of reasons. What is
needed techniques for generating a list of candidate VPNs researchers should consider prior to further analysis.
This processes is accomplished in two phases, the trigger phase and the analysis phase. The trigger phase
is concerned with initial discovery. There are multiple ways to identify preliminary candidates.

* Deducive techniques, such as OSINT intelligence gathering
* Inductive techniques, CryptoSluice
* Actively, using typo-squating enumeration
* Social network analysis (X, telegram) 

After the inital app list is generated, the initial volume needs to be reduced to apps most likely 
to put users at risk. One way to do this is using indicators about the VPN provider/developer's
operational practices (e.g., are they operating transparently?). Another is to identify the VPNs 
that are being actively targeted. To understand transparency, multiple properties of the VPN must
be investigated, such as whether it obfuscates its code, how it sends, receives, uses and stores
data, with whom it communicates and whether they are trust-worthy, what software it's using and
second trust relationships, and more. To understand active targeting requires insights about indicators
such as active infastructure, distribution networks (such as typo-squatted domains), or whether they
are being actively censored in a given country.

After generating the candidate list, a deeper analysis can be performed to confirm or refute the threat.
Analysis might include cluster analysis (such as phylogentic clustering or stylometric information) to identify
threats in non-VPN, non-Censor apps, etc.  

After this phase of the analysis, identities and persona can be attributed to an app (using strings, etc) and 
then a final investigation using e.g., [opencorporates.com](opencorporates.com). Another concerte outcome of this work is
that we will have a sense for what is currently being potentially or confirmed actively targetted and who might
be controlling the App. This is interesting because to the best of my knowledge, I have not seen discussion of actively
targeted applications in the context of VPNs. Mobile Surveillance Monitor (MSM) Gary Miller's 
project is the closest project similar to our efforts. VPN-alyzer is another similar system for 
monitoring the security of VPNs, but we are different because we focus searching for and identifying
VPNs (and other apps).

The majority of VPN projects focus on VPN security and not on whether attackers are actively targeting specific 
applications. This work moves in this direction by using proactive methods for threat hunting (deductive, inductive, active).

The lessons learned here can and already been applied beyond VPNs to other applications [CryptoSluice]().
In the future, further refinements should be performed and should be applied to the censored apps from
[applecensorship.com](applecensorship.com) and other potential sources as well.

# Background




# Methods

## Discovery 

There are multiple methods for discovering preliminary candidate VPNs. We can crowdsource the information by letting people upload files. We can use inductive methods, such as CryptoSluice that identified Kuaifan. We can brute-force domain names that are similar to other VPN products, such as in the LetsVPN case. Finally, we can crawl App stores for popular VPN apps and search for indicators. 

### Open Question(s) & Opportunity for novelty

One place where we can collaborate and/or maybe perform novel tasks
is using community detection and/or social network algorithms to
identify distribution networks on social media (This is related to
social media analysis for forecasting civil war
[1](https://dl.acm.org/doi/pdf/10.1145/3462211)).


## Preliminary Candidate Processing

### Static Analysis

#### Social Networks

- Git repositories
- imports of different code libraries
- Social Media
- URLs/domains
- IPs

#### Code

- Public keys (transparency stuff)

### Dynamic Analysis

#### Code
- Symbolic Execution - Phish
- VPNalyzer 2.0 - Piyush, Roya

#### Network
- VPNalyzer
- Proxy identification - Diwen and Roya, Jerry, Methods using techniques documented by the GFW authors, CryptoSluice

# Misc. Notes

- Mobile Surveillance Monitor

Though it answers the main question, I wish I didn't have to do so much of my own digging to understand a given threat.
I had to manually search for very detailed info about DoNot malware, for example.

## Project Dependency Diagram

```bash
          v-open and crowd sourced 
          v-network<-cryptosluice/inductive
discovery<-phishing/typosquatting<-What we are doing
          ^-deductive<-OSINT analysis <- social media <- Dave Levin (Not really, he just looks at some user studies)
                                       |- Identifying promotions to VPN products online (social media, telegram, etc.,) Open Questions here
                                       \- what I've been doing
                                     

                         v-VPNalyzer 2.0 <- Roya
                  v-code<-symbolic execution <- Phish 
data proc<-dynamic<-Network<-signals from VPNS <- VPN-alyzer <- Diwen and/or Reethika and Roya
         |                  ^- proxy id <- Diwen and Roya
         |                  |            ^- Jerry
         |                  |            ^- Us, maybe? <- port shadow/conntrack stuff
         |                  |- ???
         |                  \- cryptosluice
         |       v-social network<-imports to other code <- *What we are doing*
         |                        ^-public keys<- *What we are doing*
         |                        ^-social media<-Dave Levin?
         |                        ^-URLs
         |                        ^-IPs
         | |       v-stylometry<-Rachel Greenstadt
         \static<-code<-phylogensis<-who, *What we are doing*???
                 |     ^-Permissions<- VirusTotal
                 |     ^-static analysis<-obfuscation<-inconsistent type information between object and 
                 |                       ^-Something went here.
                 |
                 \- DNS name

analysis <- Apple some ML to answer some meaningful research question?

synthesis<-
```

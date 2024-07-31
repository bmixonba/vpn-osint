# Introduction 


VPNs are frequent targets of blocking and remove from app stores because their ability to open closed networks. 
From a user security perspective, VPNs are a high-risk application that attackers
target because repressive governments continue requiring app stores 
to block them. Identifying candidate VPNs is an important step before further analysis 
tp confirm active threats in the wild. Multiple techniques 
exist to identify candidate VPN applications for further analysis

* Deducive techniques, such as OSINT intelligence gathering (Explored)
* Inductive techniques, CryptoSluice (Explored)
* Actively, using typo-squating enumeration (Explored)
* Social network analysis (X, telegram) (not yet Explored)

Mutliple researchers have explored identifying various threats to different communities using a
variety of techniques. For example Mobile Surveillance Monitor uses data from Mobile operators to
identify instances of targetted surveillance. Citizen Lab writes extensively about mercenary spyware.
GreatFire researches which applications are being blocked by Apple app store. And the VPN-alyzer 
project identify security weaknesses (such as information leaks) in popular VPN software. This
work aims to complement these lines of research by identifying threat to VPN clients using a 
variety of methods.


One goal is that we want to identify who controls a particular VPN based on OSINT information. To do
this, we must first select which VPNs warrent further analysis. One way to do this is
to understand the VPN provider/developer's operational practices and the degree to which
they operate transparently. Another is to understand what VPNs are under active targeting.
To understand transparency, multiple properties of the VPN must be investigated, such as
whether it obfuscates its code, how it sends, receives, uses and stores data, with whom it communicates
and whether they are trust-worthy, what software it's using and second trust relationships, and more. 
To under stand active targeting requires insights about indicators such as active infastructure,
distribution networks (such as typo-squatted domains), or are being actively censored in a
given country. These are important to consider when building 
a candidate list. 

After generating the candidate list, a deeper analysis can be performed to confirm and understand the threat.
Analysis might include cluster analysis (such as phylogentic clustering or stylometric information) to identify
threats in non-VPN, non-Censor apps, etc.  

After this phase of the analysis, identifies and persona can be attributed to a the app (using strings, etc) and 
then a final investigation using [opencorporates.com](opencorporates.com). Another concerte outcome of this work is
that we will have a sense for what is currently being potentially or confirmed actively targetted and who might
be controlling the App.

This is useful because to the best of my knowledge, I have not seen discussion of actively
targetted applications in the context of VPNs or other censored applications. Mobile Surveillance Monitor (MSM) Gary Miller's 
project is the closest project similar to our efforts. VPN alyzer is another similar, system for 
monitoring the security of VPNs, but we are different because we focus searching for and identifying
VPNs (and other apps).

// (Mobile Security Monitor Does actually)

Though it answers the main question, I wish I didn't have to do so much of my own digging to understand a given threat.
I had to manually search for very detailed info about DoNot malware, for example.

The majority of VPN projects focus on VPN security and not on whether attackers are actively targeting specific 
applications. This work moves in this direction by using proactive methods for threat hunting (deductive, inductive, active).

The lessons learned here can and already been applied beyond VPNs to other applications [CryptoSluice]().
In the future, further refinements should be performed and should be applied to the censored apps from
[applecensorship.com](applecensorship.com) and other potential sources as well.

# Background

## Project Dependency Diagram

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
         |
         |       v-stylometry<-Rachel Greenstadt
         \static<-code<-phylogensis<-who, *What we are doing*???
                 |     ^-Permissions<- VirusTotal
                 |     ^-static analysis<-obfuscation<-inconsistent type information between object and 
                 |                       ^-Something went here.
                 |
                 \- DNS name

analysis <- Apple some ML to answer some meaningful research question?

synthesis<-

# Methods



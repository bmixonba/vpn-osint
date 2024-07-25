# Introduction 

The community has largely focused understanding and overcoming online threats to
bring about a safer and more open Internet. The response to this problem is often
reactive, for example, by doing X when a particular app is blocked (what is the
communities response when an app is blocked? How do people go about getting
one?). VPNs are frequent targets of removal, blocking, impersionation, and other threats
because their ability to open closed networks is a thorn in the side of censors. 
From a user security perspective, VPNs are a high-risk application that attackers
target for exploitation because repressive governments continue requiring app stores 
to block them, as well as other apps. Something not currently being doing is the active
identificatoin of threats in the wild. This work uses multiple techniques to perform
this task

* Deducive techniques, such as OSINT intelligence gathering.
* Inductive techniques, CryptoSluice
* Actively, using typo-squating enumeration

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
be controlling the App. This is useful because to the best of my knowledge, I have not seen discussion of actively
targetted applications in the context of VPNs or other censored applications. The majority of VPN projects focus
on VPN security and not on whether attackers are actively targeting specific applications. This work moves
in this direction by using proactive methods for threat hunting (deductive, inductive, active).

The lessons learned here can and already been applied beyond VPNs to other applications [CryptoSluice]().
In the future, further refinements should be performed and should be applied to the censored apps from
[applecensorship.com](applecensorship.com) and other potential sources as well.

# Background

## Project Dependency Diagram

        v-open and crowd sourced 
        v-network<-cryptosluice/inductive
discvry<-phishing/typosquatting<-What we are doing
        ^-deductive<-OSINT analysis <- social media <- Dave Levin
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

analysis<- Apple some ML to answer some meaningful research question?

synthesis<-

# Overview

The VPN OSINT project is focused on bringing transparency to the VPN provider space to help users make better-informed decisions about who
they allow to see their network traffic.


# Deploy Server

## Development

Run:

0. If this is the first time you're running the code, create a virtual environment:

```bash
$ python3 -m venv src/.env
```

1. Run the server:
```bash
$ cd  src
(.env) $ ./setup_dev_server.sh 
 * Serving Flask app 'frontend'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
2. Browse to the server front end in your web browser:

![Development Server Homepage](imgs/vpnosintWebServerHome.png)

# Methodology

## App List Creation

The first step is building a list of VPN apps on which to focus. The obvious approach is to look
through repositories of apps, such as that provided by sensortower, manually going through the
VPN apps, and selecting a subset to focus analysis. While I will use this approach later, another
approach that should be considered is finding VPNs organically. For this, the first step is finding 
social media accounts, such as on telegram, youtube, twitter, etc., and finding references to VPNs
that way. Once one or more accounts have been identified, we can mark them and then explore their 
following, verified followers, and followers lists, profile hyper links, and text. 

1. 

## App Selection
### 

## Evaluation Metric 
### 



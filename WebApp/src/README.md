# Overview

This application is composed of 2 classes of view: Macro or Aggregate views and
Mirco or Individual views. The individual view presents information about a
specific VPN provider. The aggregate view presents information about a
selection of VPN providiers. The following views can represent information at
either the micro or macro-levels.

1. Geospatial

2. Relationship network

3. Timeline view

4. Executable view


# Starting the webapp

## Backend

To start the backend

```bash
$ cd git/vpn-osint-demo/src
$ python3 backend.py dbconf.json
```

## Frontend

To start the front end

```bash
$ cd git/vpn-osint-demo/src/vpnosint_app
$ npm start
```

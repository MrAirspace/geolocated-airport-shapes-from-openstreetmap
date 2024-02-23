# geolocated-airport-shapes-from-openstreetmap

Python script to extract geolocated airport terminal shapes using the overpass turbo API and openstreetmap data.

Delivers geojson files which can be applied in e.g. QGIS.

Output 1: Simple outer delineation of the terminal infra (DUS example):
![DUS_line](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/5c7a2d4f-fbfd-4903-bd10-60f6614dfea5)

Output 2: Complete merged terminal structure (DUS example):
![DUS_merged](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/5d05ec68-41b0-4355-a591-05bcc607317a)

Output 3: Detailed terminal structure with individual infra/piers (DUS example):
![DUS_piers](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/4c7afc19-946c-41f8-b854-c80828e81ce8)

Further Examples:

Singapore (SIN)
![SIN_merged](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/9839c440-1a87-4c0b-ac81-b7d95f56af14)

Zurich (ZRH)
![ZRH_merged](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/592a6f11-f1d0-43ca-8f69-87af5dcfcce1)

Amsterdam (AMS)
![AMS_merged](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/01c0514f-3a46-4483-bc2f-36efa99551ab)

Istanbul (IST)
![IST_merged](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/3eadce04-ccc9-4d23-ad5e-b73eeee3004e)

Rome (FCO)
![FCO_merged](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/46827d97-2ed1-4173-8c14-06678b3dedb7)

Dubai (DXB)
![DXB_merged](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/c76f2278-d1e1-4774-9063-01defd47fdd7)



**Troubleshooting:**

At present, the script is no complete approach. The output can feature incomplete terminal structures such as the following example:
![FRA_merged](https://github.com/MrAirspace/geolocated-airport-shapes-from-openstreetmap/assets/144953682/47d68bac-801c-412d-9ced-8e513d1fb977)

Reason for this is the way how infrastructure is classified in openstreetmap.
Normal approach to classify a terminal is: way["aeroway"="terminal"]

But sometimes part of the terminal infra is incorrectly formatted as: relation["aeroway"="terminal"]
In this case, those parts of the terminal are not yet extracted at present.


Another reason if the terminal infrastructure is incomplete could be a too-limited search radius in the python script. In that case, increase the integer to cover a wider search area.

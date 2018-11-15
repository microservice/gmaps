# Google Maps
This service is a wrapper around the official Python SDK for Google Maps API Web Services.

### Usage

```coffee
# Storyscript
result = gmaps geocode address: "Amsterdam, Netherlands"
result = gmaps reverse_geocode lat: 52.36015 lon: 4.89571
```

### TODOs
This is a WIP service, and as such, only a few APIs from the Google Maps SDK have
been exposed.

PRs are welcome.

The following APIs are yet to be implemented:
1. Directions API
2. Distance Matrix API
3. Elevation API
4. Time Zone API
5. Geolocation API
6. Places API
7. Roads API

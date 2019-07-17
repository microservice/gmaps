# _Google Maps_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)

This service is a wrapper around the official Python SDK for Google Maps API Web Services.

## Direct usage in [Storyscript](https://storyscript.io/):

##### Google Maps
```coffee
result = gmaps geocode address: "Amsterdam, Netherlands"
result = gmaps reverse_geocode lat: 52.36015 lon: 4.89571
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Geocode
```shell
$ omg run geocode -a address=<ADDRESS> -e API_KEY=<API_KEY>
```
##### Reverse Geocode
```shell
$ omg run reverse_geocode -a lat=<LATITUDE> -a lon=<LONGITUDE> -e API_KEY=<API_KEY>
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

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/gmaps/blob/master/LICENSE).

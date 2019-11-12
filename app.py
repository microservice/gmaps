# -*- coding: utf-8 -*-
import json
import os
import sys

import googlemaps

from flask import Flask, make_response, request


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.gmaps = googlemaps.Client(key=os.getenv("API_KEY"))

    def geocode(self):
        req = request.get_json()
        result = self.gmaps.geocode(req["address"])
        if len(result) > 0:
            return self.end(
                {
                    "lat": result[0]["geometry"]["location"]["lat"],
                    "lon": result[0]["geometry"]["location"]["lng"],
                }
            )

        return self.end({"error": "not_available"})

    def reverse_geocode(self):
        req = request.get_json()
        result = self.gmaps.reverse_geocode((req["lat"], req["lon"]))
        if len(result) == 0:
            return self.end({"error": "not_available"})

        state = ""
        city = ""
        country = ""
        for component in result[0]["address_components"]:
            types = component["types"]
            if "sublocality_level_1" in types:
                city = component["long_name"]
            elif "administrative_area_level_1" in types:
                state = component["long_name"]
            elif "country" in types:
                country = component["long_name"]

        return self.end(
            {"city": city, "state": state, "country": country, "full_response": result}
        )

    @staticmethod
    def end(res):
        resp = make_response(json.dumps(res))
        resp.headers["Content-Type"] = "application/json; charset=utf-8"
        return resp


if __name__ == "__main__":
    if os.getenv("API_KEY") is None:
        print("Environment variable API_KEY not found.")
        sys.exit(1)

    handler = Handler()
    # handler.app.debug = True
    handler.app.add_url_rule("/geocode", "geocode", handler.geocode, methods=["post"])
    handler.app.add_url_rule(
        "/reverse_geocode", "reverse_geocode", handler.reverse_geocode, methods=["post"]
    )
    handler.app.run(host="0.0.0.0", port=8000)

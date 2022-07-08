# packages
import requests
import json
import time
#tutorial---https://www.youtube.com/watch?v=R3jkosrWsE8&t=30s

# geocoder class
class Geocoder:
    # base url
    base_url = "https://nominatim.openstreetmap.org/search"

    # results
    results = []

    def fetch(self, address):

        params = {
            "q": address,
            "format": "geocodejson"
        }

        res = requests.get(url=self.base_url, params=params)
        print("HTTP GET request to URL: %s | Status code: %s" % (res.url, res.status_code))

        if res.status_code == 200:
            return res
        else:
            return None

    def parse(self, res):
        try:
            label = json.dumps(res["features"][0]["properties"]["geocoding"]["label"], indent=2)
            coordinates = "".join(json.dumps(res["features"][0]["geometry"]["coordinates"], indent=2)).replace("\n", "").replace("[", ""). replace("]", "").strip()
            # retrieved data
            self.results.append({
                "address": label,
                "coordinates": coordinates
            })
        except:
            pass

    def store_results(self):
        # write results to file
        with open("10_open_street_maps/results.json", "w") as f:
            f.write(json.dumps(self.results, indent=2))
    

    def run(self):
        # addresses list
        addresses = ""

        # fetch addresses from file
        with open("10_open_street_maps/addresses.txt", "r") as f:
            for line in f.read():
                addresses += line

        # convert addresses to list
        addresses = addresses.split("\n")

        # loop over addresses
        for address in addresses:
            res = self.fetch(address).json()
            self.parse(res)
            # respect Nominatim craling policies
            time.sleep(2)

        # store results
        self.store_results()


# main driver
if __name__ == "__main__":
    geocoder = Geocoder()
    geocoder.run()

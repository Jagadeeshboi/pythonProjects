import requests
from flight_data import FlightData


class Flight_data:

    def get_flight_code(self, city):
        url = "https://api.tequila.kiwi.com"
        key = {"apikey": "OfcgZEpZN1R6HuSV3-FeAmZx3_41K-1v"}
        data = {"term": city, "location-types": "city"}
        response = requests.get(url=f"{url}/locations/query", params=data, headers=key)
        result_data = response.json()["locations"]
        return result_data[0]

    def flight_from_source(self, fly_from, fly_to, date_from, date_to):
        url = "https://api.tequila.kiwi.com/v2/search"
        key = {"apikey": "OfcgZEpZN1R6HuSV3-FeAmZx3_41K-1v"}
        query = \
            {
                "fly_from": fly_from,
                "fly_to": fly_to,
                "date_from": date_from,
                "date_to": date_to,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }
        response = requests.get(url=url, headers=key, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print("flight not found from source to destination")

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        # print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

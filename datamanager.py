import requests

sheet_url = "https://api.sheety.co/b3299610867b85055f3d291e09834986/flightDeals/prices"
sheet_key = "Bearer hjstegju34gasj3i2"


class Sheet:
    def __int__(self):
        self.store = {}

    def get_sheet_data(self):
        key = {"Authorization": sheet_key}
        response = requests.get(url=sheet_url, headers=key)
        data = response.json()["prices"]
        self.store = data
        return self.store

    def update_data_sheet(self, id, iata_code):
        key = {"Authorization": sheet_key}
        data = {"price": {"iataCode": iata_code}}
        response = requests.put(url=f"{sheet_url}/{id}", json=data, headers=key)
        return response.text

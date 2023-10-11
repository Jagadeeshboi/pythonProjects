from flight_serach import Flight_data
from datamanager import Sheet
from datetime import datetime, timedelta
from notification import NotificationManager

fd = Flight_data()
s = Sheet()
tw = NotificationManager()

id = 2

source = "LON"

# for city in s.get_sheet_data():
#     m = fd.get_flight_code(city["city"])  //already filled  if new data entered remove comments
#     s.update_data_sheet(id, m["code"])
#     id += 1
tomorrow_date = datetime.now() + timedelta(days=1)
after_six_months = datetime.now() + timedelta(days=(6 * 30))
for city in s.get_sheet_data():
    s = fd.flight_from_source(fly_from=source, fly_to=city["iataCode"], date_from=tomorrow_date.strftime("%d/%m/%Y"),
                              date_to=after_six_months.strftime("%d/%m/%Y"))
    if s.price < city['lowestPrice']:
        tw.send_sms(message=f"Price Alert!\n ${s.price} from {s.origin_city} to {s.destination_city}\n from{s.out_date} to {s.return_date}")
        print(tw)

import requests
import json

from common import get_headers
from common_cars_info import *
headers = get_headers()
print(headers)

class CarSource4s:

    def __init__(self):
        c = CarsdaqApi()
        c.get_brand_with_hot()
        c.get_series()
        c.get_model(type=2)
        self.sell_price = (float(c.cars_info_4s['guided_price']))*1.3
        self.cars_info_4s = c.cars_info_4s

    def tripartite_store(self):
        url = "http://cweb.t.carsdaq.com/api/cars_source/tripartite_store"

        payload = {
            "source": "1",
            "type": "2",
            "company_id": "1361",
            "cars": self.cars_info_4s,
            "body_color": "白",
            "interior_color": "白",
            "sales_policy": "",
            "sell_price": self.sell_price,
            "store_num": "5",
            "frame_annex": "",
            "sell_area": "",
            "sell_location": "北京",
            "logistics_type": "2",
            "procedure_type": "1",
            "invoice_type": "2",
            "contact_name": "丽丽",
            "contact_phone": "132",
            "uploadCode": "361915383226906"
        }

        r = requests.post(url, headers=headers, data=payload)
        print('创建4S车源成功')
        print(r.text)


CarSource4s().tripartite_store()

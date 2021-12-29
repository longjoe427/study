import requests
import json
from common_cars_info import CarsdaqApi
from common import get_current_time, get_headers, be_json
from common_company import Company
from common import Public

headers = get_headers()
current_time = get_current_time()
agent_company = be_json(Company().company_relate())
print('agent_company:', agent_company)
upper_company = Company().search_company()


class CarSourceForeign():
    def __init__(self):
        c = CarsdaqApi()
        c.get_brand_with_hot()
        c.get_series()
        c.get_model(type=1)
        self.sell_price = (float(c.cars_info_fn['guided_price'])) * 1.3
        self.purchase_price = (float(c.cars_info_fn['guided_price'])) * 0.7
        self.sell_deposit_one = self.sell_price * 0.2
        # print('sell_deposit_one',self.sell_deposit_one)
        # print('self.sell_price', self.purchase_price)
        self.cars_info_fn = be_json(c.cars_info_fn)

    def store_cars_source(self):
        url = "http://cweb.t.carsdaq.com/api/cars_source/store_cars_source"

        payload = {
            "type": "1",
            "cars": self.cars_info_fn,
            "price_type": "1",
            "sell_price": self.sell_price,
            "purchase_price": self.purchase_price,
            "store_num": "3",
            "recent_transaction_price": "",
            "deposit_rate": "0.20",
            "sell_deposit_one": self.sell_deposit_one,
            "car_validity_time": current_time,
            "logistics_type": "[3]",
            "agent_company_id": "1367",
            "agent_company_name": "天蓝科技",
            "cars_trader_id": "1556",
            "agent_company": agent_company,
            "upper_company": upper_company,
            "pay_at": current_time,
            "carmodel": "北京",
            "province_id": "2",
            "city_id": "2",
            "sell_location": "北京",
            "sell_at": current_time,
            "business_type": "1",
            "invoice_type": "1",
            "invoice_time": current_time,
            "contact_name": "丽丽",
            "contact_phone": "132",
            "overdue_interest": "0.001",
            "cost_interest": "0.00022",
            "payment_period": "28",
            "cars_source_type": "1",
            "sell_area": "",
            "procedure_type": "2",
            "remark": "",
            "cars_img": "[]",
            "specification_type": "2",
            "logistics_type_name": "[{\"id\":3,\"name\":\"代寻物流\",\"select\":true}]",
            "status": "1"
        }

        r = requests.post(url, headers=headers, data=payload)
        print('创建平行进口车成功')
        print(r.text)


if __name__ == '__main__':
    c = CarSourceForeign()
    c.store_cars_source()

import json
import requests
from common_cars_info import CarsdaqApi
from common import get_current_time, get_headers, be_json
from common_company import Company
# from comm_company_member import *


# 初始化工作
headers = get_headers()
print('----%s---' % headers)
current_time = get_current_time()

agent_company = be_json(Company().company_relate())
print('agent_company:',agent_company)
upper_company = Company().search_company()
print('~~~~~')
print(upper_company)
# get_member()
#agent_company_id,agent_company_name,cars_trader_id


class Car_Source(object):

    def __init__(self):
        c = CarsdaqApi()
        c.get_brand_with_hot()
        c.get_series()
        c.get_model(type=1)
        self.sell_price = (float(c.cars_info_cn['guided_price']))*1.3
        self.purchase_price = (float(c.cars_info_cn['guided_price']))*0.7
        self.sell_deposit_one = self.sell_price * 0.2
        self.reduced_price = round(self.sell_price - self.purchase_price)
        self.sell_price_format = "{:.2f}".format(self.sell_price)


        # print('sell_deposit_one',self.sell_deposit_one)
        # print('self.sell_price', self.purchase_price)
        self.cars_info_cn = be_json(c.cars_info_cn)
        # print('------cars_info:', self.cars_info)
        # print('guided_price:',self.cars_info['guided_price'])
        # self.sell_price = round()
        # print('sell_price:',self.sell_price)
        # self.purchase_price = int((self.cars_info['guided_price'])*0.75)

        # print('----haha----')
        # print(c.cars_info)
        # print('初始化%s'%self.cars_info)
        # print('___%s___' % self.cars_info)

    def store_car_source(self):
        url = 'http://capi-t.carsdaq.com/api/cars_source/store_cars_source'
        payload = {
            "type": "1",
            "cars": self.cars_info_cn,
            "price_type": "1",
            "sell_price": round(self.sell_price),
            "purchase_price": round(self.purchase_price),
            "store_num": "2",
            "recent_transaction_price": "",
            "deposit_rate": "0.20",
            "sell_deposit_one": self.sell_deposit_one,
            "car_validity_time": current_time,
            "logistics_type": "[3]",
            "agent_company_id": "1367",
            "agent_company_name": "天蓝科技",
            "cars_trader_id": "1566",
            "agent_company": agent_company,
            "upper_company": upper_company,
            "pay_at": current_time,
            "carmodel": "北京",
            "province_id": 2,
            "city_id": 2,
            "sell_location": "北京",
            "sell_at": current_time,
            "business_type": "1",
            "invoice_type": "1",
            "invoice_time": current_time,
            "contact_name": "马林",
            "contact_phone": "15600895623",
            "overdue_interest": "0.0003",
            "cost_interest": "0.00022",
            "payment_period": "28",
            "cars_source_type": "1",
            "sell_area": "",
            "procedure_type": "",
            "remark": "",
            "cars_img": "[]",
            "logistics_type_name":'[{"id":1,"name":"上游包物流","select":false},{"id":2,"name":"下游自提","select":false},{"id":3,"name":"代寻物流","select":true}]',
            "status": "1",
            "guided_price":self.cars_info_cn['guided_price'],
            "reduced_price":self.reduced_price,
            "reduced_rate":'',
            "sell_price_format":self.sell_price_format



        }
        # print('payload：%s' % payload)
        # print(type(payload))
        payload = json.dumps(payload, ensure_ascii=False)
        # payload = be_json(payload).encode('utf-8').decode('latin1')
        r = requests.post(url, headers=headers, data=payload.encode('utf-8'))
        # print('创建中规车成功')
        print(r)
        # print(r.json())
        # print(r.json()['message'])


if __name__ == '__main__':
    c = Car_Source()
    c.store_car_source()

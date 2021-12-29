import requests
from common import Public, get_headers, be_json

headers = get_headers()

class Company(object):

    def __init__(self):
        self.headers = headers

    # 公司主体所需字段
    def company_relate(self):
        url = 'http://cweb.t.carsdaq.com/api/company_relate/list'
        payload = {
            'type': 2
        }
        r = requests.post(url, data=payload, headers=headers)
        print('company:',r.json())
        agent_company = r.json()['data'][0]['company']
        # print(agent_company)
        return agent_company

    # 选取公司，默认第一个公司
    def search_company(self):
        url = 'http://cweb.t.carsdaq.com/api/search_company'
        payload = {
            'keyword': '上',
            'limit': 20
        }
        r = requests.post(url, data=payload, headers=headers)
        print(r.json())
        global upper_company
        upper_company = r.json()['data'][0]
        print(upper_company)
        #修改属性值
        upper_company['actual_address']="北京朝阳"
        upper_company['company_type'] = 1
        upper_company.setdefault('vat_company_name',r.json()['data'][0]['vat'][0]['vat_company_name'])
        upper_company.setdefault('vat_bank_number',r.json()['data'][0]['vat'][0]['vat_bank_number'])
        upper_company.setdefault('vat_bank_branch',r.json()['data'][0]['vat'][0]['vat_bank_branch'])
        upper_company.setdefault('vat_bank_cnaps_code',r.json()['data'][0]['vat'][0]['vat_bank_cnaps_code'])
        upper_company.setdefault('vat_bank_name', r.json()['data'][0]['vat'][0]['vat_bank_branch'])
        # 增加
        upper_company['order_id'] = ""
        upper_company['order_number'] = ""
        # 删除
        del upper_company['enterprise_id']
        del upper_company['establish_time']
        del upper_company['business_term_start']
        del upper_company['business_term_end']
        del upper_company['business_scope']
        del upper_company['serial_number']
        del upper_company['type']
        del upper_company['client_attribute']
        del upper_company['source']
        del upper_company['sole_code']
        del upper_company['remark']
        del upper_company['handle_id']
        del upper_company['app_type']
        del upper_company['initials']
        del upper_company['status']
        del upper_company['admin_id']
        del upper_company['created_at']
        del upper_company['updated_at']
        del upper_company['deleted_at']
        del upper_company['agent_company_id']
        del upper_company['registered_capital']
        # print('----------------')
        # print('这是上游公司',upper_company)
        upper_company['company_id'] = upper_company.pop('id')
        upper_company = be_json(upper_company)
        print('hello', type(upper_company))
        print(upper_company)
        return upper_company

    def get_member(self):
        url = 'http://cweb-t.carsdaq.com/api/company/member/list'
        payload = {
            'rank':2
        }
        r = requests.post(url, data=payload, headers=headers)
        print(r.json())
        trader_info[trader_name] = r.json()['data'][0]['name']
        trader_info[trader_phone] = r.json()['data'][0]['phone']
        trader_info[trader_company_name] = r.json()['data'][0]
        trader_info[trader_num] = r.json()['data'][0]['trader_order_num']
        trader_info[company_trader_num] = r.json()['data'][0]['company_order_num']
        trader_info[trader_header_pic_url] = r.json()['data'][0]['header_pic']
        source_invoice_type_name = '增值税专用发票'
        type_name =r.json()['data'][0]['company']['type_name']




    def store_company(self):
        url = 'http://cweb.t.carsdaq.com/api/cars_source/store_company'
        # self.search_company()
        payload = upper_company.encode("utf-8").decode("latin1")
        print(payload)
        r = requests.post(url, data=payload, headers=headers)
        print(r.json())


c = Company()
c.company_relate()
c.search_company()
c.store_company()
c.get_member()

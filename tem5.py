import json
import requests
# from tem import change

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY2FwaS10LmNhcnNkYXEuY29tXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNjM4ODU1Nzk5LCJleHAiOjE3OTQzNzU3OTksIm5iZiI6MTYzODg1NTc5OSwianRpIjoiR2ZGV1M4ZHBmT1lWYXRpdSIsInN1YiI6MTU1NywicHJ2IjoiMDJlNDU0OTE4MzhmMDE1ZGY5MzA0N2U2NWJhNzdkNTIwZjg2Mjk4YyJ9.f_XKmkMUD53gGf3pA9DP6hHX15KbZ6QPEtVVlh2b_tM',
    'Content-Type': 'application/x-www-form-urlencoded',
    'carsdaq-app': 'ios',
    'carsdaq-app-env': 'test',
    'carsdaq-app-frame': 'vue2x',
    'carsdaq-driver-token': '64bb63bf6d1d552e3ec1164f4e12df66832ee2ec9bc536fa624288f7dd6a5e3a',
    'carsdaq-signature': '5DB4730E08738B3BA9C23A50126CC33D91229263',
    'carsdaq-timestamp': '',
    'carsdaq-version': '1.8.9',
    "carsdaq-H5-env": "test",
    "host": 'http://cweb-t.carsdaq.com',
    "User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148CarDak',
    'Accept-Encoding':'gzip, deflate, br',
    "Accept":'*/*',
    "Connection":'keep-alive',
    "Cookie":'__jsluid_s=a12bd80d115ddf9b17f8e9d091c08cb0'

}



# def store_car_source():
#     url = 'http://cweb-t.carsdaq.com/api/cars_source/store_cars_source'
#     payload = {
#         "type": "1",
#         "cars": '[{"brand_id":568,"brand_name":"大众","series_id":2586,"series_name":"途安","model_id":50474,"model_name":"2018款 途安L 280TSI DSG拓界豪华版 6座 国VI","guided_price":"194800.00","deposit_rate":0.2}]',
#         "sell_price": "200000",
#         "purchase_price": "190000",
#         "store_num": "5",
#         "recent_transaction_price": "",
#         "deposit_rate": "0.20",
#         "sell_deposit_one": "40000",
#         "car_validity_time": "2021-11-19",
#         "logistics_type": "[3]",
#         "agent_company_id": "1367",
#         "agent_company_name": "天蓝科技",
#         "cars_trader_id": "1556",
#         "agent_company": "{"id":1367,"enterprise_id":0,"company_name":"天蓝科技","company_tin":"12233333333","company_type":"","registered_capital":"","establish_time":null,"business_term_start":null,"business_term_end":null,"business_scope":null,"company_address":"北京昌平","actual_address":"","company_phone":"18900213459","bank_name":"安贞","bank_number":"6225778899002345","business_entity":"天宇","business_license":"[{\"key\": \"upload/png/20210628/test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png\", \"hash\": \"FvlxJfVM5fuj2_Mep9oODknbJJ5n\", \"name\": \"截屏2021-05-12 下午3.07.49 (2).png\", \"size\": 2942206, \"ftype\": \"png\"}]","business_entity_id_pic":"[]","serial_number":"A1","type":1,"client_attribute":2,"source":1,"sole_code":"","remark":null,"handle_id":1501,"app_type":3,"initials":"","status":1,"admin_id":0,"created_at":"2021-06-28 15:59:36","updated_at":"2021-11-22 10:28:55","deleted_at":null,"establish_time_format":"","business_term_start_format":"","business_term_end_format":"","business_license_url":"[{\"key\":\"upload\\/png\\/20210628\\/test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png\",\"hash\":\"FvlxJfVM5fuj2_Mep9oODknbJJ5n\",\"name\":\"\\u622a\\u5c4f2021-05-12 \\u4e0b\\u53483.07.49 (2).png\",\"size\":2942206,\"ftype\":\"png\",\"url\":\"https:\\/\\/pics.carsdaq.com\\/upload\\/png\\/20210628\\/test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png\",\"url_200x200\":\"https:\\/\\/pics.carsdaq.com\\/upload\\/png\\/20210628\\/test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png?imageView2\\/2\\/w\\/300\\/h\\/300\",\"file_name\":\"test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png\"}]","business_entity_id_pic_url":"","url":"https://pics.carsdaq.com/","type_name":"自营","client_attribute_name":"二网综合店","vat":[{"id":441,"company_id":1367,"vat_company_name":"卢氏","vat_bank_number":"sjjfj","vat_bank_branch":"安贞支行","vat_bank_cnaps_code":"","remark":"","handle_id":1501,"app_type":2,"status":1,"admin_id":0,"created_at":"2021-06-28 16:00:35","updated_at":"2021-11-26 17:42:15","deleted_at":null}],"vat_company_name":"卢氏","vat_bank_number":"sjjfj","vat_bank_name":"安贞支行","vat_bank_branch":"安贞支行","vat_bank_cnaps_code":"","company_id":1367}",
#         "upper_company": "{\"order_id\":\"\",\"order_number\":\"\",\"company_type\":1,\"company_id\":1365,\"vat_company_name\":\"nana\",\"vat_bank_name\":\"中关村支行\",\"vat_bank_number\":\"124674488\",\"vat_bank_branch\":\"中关村支行\",\"vat_bank_cnaps_code\":\"\",\"company_name\":\"新新宝马--上\",\"company_tin\":\"1254346\",\"company_address\":\"北京朝阳\",\"company_phone\":\"13255880096\",\"bank_name\":\"安贞\",\"bank_number\":\"6225880366988805\",\"business_entity\":\"大麦\",\"business_license\":\"[{\\\"key\\\": \\\"upload\/jpg\/20210628\/testxG8nU7Cas7RpBx35fA1GWsdctItOXw5MTrKnZvOx.jpg\\\", \\\"hash\\\": \\\"FrNaj_fXtNH2J_ZVvN39qsMdsbFV\\\", \\\"ftype\\\": \\\"jpg\\\"}]\",\"business_entity_id_pic\":null,\"actual_address\":\"cc\",\"contact_name\":\"马林\",\"contact_phone\":\"15600895623\",\"vat\":[{\"id\":466,\"company_id\":1365,\"vat_company_name\":\"nana\",\"vat_bank_number\":\"124674488\",\"vat_bank_branch\":\"中关村支行\",\"vat_bank_cnaps_code\":\"\",\"remark\":\"\",\"handle_id\":1557,\"app_type\":1,\"status\":1,\"admin_id\":0,\"created_at\":\"2021-10-26 14:36:32\",\"updated_at\":\"2021-11-19 10:33:13\",\"deleted_at\":null},{\"id\":465,\"company_id\":1365,\"vat_company_name\":\"nana\",\"vat_bank_number\":\"\",\"vat_bank_branch\":\"\",\"vat_bank_cnaps_code\":\"\",\"remark\":\"\",\"handle_id\":1557,\"app_type\":1,\"status\":1,\"admin_id\":0,\"created_at\":\"2021-10-20 17:53:49\",\"updated_at\":\"2021-11-08 14:14:02\",\"deleted_at\":null},{\"id\":439,\"company_id\":1365,\"vat_company_name\":\"么么\",\"vat_bank_number\":\"1236678\",\"vat_bank_branch\":\"625454845467\",\"vat_bank_cnaps_code\":\"\",\"remark\":\"\",\"handle_id\":1501,\"app_type\":2,\"status\":1,\"admin_id\":0,\"created_at\":\"2021-06-28 15:13:12\",\"updated_at\":\"2021-10-20 15:56:25\",\"deleted_at\":null}]}",
#         "pay_at": "2021-11-19",
#         "carmodel": "北京",
#         "province_id": "2",
#         "city_id": "2",
#         "sell_location": "北京",
#         "sell_at": "2021-11-19",
#         "business_type": "1",
#         "invoice_type": "1",
#         "invoice_time": "2021-11-19",
#         "contact_name": "马林",
#         "contact_phone": "15600895623",
#         "overdue_interest": "0.0001",
#         "cost_interest": "0.00022",
#         "payment_period": "28",
#         "cars_source_type": "1",
#         "sell_area": "",
#         "procedure_type": "",
#         "remark": "",
#         "cars_img": "[]",
#         "logistics_type_name": "[{\"id\":1,\"name\":\"上游包物流\",\"select\":false},{\"id\":2,\"name\":\"下游自提\",\"select\":false},{\"id\":3,\"name\":\"代寻物流\",\"select\":true}]",
#         "trader_info": {
#             "trader_name": "交易员--我是小白",
#             "trader_phone": "18000000046",
#             "trader_company_name": "龙珠汽车--自营",
#             "trader_num": "18",
#             "company_trader_num": "31",
#             "trader_header_pic_url": "https:\/\/pics.carsdaq.com\/upload\/jpg\/20211115\/testGdLRNQrEy6zoKwNQ8cQdCnOHYwJd8qviamvRcirv.jpg"
#         },
#         "sources_invoice_type_name": "增值税专用发票",
#         "type_name": "自营",
#         "guided_price": "194800.00",
#         "reduced_price": "-5200",
#         "reduced_rate": "-2.6",
#         "sell_price_format": "200000",
#         "status": "1"
#
#
#     }
#
#     # change(name=payload)
#     j = json.dumps(payload, ensure_ascii=False)
#     # print(j.encode('utf-8'))
#     r = requests.post(url, headers=headers, data=j)
#     print(r.status_code)

# store_car_source()

def get_member():
    url = 'http://cweb-t.carsdaq.com/api/company/member/list'
    payload = {
        'rank': 2
    }

    r = requests.post(url, data=payload, headers=headers)
    print(r)


get_member()

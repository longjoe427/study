import requests

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY2FwaS10LmNhcnNkYXEuY29tXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNjM3MzAwMjM2LCJleHAiOjE3OTI4MjAyMzYsIm5iZiI6MTYzNzMwMDIzNiwianRpIjoiWTlUbzBBc2NBUkczV3FEYyIsInN1YiI6MTczMywicHJ2IjoiMDJlNDU0OTE4MzhmMDE1ZGY5MzA0N2U2NWJhNzdkNTIwZjg2Mjk4YyJ9.Y23ez-TXt_49gX_aw93aJV17ji8uwSt4hpEDzMVzRi8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'carsdaq-app': 'ios',
    'carsdaq-app-env': 'test',
    'carsdaq-app-frame': 'vue2x',
    'carsdaq-driver-token': '64bb63bf6d1d552e3ec1164f4e12df66832ee2ec9bc536fa624288f7dd6a5e3a',
    'carsdaq-signature': '5DB4730E08738B3BA9C23A50126CC33D91229263',
    'carsdaq-timestamp': '',
    'carsdaq-version': '1.8.9',
    "carsdaq-H5-env": "production",
    "host": 'http://cweb-t.carsdaq.com'

}


def store_car_source():
    url = 'http://cweb-t.carsdaq.com/api/cars_source/store_cars_source'
    payload = {'type': '1',
               'cars': '{"brand_id": 569, "brand_name": "标致", "series_id": 3563, "series_name": "标致308", "model_id": 50816, "model_name": "230THP 自动豪华版 国VI", "guided_price": "120700.00", "deposit_rate": 0.2}',
               'price_type': '1',
               'sell_price': 156910.0,
               'purchase_price': 84490.0,
               'store_num': '2',
               'recent_transaction_price': '',
               'deposit_rate': '0.20',
               'sell_deposit_one': 31382.0,
               'car_validity_time': '2021-11-19',
               'logistics_type': '[3]',
               'agent_company_id': '1367',
               'agent_company_name': '天蓝科技',
               'cars_trader_id': '1566',
               'agent_company': '{"id": 1367, "enterprise_id": 0, "company_name": "天蓝科技", "company_tin": "12233333333", "company_type": "", "registered_capital": "", "establish_time": null, "business_term_start": null, "business_term_end": null, "business_scope": null, "company_address": "北京昌平", "actual_address": "", "company_phone": "18900213458", "bank_name": "安贞", "bank_number": "6225778899002345", "business_entity": "天宇", "business_license": "[{\\"key\\": \\"upload/png/20210628/test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png\\", \\"hash\\": \\"FvlxJfVM5fuj2_Mep9oODknbJJ5n\\", \\"name\\": \\"截屏2021-05-12 下午3.07.49 (2).png\\", \\"size\\": 2942206, \\"ftype\\": \\"png\\"}]", "business_entity_id_pic": "[]", "serial_number": "A1", "type": 1, "client_attribute": 2, "source": 1, "sole_code": "", "remark": null, "handle_id": 1501, "app_type": 3, "initials": "", "status": 1, "admin_id": 0, "created_at": "2021-06-28 15:59:36", "updated_at": "2021-11-17 18:39:13", "deleted_at": null, "establish_time_format": "", "business_term_start_format": "", "business_term_end_format": "", "business_license_url": "[{\\"key\\":\\"upload\\\\/png\\\\/20210628\\\\/test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png\\",\\"hash\\":\\"FvlxJfVM5fuj2_Mep9oODknbJJ5n\\",\\"name\\":\\"\\\\u622a\\\\u5c4f2021-05-12 \\\\u4e0b\\\\u53483.07.49 (2).png\\",\\"size\\":2942206,\\"ftype\\":\\"png\\",\\"url\\":\\"https:\\\\/\\\\/pics.carsdaq.com\\\\/upload\\\\/png\\\\/20210628\\\\/test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png\\",\\"url_200x200\\":\\"https:\\\\/\\\\/pics.carsdaq.com\\\\/upload\\\\/png\\\\/20210628\\\\/test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png?imageView2\\\\/2\\\\/w\\\\/300\\\\/h\\\\/300\\",\\"file_name\\":\\"test1iyI6SUweNMDhTCpqHWqBw12FSJGdtJNgKzZxX8h.png\\"}]", "business_entity_id_pic_url": "", "url": "https://pics.carsdaq.com/", "type_name": "自营", "client_attribute_name": "二网综合店"}',
               'upper_company': '{"company_name": "新新宝马--上", "company_tin": "1254346", "company_type": 1, "registered_capital": "", "company_address": "北京朝阳", "actual_address": "北京朝阳", "company_phone": "13255880096", "bank_name": "安贞", "bank_number": "6225880366988805", "business_entity": "大麦", "business_license": "[{\\"key\\": \\"upload/jpg/20210628/testxG8nU7Cas7RpBx35fA1GWsdctItOXw5MTrKnZvOx.jpg\\", \\"hash\\": \\"FrNaj_fXtNH2J_ZVvN39qsMdsbFV\\", \\"ftype\\": \\"jpg\\"}]", "business_entity_id_pic": null, "contact_name": "马林", "contact_phone": "15600895623", "vat": [{"id": 466, "company_id": 1365, "vat_company_name": "nana", "vat_bank_number": "124674488", "vat_bank_branch": "中关村支行", "vat_bank_cnaps_code": "", "remark": "", "handle_id": 1557, "app_type": 1, "status": 1, "admin_id": 0, "created_at": "2021-10-26 14:36:32", "updated_at": "2021-11-19 10:33:13", "deleted_at": null}, {"id": 465, "company_id": 1365, "vat_company_name": "nana", "vat_bank_number": "", "vat_bank_branch": "", "vat_bank_cnaps_code": "", "remark": "", "handle_id": 1557, "app_type": 1, "status": 1, "admin_id": 0, "created_at": "2021-10-20 17:53:49", "updated_at": "2021-11-08 14:14:02", "deleted_at": null}, {"id": 439, "company_id": 1365, "vat_company_name": "么么", "vat_bank_number": "1236678", "vat_bank_branch": "625454845467", "vat_bank_cnaps_code": "", "remark": "", "handle_id": 1501, "app_type": 2, "status": 1, "admin_id": 0, "created_at": "2021-06-28 15:13:12", "updated_at": "2021-10-20 15:56:25", "deleted_at": null}], "vat_company_name": "nana", "vat_bank_number": "124674488", "vat_bank_branch": "中关村支行", "vat_bank_cnaps_code": "", "vat_bank_name": "中关村支行", "order_id": "", "order_number": "", "company_id": 1365}',
               'pay_at': '2021-11-19',
               'carmodel': '北京',
               'province_id': 2,
               'city_id': 2,
               'sell_location': '北京',
               'sell_at': '2021-11-19',
               'business_type': '1',
               'invoice_type': '1',
               'invoice_time': '2021-11-19',
               'contact_name': '马林',
               'contact_phone': '15600895623',
               'overdue_interest': '0.0003',
               'cost_interest': '0.00022',
               'payment_period': '28',
               'cars_source_type': '1',
               'sell_area': '',
               'procedure_type': '',
               'remark': '',
               'cars_img': '[]',
               'logistics_type_name': '[{"id":1,"name":"上游包物流","select":false},{"id":2,"name":"下游自提","select":false},{"id":3,"name":"代寻物流","select":true}]',
               'status': '1'
               }

    r = requests.post(url, headers=headers, data=payload)
    print(r.status_code)


store_car_source()

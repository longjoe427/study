import json
import random
import requests
from common import Public, get_headers

headers = get_headers()


class CarsdaqApi(object):
    cars_info_cn = None
    cars_info_4s = None
    cars_info_fn = None

    def __init__(self):
        self.headers = headers

    # 获取brand_id, brand_name
    def get_brand_with_hot(self, **kwargs):
        if kwargs == {}:
            # 随机得到brand_id
            brand_ids = [569, 577, 612, 581, 568]
            num_id = len(brand_ids)
            index = random.randint(0, num_id - 1)
            global brand_id
            brand_id = brand_ids[index]
            print(brand_id)
            # 获取brand_name
            url = 'http://cweb.t.carsdaq.com/api/get_brand_with_hot'
            r = requests.post(url, headers=headers)
            # print('-----%s---'%r.json())
            # try
            hot_id = list(r.json()['data']['brand'].values())
            # print(hot_id)
            for brand_list in hot_id:
                # print(brand_list)
                for dict in brand_list:
                    # print(dict)
                    if dict['id'] == brand_id:
                        brand_name = dict['name']
                        # print(brand_name)
                        global dic_brand
                        dic_brand = {'brand_id': brand_id, 'brand_name': brand_name}
                        # self.cars_info.append(dic_brand)
                        # print('第一个%s' % self.cars_info)
                        # return brand_id
        elif kwargs == {'parallel': 3}:
            url = 'http://cweb.t.carsdaq.com/api/get_brand_with_hot'
            payload = {
                'parallel':3
            }
            r = requests.post(url,data=payload, headers=headers)
            hot_data = r.json()['data']['hot'][0]
            global brand_id_fn
            brand_id_fn = hot_data['id']
            brand_name_fn = hot_data['name']
            global dic_brand_fn
            dic_brand_fn = {'brand_id':brand_id_fn,'brand_name':brand_name_fn}
            # print(dic_brand_fn)
            return brand_id_fn




    def get_series(self,**kwargs):
        if kwargs=={}:
            url = 'http://cweb.t.carsdaq.com/api/get_series'
            payload = {
                'brand_id': brand_id
            }
            r = requests.post(url, data=payload, headers=headers)
            # print(r.json())
            # 获取data的值，key是变量，不使用，使用dict.values()方法
            series = r.json()['data'].values()
            # 去掉前缀dict_values()，再获取list里面的value
            series_value = list(series)[0]
            # 获取车系的个数
            series_num = len(series_value)
            # 随机获取一个车系的索引
            index = random.randint(0, series_num - 1)
            # global series_id,series_name
            global series_id
            series_id = series_value[index]['id']
            series_name = series_value[index]['name']
            # print(series_id, series_name)
            dict_series = {'series_id': series_id, 'series_name': series_name}
            # self.get_brand_with_hot()
            # print('这是%s ' % dict_series)
            dic_brand.update(dict_series)
            print(dic_brand)
            return series_id
        elif kwargs != {}:
            url = 'http://cweb.t.carsdaq.com/api/get_series'
            payload = {
                'brand_id': brand_id_fn,
                'parallel':3
            }
            r = requests.post(url, data=payload, headers=headers)
            series_data =r.json()['data']['平行进口'][0]
            series_id_fn = series_data['id']
            series_name_fn = series_data['name']
            dict_series_fn = {'series_id': series_id_fn, 'series_name': series_name_fn}
            dict_series_fn.update(dic_brand_fn)
            # print(dict_series_fn)
            dict_series_fn['specification_id']=0
            dict_series_fn['specification_name']='美规'
            dict_series_fn['body_color']='白'
            dict_series_fn['interior_color']='白'
            dict_series_fn['model_name']='22款 3.0T'
            #平行进口各种成本
            cars_info_other = {"buy_car_advance_fund_cost":'',"invoice_cost":"","carriage_cost":"","inventory_cost":"", "other_cost":""}
            dict_series_fn['cars_computing_information']= cars_info_other
            print(dict_series_fn)
            self.cars_info_fn = dict_series_fn
            cars_info_fn = json.dumps(self.cars_info_fn, ensure_ascii=False)
            return cars_info_fn






    def get_model(self, type):
        url = 'http://cweb.t.carsdaq.com/api/get_model'
        payload = {
            'series_id': series_id
        }
        r = requests.post(url, data=payload, headers=headers)
        print('-------------')
        print(r.json())
        if r.json()['data'] != []:
            # 获取data下，年款里的最的第一个年款的值,再获取值里第一个
            the_model_first = list(r.json()['data'].values())[0][0]
            model_id = the_model_first['id']
            model_name = the_model_first['name']
            guided_price = the_model_first['price']
            dict_model = {'model_id': model_id, 'model_name': model_name, 'guided_price': guided_price}
            if type == 1:

                dict_model_cn = dict_model
                dict_model_cn['deposit_rate'] = 0.2
                dic_brand_cn = dic_brand
                dic_brand_cn.update(dict_model_cn)
                print(dic_brand_cn)
                self.cars_info_cn = dic_brand_cn
                cars_info_cn = json.dumps(self.cars_info_cn, ensure_ascii=False)
                return cars_info_cn

            elif type == 2:
                # 4S店车辆数据
                dict_model_4s = dict_model
                dict_model_4s['body_color'] = '白'
                dict_model_4s['interior_color'] = '白'
                dic_brand_4s = dic_brand
                if 'deposit_rate' in dic_brand_4s.keys():
                    del dic_brand_4s['deposit_rate']
                    # print("hahah")
                    # print('删除后dic_brand_4s',dic_brand_4s)
                    return dic_brand_4s
                dic_brand_4s.update(dict_model_4s)
                # print('------',dic_brand_4s)
                self.cars_info_4s = dic_brand_4s
                cars_info_4s= json.dumps(self.cars_info_4s, ensure_ascii=False)
                return cars_info_4s
        else:
            r = requests.post(url, data=payload, headers=headers)


c = CarsdaqApi()
c.get_brand_with_hot()
c.get_brand_with_hot(parallel=3)
c.get_series()
c.get_series(brand_id=brand_id_fn,parallel=3)
c.get_model(type=2)
c.get_model(type=1)


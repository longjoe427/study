import requests


def get_member():
    url = "http://cweb-t.carsdaq.com/api/company/member/list"

    payload = 'rank=2'
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY2FwaS10LmNhcnNkYXEuY29tXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNjM2NDM2NzgzLCJleHAiOjE3OTE5NTY3ODMsIm5iZiI6MTYzNjQzNjc4MywianRpIjoic0pwRDVtMlF6VE92dTFTNyIsInN1YiI6MTUwMSwicHJ2IjoiMDJlNDU0OTE4MzhmMDE1ZGY5MzA0N2U2NWJhNzdkNTIwZjg2Mjk4YyJ9.UMsDb7Pfwi6NVYoOyP0TcOvIWG57pKWjJ4o8aHNaD_A',
        'carsdaq-app': 'ios',
        'carsdaq-H5-env': 'production',
        'carsdaq-version': '1.8.2',
        'carsdaq-app-env': 'test',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'cweb-t.carsdaq.com',
        'Cookie': '__jsluid_h=01f200015a6ae502804de7047de6fd20',
        'User-Agent': 'Mozila 2.0'
    }

    r = requests.request("POST", url, headers=headers, data=payload)
    print(r.json())
    global cars_trader_id
    cars_trader_id = r.json()['data'][0]['id']
    print(cars_trader_id)

    return cars_trader_id

get_member()
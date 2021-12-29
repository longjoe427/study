import requests

url = "https://cweb-t.carsdaq.com/api/company/member/list"

payload={'rank': '2'}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY2FwaS10LmNhcnNkYXEuY29tXC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNjM4ODU1Nzk5LCJleHAiOjE3OTQzNzU3OTksIm5iZiI6MTYzODg1NTc5OSwianRpIjoiR2ZGV1M4ZHBmT1lWYXRpdSIsInN1YiI6MTU1NywicHJ2IjoiMDJlNDU0OTE4MzhmMDE1ZGY5MzA0N2U2NWJhNzdkNTIwZjg2Mjk4YyJ9.f_XKmkMUD53gGf3pA9DP6hHX15KbZ6QPEtVVlh2b_tM',
  'carsdaq-app': 'ios',
  'host': 'cweb-t.carsdaq.com',
  'Content-Type': 'application/x-www-form-urlencoded',
  'carsdaq-app-env': 'test',
  'carsdaq-app-frame': 'vue2x',
  'carsdaq-driver-token': '64bb63bf6d1d552e3ec1164f4e12df66832ee2ec9bc536fa624288f7dd6a5e3a',
  'carsdaq-signature': '5DB4730E08738B3BA9C23A50126CC33D91229263',
  'carsdaq-timestamp': '',
  'carsdaq-version': '1.8.9',
  'carsdaq-H5-env': 'test',
    "User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148CarDak'

}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

print('{:.2f}'.format(20000.115))
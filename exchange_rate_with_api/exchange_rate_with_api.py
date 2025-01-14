import requests
from datetime import datetime
class Currency:
    def __init__(self):
        self.api_key = open('exchange_rate_with_api/api_key.txt').readline().strip()

        # self.url = f'http://api.exchangeratesapi.io/v1/latest?access_key={self.api_key}&base=USD'
        #You can also specify only the symbols you want to see e.g GBP, JPY, EUR

        self.url = f'http://api.exchangeratesapi.io/v1/latest?access_key={self.api_key}'
        self.output = ''
        # self.file_name = datetime.now().strftime('%d %b - %Y')
        # print(self.file_name)

    def do_request(self):
        res = requests.get(self.url)

        #This is very important for debugging when working with apis
        # print(res.status_code, res.text)

        if res.status_code == 200:
            self.output = res.json()

    def write_to_file(self):
        print(self.output['rates']['USD'])

c = Currency()
c.do_request()
c.write_to_file()
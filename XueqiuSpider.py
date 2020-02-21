import requests
import re
import json
import datetime

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'xueqiu.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

req_url = 'https://xueqiu.com/S/'

pattern = r'.*quote:(.*),.*'
time_pattern = r'(\d+-\d+)'

## fetch raw data from stock
def stock_getter_and_parser(stock_code, stock_source='SH', target=['open', 'name', 'current', 'chg', 'percent']):
    url = req_url + stock_source + stock_code
    res_json = {}

    response = requests.get(url, headers=header)
    response_json = json.loads(re.findall(pattern, response.text)[0])
    for key in target:
        if key in response_json:
            res_json[key] = response_json[key]
    res_json['stock_code'] = stock_code

    ## get end_date and cur_date
    end_date = re.findall(time_pattern, response_json['parsedTime'])[0]
    res_json['cur_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
    res_json['end_date'] = '{0}-{1}'.format(datetime.datetime.now().year, end_date)
    res_json['status'] = response_json['quoteMarket']['status']

    return json.dumps(res_json)

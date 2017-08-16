import requests
import re
import json

sina_sz_list = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/' \
               'Market_Center.getHQNodeData?page=1&num=4000&sort=symbol&asc=1&node=sz_a&_s_r_a=init'

sina_sh_list = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/' \
               'Market_Center.getHQNodeData?page=1&num=4000&sort=symbol&asc=1&node=sh_a&_s_r_a=init'


def get_sz_stock_from_sina():
    raw_result = requests.get(sina_sz_list)
    if raw_result.status_code == 200:
        return _format_result(raw_result.text)


def _format_result(result):
    # utf_result = result.decode('gbk').encode('utf8')
    regex = r"(?i)\b([a-z]+)(:)"
    quota_result = re.sub(regex, _quota_surround, result)
    # print ddd
    return json.loads(quota_result)


def _quota_surround(match):
    return '"' + match.group(1) + '"' + match.group(2)


if __name__ == '__main__':
    print(get_sz_stock_from_sina())

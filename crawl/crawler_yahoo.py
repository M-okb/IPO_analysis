from pyquery import PyQuery as pq
from urllib import request
from urllib.error import URLError
import csv, time

with open('old_comps.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    comp_list = []
    for row in reader:
        comp_list.append(row[0])

master = 'http://stocks.finance.yahoo.co.jp/stocks/detail/?code='
result = []
for comp in comp_list:
    url = master + comp
    resp = request.urlopen(url)
    html = resp.read()
    obj = pq(html)
    industry = obj.find('.yjSb a').text()
    result.append([comp, industry])
    time.sleep(5)
    print(comp)

with open('yhoo_industry.csv', 'w', encoding='shift-jis') as f:
    writer = csv.writer(f)
    header = ['company', 'industry']
    writer.writerow(header)
    for elm in result:
        writer.writerow(elm)

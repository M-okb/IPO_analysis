# -*- coding: utf-8 -*-
import time
import csv
from pyquery import PyQuery as pq
from urllib import request
from urllib.error import URLError


with open('ipo_companylist2.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    comp_list = []
    for row in reader:
        comp_list.append(row[0])

master_url =  'http://www.traders.co.jp/ipo_info/schedule/ipo_info.asp?no='

result = []

for (i,comp) in enumerate(comp_list):
    time.sleep(1)
    url = master_url + comp
    try:
        #   クローリング
        resp = request.urlopen(url)
        html = resp.read()
        obj = pq(html)
        #   以下cssセレクタで指定してスクレイピング
        #   csvで保存する都合上','は徹底的に殺す
        #   上場日
        off_date = obj.find(" td:contains('上場') + td").text().split(' ')[0]
        #   公開価格
        off_price = int(obj.find(" td:contains('公開価格') + td").text().split(' ')[1].replace(',', ''))
        #   初値
        opn_price = int(obj.find(" td:contains('初値') + td").text().split(' ')[1].replace(',', ''))
        #   仮条件価格（'\u3000'は全角空白）
        fileprice = obj.find(" td:contains('仮条件') + td").text().split(' ')[1].replace(',', '').split('\u3000〜\u3000')
        fileprice_min = int(fileprice[0])
        fileprice_max = int(fileprice[1])
        #   公開株数、公募、売出、オーバーアロットメント（非定型なので後で区切る）
        totaloffer = obj.find(" td:contains('公開株数') + td").text().replace(',', '').replace('株) 単位（株）', '').replace('株)', '')
        if totaloffer.count('公募') == 1:
            totaloffer, others = totaloffer.split('株（公募')
            if others.count('売り出し') == 1:
                prim_offer, others = others.split('株、売り出し')
                totaloffer = int(totaloffer)
                prim_offer = int(prim_offer)
                others = others.split('株、オーバーアロットメント')
                if len(others) == 2:
                    seco_offer = int(others[0])
                    overallot = int(others[1])
                else:
                    seco_offer = int(others[0])
                    overallot = 0
            else:
                prim_offer, others = others.split('株、オーバーアロットメント')
                prim_offer = int(prim_offer)
                seco_offer = 0
                overallot = int(others)
        else:
            totaloffer, others = totaloffer.split('株（売り出し')
            totaloffer = int(totaloffer)
            prim_offer = 0
            seco_offer = int(others)
            overallot = 0
        #   単元
        trading_unit = int(obj.find(" td:contains('売買単位')").text().replace('売買単位／', '').replace('株', ''))
        #   設立年（元年表記と西暦表記がある、なぜか'M35年'表記も）
        found_year = obj.find(" td:contains('設立年') + td").text().replace('年', '')
        if found_year[0] == 'S' or found_year[0] == 'M':
            found_year = int(found_year[1:]) + 1925
        elif found_year[0] == 'H':
            found_year = int(found_year[1:]) + 1988
        else:
            found_year = int(found_year)
        #   業種
        industry = obj.find(" td:contains('業種')").text().replace('業種／', '')
        #   市場
        market = obj.find(" td:contains('市場')").text().replace('市場／', '')
        result.append([comp, off_date, off_price, opn_price, trading_unit, fileprice_min, fileprice_max, totaloffer,
        prim_offer, seco_offer, overallot, found_year, industry, market])
    except URLError:
        print('url error at '+ comp)
    except ValueError:
        print('value error at '+ comp)
    except IndexError:
        print('index error at ' + comp)
    finally:
        print(i)

with open('ipodata.csv', 'w', encoding='shift-jis') as f:
    writer = csv.writer(f)
    header = ['security code', 'offering date', 'offering price', 'opening price', 'trading unit', 'fileprice min', 'fileprice max', 'total offering',
        'primary offering', 'secondary offering', 'over allotment', 'founding year', 'industry', 'market']
    writer.writerow(header)
    for elm in result:
        writer.writerow(elm)

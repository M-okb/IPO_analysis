# IPO_analysis
卒論データ＆ソースコード保存用レポジトリ

## データソース
大まかに言って、慶応大学の金子隆先生~~(金子勝ではない)~~の研究における既存データセットと、  
自分でクローラを回して取得したデータに別れます。
* **Data_Set_of_Book-built_IPOs_Ver_1.3.xls**  
1997年から2009年の日本のIPOに関するデータ。初値以降の株価推移データはない。  
[Kaneko and Pettway’s Japanese IPO Database](http://www.fbc.keio.ac.jp/~kaneko/KP-JIPO/top.htm)から頂戴しました。  

* **クロールしたもの**  
2010年以降のデータは
  - [総合投資情報サイト](http://www.traders.co.jp)
  - [yahoo finance](http://stocks.finance.yahoo.co.jp)  
から頂戴しています。  
~~Yahoo!は実はクロールに厳しい~~  
[ここ](https://github.com/M-okb/IPO_analysis/tree/master/crawl)を見てもらえれば非定型の表記に対してどう頑張ったかが見て取れるハズ

## メモ
* okb_ipo_treated.csv
  - クロールしたデータをまとめてダミーとか部分的に作ったもの
  - 変数の説明
    * **主幹事ダミー**  
    野村と大和と日興とみずほとSBIだけ作った。ふつーに多い順。有意差出たら面白いね
    * **marketダミー**  
    1だと新興市場、0だと既存市場（東証1,2,福証など）
    * **industry変数**  
    日本の33業種コードまんま。対応表もアップしております

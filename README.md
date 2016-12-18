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
から頂戴しています。</br></br>
~~Yahoo!は実はクロールに厳しい~~   </br></br>
クロールしているとは言え、 ウェブページの形式が非定型であったので、  
ゴリ押ししているところも多いです。

## データについて
前述のデータソースから集めたデータをまとめたcsvファイルを[ここ](https://github.com/M-okb/IPO_analysis/blob/master/data/IPO_1997_2016.csv)に保存してあります。  
* 1997年9月に上場した株式会社フォトロン（現：株式会社イマジカ・ロボット ホールディングス）から、   
2016年12月に上場した株式会社グッドコムアセットまでの、計1962社を扱っています。
* 上場中止した企業（例：株式会社ZMP）は扱っていません。  
* また、J-REIT（例：星野リゾート・リート投資法人）も扱っていません。  
* 変数について
  - **offer date**   
  上場日を8桁で示したもの。（yyyymmdd）
  - **offer price**  
  公募価格。（円）
  - **opening price**  
  上場初日に、株式市場で初めてつけられた価格。（円）  
  - **fileprice min**  
  主幹事証券会社がブックビルディングを行った価格帯の下限。（円）
  - **fileprice max**  
  その上限。（円）
  - **industry**  
  証券コード協議会が定める33業種の分類。[このファイル](https://github.com/M-okb/IPO_analysis/blob/master/data/industry_correspondence.csv)を参照。
  - **founding year**  
  当該企業が設立された年度。（yyyy）
  - **trading unit**  
  株式市場での取引の最小単位である単元株式数。（株）
  - **total offering**  
  IPOにおける、総公開株式数（株）
  - **primary offering**  
  公募株式数。IPOにあたり、新規に発行した株式数。（株）
  - **secondary offering**  
  売出株式数。既存株主が、保有している株式を投資家に売り出した株式数。（株）
  - **over allotment**  
  主幹事が既存株主から一旦株を借り、投資家に追加で売り出した株式数。  
  公募・売出の数量を上回る需要があったときに、その15%を上限として行われる。（株）
  - **market dummy**  
  上場先がJASDAQ（旧店頭市場、大証ヘラクレス、NEO含む）、マザーズ、福証Q-Board、  
  札証アンビシャス、名証セントレックスなどの新興市場に上場する場合に1を、それ以外で0を取るダミー変数。（Boolian）
  - **Nomura dummy ~ SBI dummy**  
  それぞれ、主幹事が、野村、大和、日興、みずほ、SBIであったときに1を、  
  それ以外で0を取るダミー変数。（Boolian）

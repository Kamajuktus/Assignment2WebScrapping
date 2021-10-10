Assignment 2

Installation
Import this project in your project as following: from assignment2WebScrapping.src.scrapCryptInfo import CryptInfoScrapper

Usage
Create an instance of CryptInfoScrapper class:
infoScrapper = CryptInfoScrapper()

Call scrapCryptInfo function and pass the name of cryptocurrency as a parameter:

infoScrapper.scrapCryptInfo("bitcoin")

Examples
Function will search first 100 cryptocurrencies' information listed on https://coinmarketcap.com.

Output will be like following:

1
Bitcoin1BTCBuy
$54,907.77    
0.02%
14.85%        
$1.03T$1,034,443,225,777
$36,923,893,570672,471 BTC
18,839,650 BTC




Bitcoin CashBCH
$615.73



Wrapped BitcoinWBTC
$54990.24



Bitcoin BEP2BTCB
$55107.86



Bitcoin SVBSV
$178.90



Bitcoin GoldBTG
$70.08
#python main.py
#以下代码用于抓取数据
import requests as req
import json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
import re
import csv

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0","Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Type": "application/json",}
cookies={"JSESSIONID":"534889F2B3335CE723F96AFC5FF86D6D"}
all_payload = [{"cid":"d153132154a549a78363017ef74ca784","indicatorIds":["305bba1e881e413b91f32a06a4be65fd","c6529a19138449da88a4ba2b75ff6259","bf74960bda394547bc1c3a39a70153c1","7ecd7929579346b4bbf592e9036d3a16","d3ad1dd4653a41e59a5c93406de31432","60001f8e97f649a8bd802da441ad4a67","88cc24ad47ac4167bcca1acb756b5dd7","ec3ac7ae3a874a0cbde431b726577567","a41674feee1d472c930f206b6e43a19f","50ed8aa668f040e6a8fb56029fc27a48","679e3e40b723423e8ed9e69941148fca","b00e93cb5f444c63a6919a3d742fe22d"],"daCatalogId":"","das":[{"text":"全国","value":"000000000000"}],"showType":"1","dts":"","rootId":"884c062607104a91967b22742537f44f"},
           {"cid":"d310e3ead14b403d9d10d29391713783","indicatorIds":["c0908d6012a840dca82d2b362f7e2d69","9952c1961a234ac7be34b1d5d12f50e0","fd8eb198215844e98212797eae2b8665","b9fc88fa0f3e4c53808ce5157cbec9ae","cd86ebda61564c6e8f0cec26fe7e16ee","ba5c724b95df46c0ba414ff077360b69","86bd99e4c4cb4471b6e1ff3c92aa9f93","67903f3fc6a74403b0925836d8794aac","ad835f138e544de087f2c1590b9194dd","cb86b8a8e01447d4ad1c11ce4ee6fcad","3440e871326142d18b060aaf2e0b4833","ea356053e36f4efe8367f6f618f1ff57"],"daCatalogId":"","das":[{"text":"全国","value":"000000000000"}],"showType":"1","dts":"","rootId":"884c062607104a91967b22742537f44f"},
           {"cid":"7bd16d8e47ee44109280d7e8ce4cafe9","indicatorIds":["b5040ecf88fd469591909ee04df59147","88ac9ad8bd834512989342a19fa54d00","d7d9d55536314632a5d6419bace68267","ec5d419ca78941dea8b2a63d27da915b","ad10dbe9c5264e969fffce2c078aa86d","581a9537334844c294ae6584cdc6b6a8","0462911888344970b87d97742f2eb626","1cb0a489ee1846db8adee29fab322c39","66b676fbe0b1445da89546696f6981cf","75366f52b70d40eba929e6c786383b22","4cf11d4aca8946d3b5d23ce6d2271f2d","5db72408b34e45cbbd6614266ba5fd61"],"daCatalogId":"","das":[{"text":"全国","value":"000000000000"}],"showType":"1","dts":"","rootId":"884c062607104a91967b22742537f44f"},
           {"cid":"47e188eb48a840e4b7ee00c1d30a4792","indicatorIds":["aae3499756ee4863a472d1bbf191b471","080e88d265484584b42fd15b3969832f","c245fec3e745429996222fa5591a958e","a1821ad1c8334e578f9337504140a583","d74ee3c2a03e47b0872ad3f36e1da7db","4b29c65da5ae4a3094cc1a9a66ba38ae","a0aa1d4d85154fa491ab4c4cf8d3fba3","ec4411ecd02e4439b868280c65cdca6b","5d35c0bf8ffb4d7c9a6ddb89bb764989","8cd8794b4ac14b94a978d6a9f3392283","06a25105929d4d5091e4e9608639f0b9","de01b263f2254ada9afa874b98430952","c77ae767d8fb4b4cac6a36e6f704d519","67b818d8b97641c39009e4e5b428e20b","4e022e23f8ea49f2a72ce62090fb48a8","6a78e55856774a8f8de2c53b63d1a6f1","f68fa08db6f449299e4ce7051ffee16e","8af01d9c42f143009aba21242bbf2559","0ab64c9619fe44b19691c4290945c3ea","6c63e3d7244b47ddbfe53d321a99cd16"],"daCatalogId":"","das":[{"text":"全国","value":"000000000000"}],"showType":"1","dts":"","rootId":"884c062607104a91967b22742537f44f"},
           {"cid":"6846b7d7de154c5295bf5598f6e32a5e","indicatorIds":["bc13d74f635748a3942e2348075cface","8736d6fcc12f47918fb9d6d7a70b8f9a","80fecb897ac047f99caa10dc51398c6a","d0489223c3a7427188e23f925ed6c5e1","a00cbc799a514fb48ef9d2d963d5de1f","a9a8ee5269d5439996443b415d49cf2b","65cf2a18747741f9b1e1584747dac98f","fdf6886617224c55a594785cb8fc6be3","0691e6586e4f4f5d9ef9b6e6982b76e6","517f8babd7cb4e308e299172f0ff4ea3","771c4acb9cb346568ea0bc948c31f0d3","c5d016b5de674fd2a6b501c2565b89e6","7e126cbbeada40108c20a4a2db054896","bc4a1e5c5fe84d929d7f6a4db0e9a93a","8c95d5e105ce4a62bbc1696bb339673b","e5dd9ab078ed4104a2b2d1895afa4d11","16dcff5cb4ea4227ac7b1968a418e8a1","13db6b36fc3d477280a7b2ef2df07b5e","50bd5cdf25e84097b46a506a3377ad2f","efc0969159c34c63b6e541c73bfb7fcd"],"daCatalogId":"","das":[{"text":"全国","value":"000000000000"}],"showType":"1","dts":"","rootId":"884c062607104a91967b22742537f44f"},
           {"cid":"f0c8e1468542491db2f76d56bca8e103","indicatorIds":["85450237dbad491093ce04e391916074","d147fe77b0724f658a3908ee3f30eee2","e172a8292164403688792b9de2a6fa65","a820a895cbd741e8bbe546263996376e","6aab8b691d34404d955aefe56d6f00cf","582a37c3524c49988ff7b8edc8023a23","890a43b178da43c18ae4e3453d939821","ad4120de560e465f8a328873aeb869fc","4c2c7f2cfbc242b6abdd6931004d7986","02cafdca0d614180b7171dfa9b97c114","7eadc5ee11774b6e944394918b3aeb08","3e2e8e9e0dc64aa2a842a4022f6a189d","bc8616e72d0a45028e6424a12dcd1317","ec45a514111e4837b48c7af9dea59b36","3e8b1f45cfdf42499d0e06993c2ebf7c","bcdd63e7bece4755b650eacbe43856c7","4777b96ecae047a780a151b679f3e90a","a7db9d16b71f45fa87def3e1f3974e0e","bd98641ef60c4bb0abfba02502cc9ec4","260c6d742f584d4cb759b476b9938808"],"daCatalogId":"","das":[{"text":"全国","value":"000000000000"}],"showType":"1","dts":"","rootId":"884c062607104a91967b22742537f44f"}
           ]
url="https://data.stats.gov.cn/dg/website/publicrelease/web/external/stream/esData"
box=[]#准备一个列表来装数据

for payload in all_payload:
    res = req.post(url,headers=headers,cookies=cookies,json=payload)
    all_data=res.json()#转成我看的懂的形式
    year_list=all_data.get('data',[])#我看到我想要的数据都在data里

    for yeardata in year_list:#做个循环，取出year_list中的name和values
        the_name=yeardata.get("name") or yeardata.get("_name")
        the_values=yeardata.get('values',[])
        for sth in the_values:#再做个循环，取出the_values中的values和i_showname
            part1=sth.get("value") 
            name=sth.get("i_showname") or sth.get("_i_showname")
            part2=name[0:len(name)-4]
            if '支出' in part2:
                part3='支出'
            else:
                part3='收入'
            part4=name[0:2]
            part0=name[len(name)-3:len(name)-4:-1]
            if part4=="居民":
                part4="全国"
            box.append({
                "年份":the_name,
                "范围":part4,
                "收支类型":part3,
                "指标":part2,
                "数值":part1,
                "单位":part0
            })#把数据装入


print(box)#打印一下，发现没问题
df=pd.DataFrame(box)#变成表格
df['数据来源']='国家统计局'
df.to_csv("all_data(已清洗).csv",index=False,encoding="utf-8-sig")
yl=pd.DataFrame(year_list)
yl.to_csv("all_data(原始数据).csv",index=False,encoding="utf-8-sig")
print("over!")
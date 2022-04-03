import requests

def downloadData():
    URL = 'https://trends.google.com.tw/trends/trendingsearches/daily/rss?geo=TW' 

    r = requests.get(URL)

    if r.status_code == 200:
        import xmltodict, json
        xml_string = xmltodict.parse(r.text)

        with open('./output/crawler_data.json', 'w', encoding='utf-8-sig') as f:
            json.dump(xml_string, f, ensure_ascii=False)

def readFile(name):
    import json
    with open(name, 'r', encoding='utf-8-sig') as f:
        json_string = json.load(f)
        return json_string

def listTitles(dictionary):
    for index, item in enumerate(dictionary['rss']['channel']['item']):
        print(index, ' : ', item["title"])

def listNews(dictionary):
    for index, item in enumerate(dictionary['rss']['channel']['item']):
        # print(index, ' : ', item['ht:news_item'][0].values())
        # print(type(item['ht:news_item']))
        if type(item['ht:news_item']) is list :
            print(item['ht:news_item'][0].values())
        elif type(item['ht:news_item']) is dict :
            print(item['ht:news_item'].values())

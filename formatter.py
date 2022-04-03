from hashlib import new


class Formatter:
    def __init__(self, filename):
        self.crawler_filename = filename
        self.crawler_json_string = self.readJsonFile(self.crawler_filename)
        self.crawler_data_list = self.crawlerDataFormatting(self.crawler_json_string)

    def readJsonFile(self, name):
        import json
        with open(name, 'r', encoding='utf-8-sig') as f:
            json_string = json.load(f)
            return json_string

    def crawlerDataFormatting(self, dictionary):
        data_list = []
        for item in dictionary['rss']['channel']['item']:
            if type(item['ht:news_item']) is list :
                tmp_news = [list(item['ht:news_item'][0].values()), list(item['ht:news_item'][1].values())]
            elif type(item['ht:news_item']) is dict :
                tmp_news = list(item['ht:news_item'].values())
            
            tmp_list = [item['title'], item['ht:approx_traffic'], item['pubDate'], tmp_news]
            
            data_list.append(tmp_list)

        return data_list

    def initCsvFile(self):
        import pandas as pd
        index_list = [num for num in range(0,len(self.crawler_data_list))]
        df = pd.DataFrame(self.crawler_data_list, columns =['title', 'traffic', 'data', 'news'], index=index_list)
        df.to_csv('./output/keywords.csv', index_label='index')

    def combineCsvFile(self):
        import pandas as pd
        previous_data = pd.read_csv('./output/keywords.csv', index_col='index')
        previous_length = len(previous_data)

        index_list = [num for num in range(previous_length, previous_length + len(self.crawler_data_list))]
        new_data = pd.DataFrame(self.crawler_data_list, columns =['title', 'traffic', 'data', 'news'], index=index_list)
        
        combine_frames = [previous_data, new_data]
        result = pd.concat(combine_frames)
        result.drop_duplicates(ignore_index=True)

        result.to_csv('./output/keywords.csv', index_label='index')

if __name__ == '__main__':
    import crawler
    crawler.downloadData()
    
    # import viewer
    # data = viewer.readFile('./newdata.json')
    # viewer.listNews(data)

    import formatter
    formatter = formatter.Formatter('./output/crawler_data.json')
    # formatter.initCsvFile()
    formatter.combineCsvFile()

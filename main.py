if __name__ == '__main__':
    import crawler, sys
    import formatter
    
    crawler.downloadData()
    formatter = formatter.Formatter('./output/crawler_data.json')

    if str(sys.argv[1]) == 'archive':
        formatter.pushToArchive(str(sys.argv[2]))
        formatter.initCsvFile()
    else:
        formatter.combineCsvFile()


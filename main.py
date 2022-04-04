if __name__ == '__main__':
    import crawler, sys
    import formatter
    
    crawler.downloadData()
    formatter = formatter.Formatter('./output/crawler_data.json')

    if len(sys.argv) == 1:
        formatter.combineCsvFile()
    else:
        if str(sys.argv[1]) == 'archive':
            formatter.pushToArchive(str(sys.argv[2]))
            formatter.initCsvFile()
    

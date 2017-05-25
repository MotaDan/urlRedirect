from urllib import request
import csv

def undirect(urlsFile):
    """Passed in a csv file of urls, it returns a list of what they rediect to."""
    with open(urlsFile, 'r', newline='') as urls:
        fileReader = csv.reader(urls)
        
        for url in fileReader:
            req = request.Request(url[0], headers={'User-Agent' : "Magic Browser"})
            yield (url[0], request.urlopen(req).geturl())
    
    
if __name__ == "__main__":
    file_name = "./dirtyUrls.csv"
    pureurls = undirect(file_name)
    
    with open('cleanUrls.csv', 'w', newline='') as f:
        fileWriter = csv.writer(f)
        fileWriter.writerows(pureurls)
        
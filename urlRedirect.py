from urllib import request, error
import csv
import sys
import random
from time import sleep
import requests

user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"]

def undirect(urlsFile):
    """Passed in a csv file of urls, it returns a list of what they rediect to."""
    with open(urlsFile, 'r', newline='') as urls:
        fileReader = csv.reader(urls)
        
        for url in fileReader:
            try:
                opener = request.build_opener(request.HTTPCookieProcessor)
                opener.addheaders = [('User-Agent', random.choice(user_agents))]
                request.install_opener(opener)
                
                print(".", end='')
                yield (url[0], url[1], request.urlopen(url[1]).geturl())
                sleep(random.random())
            except Exception as e: #(error.HTTPError, error.URLError, ValueError) as e:
                print(e)
                print("{0} {1}\n".format(url[0], url[1]))
                yield (url[0], url[1])
    
    
def undirect_w_requests(urlsFile):
    """Passed in a csv file of urls, it returns a list of what they rediect to. Uses requests instead of urllib."""
    with open(urlsFile, 'r', newline='') as urls:
        fileReader = csv.reader(urls)
        
        for url in fileReader:
            try:
                print(".", end='')
                yield (url[0], url[1], requests.get(url[1]).url)
                sleep(random.random())
            except Exception as e: #(error.HTTPError, error.URLError, ValueError) as e:
                print(e)
                print("{0} {1}\n".format(url[0], url[1]))
                yield (url[0], url[1])
    
    
def main():
    file_name = "./dirtyUrls.csv"
    pureurls = undirect(file_name)
    
    with open('cleanUrls.csv', 'w', newline='') as f:
        fileWriter = csv.writer(f)
        for row in pureurls:
            fileWriter.writerow(row)
    
    
if __name__ == "__main__":
    main()
        

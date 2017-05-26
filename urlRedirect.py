from urllib import request, error
import csv
import sys

def undirect(urlsFile):
    """Passed in a csv file of urls, it returns a list of what they rediect to."""
    with open(urlsFile, 'r', newline='') as urls:
        fileReader = csv.reader(urls)
        
        for url in fileReader:
            try:
                opener = request.build_opener(request.HTTPCookieProcessor)
                opener.addheaders = [('User-Agent', "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0")]
                yield (url[0], url[1], opener.open(url[1]).geturl())
            except error.HTTPError as e:
                print(e)
                if "linkedin" in e.headers.get("Set-Cookie"):
                    print("LinkedIn")
                print("{0} {1}\n".format(url[0], url[1]))
                yield (url[0], url[1])
            except ValueError as e:
                print(e)
                print("{0} {1}\n".format(url[0], url[1]))
                yield (url[0], url[1])
    
    
if __name__ == "__main__":
    file_name = "./dirtyUrls.csv"
    pureurls = undirect(file_name)
    
    with open('cleanUrls.csv', 'w', newline='') as f:
        fileWriter = csv.writer(f)
        fileWriter.writerows(pureurls)
        
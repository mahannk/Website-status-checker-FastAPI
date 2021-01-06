import requests
import time
import concurrent.futures
import sys, getopt, os


TIME_OUT = 5

class checking_url:
    
    @staticmethod
    def checker(url):

        status_code = int
        redirected_URL = str

        try:
            r = requests.get(url, timeout = TIME_OUT) # request 
            if len(r.history) > 0: # url is redirected
                status_code = r.history.pop().status_code
                redirected_URL = r.url
            
            else:
                status_code = r.status_code
                redirected_URL = None
            
        except Exception as e:
            print(e)
            status_code = None
            redirected_URL = None
            
        return {'URL' : url, 'Status Code' : status_code, 'Redirected URL' : redirected_URL}

    @staticmethod
    def run(urls):

        t1 = time.perf_counter()
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            rs = executor.map(checking_url.checker, urls)
            
            results = [r for r in rs]
        
        
        t2 = time.perf_counter()
        print(f'Finished in {round(t2-t1)} seconds')   

        return results
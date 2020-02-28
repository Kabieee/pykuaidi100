import requests,random

class Query:
    def __init__(self,url,ex_type,ex_code):
        self.url = url
        self.ex_type = ex_type
        self.ex_code = ex_code
        self.cookies = requests.cookies.RequestsCookieJar()

    
    def get_cookie(self):
        _request = requests.Session()
        response = _request.get(self.url)
        self.cookies.update(response.cookies.get_dict())
        # print(self.cookies.get_dict())
    
    def query_express(self):
        # print(random.random())
        # exit()
        self.get_cookie()
        queryUrl = self.url+'/query'
        queryParams = {
            'type':self.ex_type,
            'postid':self.ex_code,
            'temp':random.random(),
            'phone':'' #留空

        }
        queryHeader = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
            'Referer': 'https://www.kuaidi100.com/?from=openv',
            'Host':'www.kuaidi100.com',
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = requests.get(queryUrl,headers=queryHeader,params=queryParams,cookies=self.cookies)
        # print(response.request.url)
        return response.text

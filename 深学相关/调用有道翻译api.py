#/usr/bin/env python
#coding=utf8
import urllib.parse
import http.client
import random
import hashlib
 
appKey = '78badb097b683b63'
secretKey = 'Wodv82XTOsy1rSTCWw4odBJYn0wpGvko'
 
def youdaoTranslate(q):
    httpClient = None
    myurl = '/api'
    fromLang = 'zh-CHS'
    toLang = 'EN'
    salt = random.randint(1, 65536)
    sign = appKey+q+str(salt)+secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    myurl = myurl+'?appKey='+appKey+'&q='+ urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        s = eval(response.read().decode("utf-8"))['translation']
        print(s)
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return s
 
if __name__ == '__main__':
    ss = youdaoTranslate('你好')
    print(ss)

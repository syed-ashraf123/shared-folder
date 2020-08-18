from bs4 import BeautifulSoup
import requests
import json
headers={
    'accept':'*/*',
    'method': 'GET',
    'path': '/ajax/nav/UserNavAsync.htm?pageframe=true',

    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-IN,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cookie': 'zguid=23|%247477d58d-26b4-48a4-874b-e4830bb00dee; _ga=GA1.2.1461655041.1593612751; zjs_user_id=null; zjs_anonymous_id=%227477d58d-26b4-48a4-874b-e4830bb00dee%22; _pxvid=e89dfed6-bba4-11ea-8b26-0242ac120009; _gcl_au=1.1.556517947.1593612752; _fbp=fb.1.1593612753197.31498831; _pin_unauth=dWlkPU9HVTFOVEEwT0RZdFl6RmpPQzAwTkdVMExXSmhNelF0WldZNFl6Rm1ObVEzTkdZMQ; G_ENABLED_IDPS=google; __gads=ID=9be2d6409f2ebf8b:T=1593616228:S=ALNI_MZIRCGndniilaken3iSWJNYe9H03g; ki_r=; ki_s=; ki_t=1593698015413%3B1593698015413%3B1593699560167%3B1%3B5; g_state={"i_p":1593842680487,"i_l":2}; zgsession=1|703dd965-b0af-48a4-b13f-ca15ab78468b; KruxPixel=true; DoubleClickSession=true; KruxAddition=true; _gid=GA1.2.664843069.1594030833; JSESSIONID=4897CD0C285049B023F8D4B9CCEB5E9E; GASession=true; _px3=f4134e9f51f364a544fd33e1c7bcf8319d4e1540db55d9fa5637aa19fb621590:kHDGu7NxblyQagsUeFyO8Sh9uow4Z7eA8PkL2JRzDasGO5q68kBlMEkGVs2UQ0JbklOj4N+uOxBZIh/Q8vSdLA==:1000:et0cqEPBqfv7n0FKxMrMRIVPO6DU5Fad8UgJ2f4rt8ZcVJa5DcQaBB+O6/KkRxiAgNyUjHHOnfIjh4EFa59JGCyl5gqytxawIE2GcIABcu3Q4tWWw3RTNNNEGFs8DyekL8UGuvEpOghMWWYPX5ebKldYheVi6/vgDlzn6mEiBrM=; _uetsid=d09a8cd5-2efa-ed86-ac0f-6e2e478fa11e; _uetvid=3603e5e3-1738-d84e-40b0-e7edb37453f4; _gat=1; AWSALB=MACKgbLQ4Xq5FoidFWOCBSYVe+thyj3rcW4SefyxG9zWSkDhOBnT3yRGVdUCHjGjLI6yyc9SHiNwRzvJCGQQ0TH1fQOAbi6rMRGUX6i8m5d3SkH6xeCh8OV2fqk5; AWSALBCORS=MACKgbLQ4Xq5FoidFWOCBSYVe+thyj3rcW4SefyxG9zWSkDhOBnT3yRGVdUCHjGjLI6yyc9SHiNwRzvJCGQQ0TH1fQOAbi6rMRGUX6i8m5d3SkH6xeCh8OV2fqk5; search=6|1596622908014%7Crect%3D38.96992552152501%252C-76.80287268359373%252C38.82831390105304%252C-77.22584631640623%26rid%3D41568%26disp%3Dmap%26mdm%3Dauto%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0941568%09%09%09%09%09%09',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
url="https://www.zillow.com/homes/"


address="9831 Sepulveda Blvd UNIT 30, Los Angeles, CA 91343"
address=url+address.replace(", ",".dash.").replace(" ",".dash.").replace("/",".dash.").replace("#",".num.").replace("-",".dash.")+'_rb'
res=requests.get(address,headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
const=soup.select("[type='application/json']")
firstValue = str(const[3]).index("{")
lastValue = len(str(const[3])) - str(const[3])[::-1].index("}")
jsonString = str(const[3])[firstValue:lastValue]
jsonString=json.loads(jsonString)
#for i in jsonString:
#    print(i)
#print(jsonString['apiCache'])
for i in json.loads(jsonString['apiCache']):
    print(json.loads(jsonString['apiCache'])[i])
    print("")










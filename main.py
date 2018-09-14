from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/1311-1","my_appId","my_appSecret" )
r.addBodyPara("long", "http://www.baidu.com")
res = r.post()

f = open("test.txt",'a')
f.write(res.text) 
print(res.text) # 返回信息

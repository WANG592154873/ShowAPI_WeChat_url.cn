# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from ShowapiRequest import ShowapiRequest
x = input("请输入需要缩短的网址：（例如：www.baidu.com）\n")
num = int(input("请输入要生成的数量：\n"))
import time
def sleep(mytime=""):
        time.sleep(mytime)
while num > 0:
    f = open("test.txt", 'a')
    r = ShowapiRequest("http://route.showapi.com/1311-1","72683","028b760013994ee9ab2cc01601603fbb" )
    r.addBodyPara("long", x)
    res = r.post()
    #print(res.text) # 返回信息
    f.write(res.text)
    f.write("\r\n")
    print(res.text)
    sleep(2)
    num = num - 1
print("调用完成，请按任意键退出！")
end1 = input()

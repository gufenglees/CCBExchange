# -*- coding: UTF-8 -*-
# Written by xizhi

import os
import platform
import re
import requests
import linecache
import time
import datetime
import random
try:
  import qrcode
  qrcode.make("testerror")
  qrcodemodule = True
except ImportError:
  qrcodemodule = False
  print("\nqrcode模块或其依赖模块没有安装好,将无法转换为二维码"\
        "\n稍后请自行将支付链接转为二维码或复制链接到浏览器打开")
  time.sleep(3)

def CCBExchangeExit1():
  print("程序5秒后自动退出")
  linecache.clearcache()
  time.sleep(5)
  os._exit(0)

def CCBExchangeClear1():
  OS = platform.system()
  if re.findall(r"Windows",OS,flags=re.I) != []:
    os.system("cls")
  else:
    os.system("clear")

def CCBEcHeaders1():
  ccbeccookies1 = linecache.getline(r"ccbec1cfg.set",18).strip()
  ccbecheaders1 = {"Host":"ccbtreasure.mobi88.cn",
                  "user-agent":"Mozilla/5.0 (Linux; Android 10; GM1910 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36",
                  "x-requested-with":"XMLHttpRequest",
                  "cookie":"%s"%(ccbeccookies1)
                  }
  return ccbecheaders1

def CCBEcSign1(ccbecheaders1):
  ccbecsigns1 = requests.get("https://ccbtreasure.mobi88.cn/index.php/sign/sign.html",
                            headers=ccbecheaders1,timeout=3)
  if re.findall(r"error_404",str(ccbecsigns1.text),flags=re.I) != []:
    print("\n建行CCB登录状态失效了,请重新获取Cookie")
    CCBExchangeExit1()
  else:
    print("\n签到信息: "+ccbecsigns1.json()["msg"],end=" ")
    if re.findall(r"growth_value",str(ccbecsigns1),flags=re.I) != []:
      print("本次签到成长值: "+ccbecsigns1.json()["data"]["growth_value"])

def CCBEcGameTurn1(ccbecheaders1):
  ccbecgremarkj1 = requests.get("https://ccbtreasure.mobi88.cn/index.php/game/get_times.html",
                              headers=ccbecheaders1,timeout=3).json()
  ccbecgtimes1 = 2-int(ccbecgremarkj1["data"]["count"])
  ccbecgremark1 = ccbecgremarkj1["data"]["game_remark"]
  print("\n当前剩余免费游戏次数: "+str(ccbecgtimes1))
  if ccbecgtimes1 > 0:
    ccbecgscores1 = ["给你个眼神,自己体会下","好好反省一下为啥这么差","你真是个好人,幸运女神都不站在你那边",
                     "这确定不是作弊才有的吗","此刻心情无法言语,只能666了","看来你是彦祖或者亦菲的身份已经藏不住了"
                     ]
    print("\n即将自动开始游戏...")
    for i in range(ccbecgtimes1):
      ccbecgrscore1 = random.randint(1200,2000)
      if ccbecgrscore1 < 1600:
        print("\n游戏分数: %s\n%s"%(ccbecgrscore1,ccbecgscores1[random.randint(0,2)]))
      else:
        print("\n游戏分数: %s\n%s"%(ccbecgrscore1,ccbecgscores1[random.randint(3,5)]))
      ccbecheaders1["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
      ccbecgscorej1 = requests.post("https://ccbtreasure.mobi88.cn/index.php/game/game_record_score.html",
                                 headers=ccbecheaders1,data="game_score=%s&game_remark=%s"%(ccbecgrscore1,ccbecgremark1),
                                 timeout=3).json()
      print("\n返回信息: "+ccbecgscorej1["msg"])
      if re.findall(r"您有一次抽奖机会未使用",ccbecgscorej1["msg"]) != []:
        print("\n发现有未抽奖机会,将自动抽奖后继续游戏")
        ccbecgturnj1 = requests.get("https://ccbtreasure.mobi88.cn/index.php/game/turn.html",
                             headers=ccbecheaders1,timeout=3).json()
        print(ccbecgturnj1)
        print("\n返回信息: "+ccbecgturnj1["msg"],end=" ")
        print("抽奖结果: %s"%(ccbecgturnj1["data"]["title"]))
        CCBEcGameTurn1(ccbecheaders1)
      else:
        print("\n正在抽奖...")
        ccbecgturnj1 = requests.get("https://ccbtreasure.mobi88.cn/index.php/game/turn.html",
                             headers=ccbecheaders1,timeout=3).json()
        print(ccbecgturnj1)
        print("\n返回信息: "+ccbecgturnj1["msg"],end=" ")
        print("抽奖结果: %s"%(ccbecgturnj1["data"]["title"]))
      time.sleep(random.randint(5,10))

def CCBEcGift1(ccbecheaders1):
  ccbecgiftp1 = requests.get("https://ccbtreasure.mobi88.cn/index.php/gift/index.html",
                             headers=ccbecheaders1,timeout=3).text
  ccbecxxs1 = "".join(re.findall(r'<div class="xinxinshu">(.*)</div>',ccbecgiftp1,flags=re.I))
  ccbecgiftl1 = re.findall(r"<span>(.*)</span>",ccbecgiftp1,flags=re.I)
  ccbecgiftl1 = ccbecgiftl1[0:len(ccbecgiftl1):2]
  ccbecgiftpril1 = re.findall(r"\d+\.?\d?",str(ccbecgiftl1))
  ccbecgiftidl1 = re.findall(r"/index.php/gift/detail/id/(.*).html",ccbecgiftp1,flags=re.I)
  ccbecgiftl11 = []
  for i,gift in enumerate(ccbecgiftl1,1):
    ccbecgiftl11.append(str(i)+"   "+gift)
  print("\n可抵扣星星数: %s\n获取礼品成功\n\n%s"%(ccbecxxs1,"\n".join(ccbecgiftl11)))
  ccbecgifts1 = input("\n请输入数字选择商品: ")
  if ccbecgifts1 == "" or ccbecgifts1 == "0":
    ccbecgifts1 = 1
    print("\n数字少于1,默认选择第一个: %s"%(ccbecgiftl1[0]))
  try:
    ccbecgiftpri1 = int(float(ccbecgiftpril1[int(ccbecgifts1)-1])*100+10)
    print("选择的礼品原价格为(分): %s"%(ccbecgiftpri1))
    ccbecxxsn1 = input("\n请输入要抵扣的星星数量(最小为1): ")
    if ccbecxxsn1 == "" or ccbecxxsn1 == "0":
      ccbecxxsn1 == 1
    elif int(ccbecxxsn1) > int(ccbecxxs1):
      print("请输入少于可抵扣星星数量的数字,1秒后重新选择")
      time.sleep(1)
      CCBExchangeClear1()
      return CCBEcGift1(ccbecheaders1)
    ccbecgiftpri1 = ccbecgiftpri1-int(ccbecxxsn1)*500
    if int(ccbecgiftpri1) < 10:
      print("抵扣星星数量超额啦!1秒后重新选择")
      time.sleep(1)
      CCBExchangeClear1()
      return CCBEcGift1(ccbecheaders1)
    else:
      print("星星抵扣后的价格为(分): %s"%(ccbecgiftpri1))
      ccbecgift1 = ccbecgiftl1[int(ccbecgifts1)-1]
      ccbecgiftid1 = ccbecgiftidl1[int(ccbecgifts1)-1]
      print("\n已选择礼品名称: %s\n对应实付价格(分): %s\n对应礼品ID: %s"%(ccbecgift1,ccbecgiftpri1,ccbecgiftid1))
      return ccbecgift1,ccbecxxsn1,ccbecgiftpri1,ccbecgiftid1
  except IndexError:
    print("请输入仅列出的数字,1秒后重新输入")
    time.sleep(1)
    CCBExchangeClear1()
    return CCBEcGift1(ccbecheaders1)

def GetTimeis1():
  try:
    timeisp1 = requests.get("https://time.is/t/?zh.0.0.0.0p.0.0.0.",timeout=3)
    timeists1 = "".join(re.findall(r"\d{13}",timeisp1.text))
    timeist1 = datetime.datetime.fromtimestamp(int(timeists1)/1000).strftime("%H:%M:%S.%f")[:-3]
    return timeist1
  except (requests.exceptions.Timeout,requests.exceptions.ConnectionError):
    return GetTimeis1()

def CCBEcGetOrderj1(ccbecheaders1,ccbecxxsn1,ccbecgiftpri1,ccbecgiftid1):
  try:
    ccbecheaders1["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    ccbecgorderj1 = requests.post("https://ccbtreasure.mobi88.cn/index.php/gift/ops_order.html",
                                headers=ccbecheaders1,
                                data="g_id=%s&butterfly_num=%s&pay_money=%s"%(ccbecgiftid1,ccbecxxsn1,ccbecgiftpri1),
                                timeout=int(linecache.getline(r"ccbec1cfg.set",10).strip())).json()
    return ccbecgorderj1
  except (requests.exceptions.Timeout,requests.exceptions.ConnectionError,ValueError):
    return CCBEcGetOrderj1(ccbecheaders1,ccbecxxsn1,ccbecgiftpri1,ccbecgiftid1)

def CCBEcOrderPay1(ccbecheaders1,ccbecorderno1):
  ccbecpayinfoj1 = requests.get("https://ccbtreasure.mobi88.cn/index.php/gift/go_buy.html?order_no=%s"%(ccbecorderno1),
                               headers=ccbecheaders1,timeout=3).text
  ccbecpayinfo1 = "".join(re.findall(r'payInfo=\\"(.*)\\"',str(ccbecpayinfoj1),flags=re.I))
  ccbecorderpay1 = "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_05_MB?"+ccbecpayinfo1
  return ccbecorderpay1
  
def CCBEcQRcode1(ccbecorderpay1):
  ccbecqrcode1 = qrcode.make(ccbecorderpay1)
  ccbecqrcode1.show()
  ccbecqrcode1.save("ccbecorderpay1.png")
  print("\n支付链接二维码图片已保存在该目录下,打开建行APP扫码即可"\
        "\n支付前请务必对照好订单号\n等待30秒后自动退出")
  time.sleep(30)
  CCBExchangeExit1()
  
def CCBEcMain1():
  ccbecheaders1 = CCBEcHeaders1()
  CCBEcSign1(ccbecheaders1)
  print("\n签到已完成")
  print("\n是否需要自动完成免费2次游戏和抽奖,将会一次性完成所有游戏和抽奖次数,抽奖没有放水的时候建议 否 哦")
  ccbecgturn = input("是 就输入 y 后按确认,否 就直接按确定继续:")
  if ccbecgturn.lower() == "y":
    CCBEcGameTurn1(ccbecheaders1)
    print("\n免费游戏和抽奖已完成,即将获取礼品页...")
  else:
    print("\n即将获取礼品页...")
  ccbecgift1,ccbecxxsn1,ccbecgiftpri1,ccbecgiftid1 = CCBEcGift1(ccbecheaders1)
  print("\n现在有5秒确认所有信息是否正确,如有错误,请马上关闭软件然后重新运行"\
        "\n温馨提示: 就算已经创建订单了,只要没付款,星星数都是没有减少的")
  for i in range(5,0,-1):
    print("倒数 %s 秒"%(i),end="\r")
    time.sleep(1)
  if int(linecache.getline(r"ccbec1cfg.set",5).strip()) == 1:
    ccbecbuytime1 = "09:59:57.000"
    ccbecwaittime1 = (datetime.datetime.strptime(ccbecbuytime1,"%H:%M:%S.%f")+\
                      datetime.timedelta(minutes=-60)).strftime("%H:%M:%S.%f")[:-3]
    ccbecbuytime11 = (datetime.datetime.strptime(ccbecbuytime1,"%H:%M:%S.%f")+\
                      datetime.timedelta(minutes=-1)).strftime("%H:%M:%S.%f")[:-3]
    timeist1 = GetTimeis1()
    if timeist1 >= ccbecwaittime1 and timeist1 < ccbecbuytime1:
      print("\n请勿关闭,程序将在 %s 开抢"%(ccbecbuytime1))
      while timeist1 >= ccbecwaittime1 and timeist1 < ccbecbuytime1:
        if timeist1 < ccbecbuytime11:
          print("当前时间 %s 并以每30秒间隔刷新"%(timeist1),end="\r")
          time.sleep(30)
        else:
          print("当前时间 %s 并以每0.1秒间隔刷新"%(timeist1),end="\r")
          time.sleep(0.1)
        timeist1 = GetTimeis1()
  ccbecftime1 = linecache.getline(r"ccbec1cfg.set",7).strip()
  ccbecftimes1 = 1
  ccbecgorderj1 = CCBEcGetOrderj1(ccbecheaders1,ccbecxxsn1,ccbecgiftpri1,ccbecgiftid1)
  print("\n返回信息: %s"%(ccbecgorderj1["msg"]))
  while re.findall(r"创建订单成功",ccbecgorderj1["msg"]) == []:
    ccbecftimes1 += 1
    print("没有下单成功,将在%s秒后第%s次刷新"%(ccbecftime1,ccbecftimes1))
    time.sleep(float(ccbecftime1))
    CCBEcGetOrderj1(ccbecheaders1,ccbecxxsn1,ccbecgiftpri1,ccbecgiftid1)
    print("返回信息: "+ccbecgorderj1["msg"])
  print("\n%s 创建订单成功,正在获取订单号..."%(ccbecgift1))
  ccbecorderno1 = ccbecgorderj1["order_no"]
  print("\n订单号是: %s\n付款前请务必仔细对照好,避免误付款到别人的订单!\n正在生成支付链接..."%(ccbecorderno1))
  time.sleep(5)
  ccbecorderpay1 = CCBEcOrderPay1(ccbecheaders1,ccbecorderno1)
  with open("CCBExchange1的礼品 "+ccbecgift1+" "+\
      time.strftime("%H{}%M{}%S{}").format("时","分","秒")+"下单成功.ordered","w") as ordered:
    ordered.write(ccbecorderpay1)
  print("\n支付链接已生成在 .ordered 文件里并记录了下单时间,使用一般的打开文本类程序即可查看修改该文件"\
        "\n温馨提示: 未支付成功的请勿丢失支付链接,订单是无法找回的,支付链接丢失后未支付成功的将无法再次支付哦!"\
        "\n在支付页面长按 左上角-识别二维码 或 用手机扫二维码 都可以调用快捷支付哦")
  if int(linecache.getline(r"ccbec1cfg.set",13).strip()) == 1:
    times = time.strftime("%H{}%M{}%S{}").format("时","分","秒")   #加入时间,避免造成重复消息导致Server酱无法推送
    requests.get("https://sc.ftqq.com/%s.send?text=%s %s下单成功,请尽快支付,逾期将失效哦"\
                 %(linecache.getline(r"ccbec1cfg.set",15).strip(),times,ccbecgift1))
  if qrcodemodule:
    print("\n支付链接已生成,3秒后将自动转换为二维码")
    time.sleep(3)
    CCBEcQRcode1(ccbecorderpay1)
  else:
    CCBExchangeExit1()

if __name__ == "__main__":
  try:
    ccbeclines1 = len(open(r"ccbec1cfg.set",errors="ignore",encoding="UTF-8").readlines())
    if ccbeclines1 != 18:
      print("出错了, ccbec1cfg.set 的行数不对哦")
      CCBExchangeExit1()
  except FileNotFoundError:
    print("出错了,该目录下没有 ccbec1cfg.set 文件哦")
    CCBExchangeExit1()
  linecache.updatecache("ccbec1cfg.set")
  CCBEcMain1()
  

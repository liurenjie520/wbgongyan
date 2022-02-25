# -*- coding:utf-8 -*-
#场时间：\d+月\d\d日+\d{2,}
#xianqudiao \d+月\d\d日+\d{2,}点59分
#\d+月\d\d日+\d{2,}：+\d\d goumsishijisn
from datetime import datetime
#gytime \d+月\d\d日+\d{2,}点

#soumai \d+月\d\d日+\d{2,}点场于(.+?)售卖

import re


def timejx(ddd):
    ddd=ddd
    strr=ddd
    # strr = "#恋爱禁止条例#公演将于2月26日（周六）19：00，本场公演为@沈莹-AKB48TeamSH生日公演；#缩略图#研修生公演将于2月26日（周六）/2月27日（周日）14：00举办；2月27日（周日）19:00举办《春日缩略图特别公演》。#缩略图#研修生公演门票将采取官方商城售卖的方式。#恋爱禁止条例#公演和《春日缩略图特别公演》门票将采取VIP门票申请实名制抽选，普通门票和站票在官方商城售卖的方式。恋爱禁止条例公演：公演场地：万代南梦宫梦想剧场时间：2月26日19点VIP门票申请🔗：网页链接VIP门票申请时间：截至2月18日20点59分普通门票&amp;站票售卖时间：2月21日18：48开始售卖春日缩略图特别公演：公演场地：万代南梦宫梦想剧场时间：2月27日19点VIP门票申请🔗：网页链接VIP门票申请时间：截至2月18日20点59分普通门票&amp;站票售卖时间：2月22日18：48开始售卖缩略图研修生公演：公演场地：万代南梦宫梦想剧场时间：2月26日14点和2月27日14点门票购买时间：2月26日14点场于2月21日17：48开始售卖2月27日14点场于2月22日17：48开始售卖"
    # qudiaostr=str.replace("\d+月\d\d日+\d{2,}点59分", "qudiao");
    qudiaostr = re.sub(r'\d+月\d\d日+\d{2,}点59分', '', strr)
    qudiaostr2 = re.sub(r'\d+月\d\d日+\d{2,}点场于(.+?)售卖', '', qudiaostr)
    y = datetime.now().year
    y = str(y)
    # print(qudiaostr)

    result1 = re.findall(r"\d+月\d\d日+\d{2,}点", qudiaostr2)

    # qudiaostrbt=re.findall(r"#(.+?)#", str)
    # qudiaostrbt=list(set(qudiaostrbt))
    print(result1)
    # print(qudiaostrbt)

    result2 = re.findall(r"\d+月\d\d日+\d{2,}：+\d\d", qudiaostr)
    print(result2)

    gg=[]
    opt = ''
    for i in result2:
        t = datetime.strptime(y + i, "%Y%m月%d日%H：%M")
        h=t.strftime('%H')
        h=int(h)
        h=h-8
        txshi = "{0:02d}".format(h)
        txshi = str(txshi)
        # ms = t.strftime('%M%S')
        min=t.strftime('%M')
        min = int(min)
        min = min - 5
        txmin = "{0:02d}".format(min)
        txmin = str(txmin)
        s = t.strftime('%S')
        s = str(s)
        hms=txshi+txmin+s
        ymd = t.strftime('%Y%m%d')


        st = (f'{ymd}', f'{hms}')
        st = str(st) + ','
        opt = opt + st
        lsat = '[' + opt + ']'
        lsat = lsat.replace('),]', ')]')


    return lsat



def sdf(ddd):
    ddd=ddd
    s=timejx(ddd)
    dicee = eval(s)
    return dicee
    # print(dicee)


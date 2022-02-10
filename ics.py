
import datetime


import gyfwb
import shuijishu

def sd(urlid):
    urlid = urlid
    now_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    bd = now_time.strftime('%Y%m%d')
    # tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y%m%d")
    with open(file="wbakb48tsh.ics", encoding="utf8", mode="w") as file_object:
        start_string = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:" \
                       + "微博发布公演日程" + "\nX-WR-TIMEZONE:Asia/Shanghai\n" \
                       + "X-WR-CALDESC:"+bd+"发布了微博公演\n"
        file_object.write(start_string)
        body = gyfwb.lastfanhui(urlid)
        body_string = ("BEGIN:VEVENT\nDTSTAMP:20190912T184136Z\nUID:",
                       "END:VEVENT\n")


        if body==None:
            print('今天没有发布公演。')
        else:
            for item in body:
                body0 = body_string[0]
                body1 = item[0] + 'almanac_in_' + shuijishu.suiji() + "\n"
                body2 = "DTSTART;VALUE=DATE:" + item[0] + "\nDTEND;VALUE=DATE:" + item[1] + "\n"
                beizhu = "DESCRIPTION:" +  item[2]+ "微博详情链接："+item[3]+"\n"
                body3 = "SUMMARY:" + "近期公演动态" + "\n"
                tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + item[0] + "T013000Z" + "\n"
                tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
                body4 = body_string[1]
                full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
                file_object.write(full_body)
            end_string = "END:VCALENDAR"
            file_object.write(end_string)
    return '函数执行ok'

def isgytrue(urlid):
    urlid = urlid
    body = gyfwb.lastfanhui(urlid)
    for item in body:
        zifu=item[2]
        if zifu=='没有发布公演':
            print('没有发布公演')
        else:
            print('有公演动态！正在生成ics')
            sd(urlid)





# if __name__ == '__main__':
#     strr='4677399825875715'
#     a=isgytrue(strr)
#     print(a)
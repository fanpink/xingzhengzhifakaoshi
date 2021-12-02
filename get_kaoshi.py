# coding=utf-8
import json
import time

import requests


def panduan_get(typeing):
    panduan_get = requests.get("http://139.155.25.53:9191/getRandomList?questionType=%E5%88%A4%E6%96%AD%E9%A2%98&subjectType="+typeing)
    # print(panduan_get.encoding)
    panduan_get.encoding = 'utf-8'
    json_re = panduan_get.text      #抓取网页数据
    json_data = json.loads(json_re)     #加载json
    datalist = json_data["data"]    #提取数据
    dalistlen =len( datalist )  #数据 行数
    f_panduan_data=open('data/panduan_data.txt','a+')
    f_panduan_id=open('id/panduan_id.txt','r+')
    readid = f_panduan_id.readlines()
    readid_list = list(readid)
    # print(len(readid))
    # print(type(readid_list))
    id_new = ""
    for j in range( 0, dalistlen):
        datalist_data = datalist[j]
        id = datalist_data["id"]
        # print(type(id))
        idstr = str(id)+"\n"
        # print(readid_list)
        if idstr not in readid_list:
            id_new = id_new + str(id)+"\n"  # "correctOption": "B",
            timu = str(id)+"\t" + datalist_data["subject"]+"\t正确答案："+ datalist_data["correctOption"]+"\t"+datalist_data["optionA"]+"\t"+datalist_data["optionB"]+"\n"
            f_panduan_data.write(timu)
            print(str(id)+"\t")
            print("id不cun在")
    f_panduan_id.write(id_new)
def danxuan_get(typeing):
    danxuan_get = requests.get("http://139.155.25.53:9191/getRandomList?questionType=%E5%8D%95%E9%80%89%E9%A2%98&subjectType="+typeing)
    # print(panduan_get.encoding)
    danxuan_get.encoding = 'utf-8'
    json_re = danxuan_get.text      #抓取网页数据
    json_data = json.loads(json_re)     #加载json
    datalist = json_data["data"]    #提取数据
    dalistlen =len( datalist )  #数据 行数
    f_panduan_data=open('data/danxuan_data.txt','a+')
    f_panduan_id=open('id/danxuan_id.txt','r+')
    readid = f_panduan_id.readlines()
    readid_list = list(readid)
    # print(len(readid))
    # print(type(readid_list))
    id_new = ""
    for j in range( 0, dalistlen):
        datalist_data = datalist[j]
        id = datalist_data["id"]
        # print(type(id))
        idstr = str(id)+"\n"
        # print(readid_list)
        if idstr not in readid_list:
            id_new = id_new + str(id)+"\n"  # "correctOption": "B",correctOption
            timu = str(id)+"\t" + datalist_data["subject"]+"\t正确答案："+ datalist_data["correctOption"]+"\t"+datalist_data["optionA"]+"\t"+datalist_data["optionB"]+"\t"+datalist_data["optionC"]+"\t"+datalist_data["optionD"]+"\n"
            f_panduan_data.write(timu)
            print(str(id)+"\t")
            print("id不cun在")
    f_panduan_id.write(id_new)
def duoxuan_get(typeing):
    duoxuan_get = requests.get("http://139.155.25.53:9191/getRandomList?questionType=%E5%A4%9A%E9%80%89%E9%A2%98&subjectType="+typeing)
    # print(panduan_get.encoding)
    duoxuan_get.encoding = 'utf-8'
    json_re = duoxuan_get.text      #抓取网页数据
    json_data = json.loads(json_re)     #加载json
    datalist = json_data["data"]    #提取数据
    dalistlen =len( datalist )  #数据 行数
    f_panduan_data=open('data/duoxuan_data.txt','a+')
    f_panduan_id=open('id/duoxuan_id.txt','r+')
    readid = f_panduan_id.readlines()
    readid_list = list(readid)
    # print(len(readid))
    # print(type(readid_list))
    id_new = ""
    for j in range( 0, dalistlen):
        datalist_data = datalist[j]
        id = datalist_data["id"]
        # print(type(id))
        idstr = str(id)+"\n"
        # print(readid_list)
        if idstr not in readid_list:
            id_new = id_new + str(id)+"\n"  # "correctOption": "B",
            timu = str(id)+"\t" + datalist_data["subject"]+"\t正确答案："+ datalist_data["correctOption"]+"\t"+datalist_data["optionA"]+"\t"+datalist_data["optionB"]+"\t"+datalist_data["optionC"]+"\t"+datalist_data["optionD"]+"\n"
            f_panduan_data.write(timu)
            print(str(id)+"\t")
            print("id不cun在")
    f_panduan_id.write(id_new)
def anlifenxi_get(typeing):
    anlifenxi_get = requests.get("http://139.155.25.53:9191/getRandomList?questionType=%E6%A1%88%E4%BE%8B%E5%88%86%E6%9E%90%E9%A2%98&subjectType="+typeing)
    # print(panduan_get.encoding)
    anlifenxi_get.encoding = 'utf-8'
    json_re = anlifenxi_get.text      #抓取网页数据
    json_data = json.loads(json_re)     #加载json
    datalist = json_data["data"]    #提取数据
    # dalistlen =len( datalist )  #数据 行数
    f_panduan_data=open('data/anlifenxi_data.txt','a+')
    f_panduan_id=open('id/anlifenxi_id.txt','r+')
    readid = f_panduan_id.readlines()
    id1 = datalist["id"]
    id1str = str(id1)+"\n"
    id_new = ""
    timulit= ""
    if id1str not in readid:
        id_new = id_new + id1str
        print(id1str+"\tid不cun在")
        timu = str(id1) + "\t" + datalist["caseName"]+"\n"
        # print(timu)
        f_panduan_data.write(timu)
        anlifenxi_data = datalist["questionBankList"]
        # print(anlifenxi_data)
        dalistlen =len( anlifenxi_data )

        # print(dalistlen)
        for j in range( 0, dalistlen):
            datalist_data = anlifenxi_data[j]
            timulit = datalist_data["subject"]+"\n正确答案："+ datalist_data["correctOption"]+"\n"+datalist_data["optionA"]+"\n"+datalist_data["optionB"]+"\n"+datalist_data["optionC"]+"\n"+datalist_data["optionD"]+"\n"
            f_panduan_data.write(timulit)
    timulit = "\n"
    #print(timulit)
    f_panduan_data.write(timulit)
    f_panduan_id.write(id_new)


if __name__ == '__main__':
    # <option value="1">关于全面推行证明事项和涉企经营许可事项告知承诺制的指导意见</option>
    # <option value="2">习近平法治思想</option>
    # <option value="3">全面推行行政执法三项制度指导意见解读</option>
    # <option value="4">行政复议法</option>
    # <option value="5">行政强制法</option>
    # <option value="6">行政诉讼法</option>
    # <option value="7">国家赔偿法</option>
    # <option value="8">行政许可法</option>
    # <option value="9">立法法</option>
    # <option value="10">新行政处罚法</option>

    #typeing ="1"
    # 判断题
    # http://139.155.25.53:9191/getRandomList?questionType=%E5%88%A4%E6%96%AD%E9%A2%98&subjectType=1
#    panduan_get(typeing)
    # 单选题
    # http://139.155.25.53:9191/getRandomList?questionType=%E5%8D%95%E9%80%89%E9%A2%98&subjectType=1
#    danxuan_get(typeing)
    # 多选题
    # http://139.155.25.53:9191/getRandomList?questionType=%E5%A4%9A%E9%80%89%E9%A2%98&subjectType=1
#    duoxuan_get(typeing)
    # 案例分析题
    # http://139.155.25.53:9191/getRandomList?questionType=%E6%A1%88%E4%BE%8B%E5%88%86%E6%9E%90%E9%A2%98&subjectType=1
#    anlifenxi_get(typeing)


    for type in range( 1, 10):
        typeing = str(type)
        for n in range( 1, 200):
            panduan_get(typeing)
            time.sleep(5)
    for type in range( 1, 10):
        typeing = str(type)
        for n in range( 1, 200):
            danxuan_get(typeing)
            #time.sleep(5)

    for type in range( 1, 10):
        typeing = str(type)
        for n in range( 1, 200):
            duoxuan_get(typeing)
            #time.sleep(5)

    for type in range( 1, 10):
        typeing = str(type)
        for n in range( 1, 100):
            anlifenxi_get(typeing)
            # time.sleep(5)
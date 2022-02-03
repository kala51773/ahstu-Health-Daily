#!/usr/bin/python3
import configparser

import requests
import time
import  re
cf=configparser.ConfigParser()
cf.read('config.ini')

vec=cf.sections()
f=open('anhui_status.log','a')
try:
    for a in vec:
        
        name=cf.get(a,'name')
        # Cookie = cf.get(a,'Cookie')
        print(name)
        user_passwd=cf.get(a,'user_passwd')
        print(1)
        id=cf.get(a,'id')#学号
        
        Sex=cf.get(a,'Sex')
       
        IdCard=cf.get(a,'IdCard')
        MoveTel=cf.get(a,'MoveTel')
        
        ProvinceName=cf.get(a,'ProvinceName')
        CityName=cf.get(a,'CityName')
        CountyName=cf.get(a,'CountyName')
        FaProvinceName=cf.get(a,'FaProvinceName')
        FaCityName=cf.get(a,'FaCityName')
        FaCountyName=cf.get(a,'FaCountyName')
        ComeWhere=cf.get(a,'ComeWhere')
        #现在所在地

        FaProvince=cf.get(a,'FaProvince')
        FaCity=cf.get(a,'FaCity')
        FaCounty=cf.get(a,'FaCounty')
        FaComeWhere=cf.get(a,'FaComeWhere')
        #家庭所在地
        


        # Postman_Token=''#提交识别码
       
        # SpecialtyName=''#系别
        # ClassName=''#班级 格式为班级+班级号 例：汉语言文学213
        # SpecialtyName


        pom={
            'txtUid': id,
        'txtPwd': user_passwd
            }
       

        #构造header放入UA Cookies等信息此处通过抓包获取
        session=requests.session()
        r=session.post(url='http://xgb.ahstu.edu.cn/SPCP/Web',data=pom)
        print(r.text)
        print ('断点1')
        #先发送一个带有Cookies的get请求加载打卡填写界面以获取ReSubmiteFlag识别码
        r = session.get(url='http://xgb.ahstu.edu.cn/SPCP/Web/Report/Index')
        print ('断点2')
        try:
            obj=re.search('ReSubmiteFlag.*',r.text,re.M).group()
            obj2=re.search('"........-.*"',obj).group()
            obj_final=obj2.split('\"',3)[1]
        except  AttributeError:
            print(r.text)
            f.write(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
            f.write(name)
            try:
                if re.search('当前采集日期已登记！',r.text,re.M).group():
                    f.write('今日已经打卡\n')
                    print('今日已经打卡')
            except:
                if re.search('请根据学校提供的地址登录后再来访问！',r.text,re.M).group():
                    f.write('打卡失败 身份验证过期\n')
                    print('打卡失败 身份验证过期')


            continue


        
        url = "http://xgb.ahstu.edu.cn/SPCP/Web/Report/Index"
        data={
        'StudentId': id,
        'Name': name,
        'Sex': Sex,
        'SpeType': 'B',
        'CollegeNo': '309',
        'SpeGrade': '2021',
        'SpecialtyName': '汉语言文学',
        'ClassName': '汉语言文学213',
        'MoveTel': MoveTel,
        'Province': '340000',
        'City': '341100',
        'County': '341126',
        'ComeWhere': '安徽科技学院',
        'FaProvince': FaProvince,
        'FaCity': FaCity,
        'FaCounty': FaCounty,
        'FaComeWhere': FaComeWhere,
        'radio_1': '71a16876-3d52-4510-8c96-09b232a0161b',
        'radio_2': '083d90f5-5fa2-4a6d-a231-fe315b5104a3',
        'radio_3': '994c60eb-6f68-48bd-8bda-49a8a7ea812c',
        'radio_4': 'a99d5cba-f691-4372-9487-4988dba252f1',
        'radio_5': 'afcfb6e2-ec9f-457d-8b72-37d13e958ace',
        'radio_6': '6dd9b137-651c-4d18-9479-44854666f57e',
        'radio_7': '558acb85-cb5c-451a-af77-573c4df8856c',
        'radio_8': '3e991072-cb63-40d5-8aef-7fdc4bc02cda',
        'radio_9': '669acedd-9e94-48e7-abe9-e90c5bcf75d7',
        'radio_10':' e742629f-8cb7-4533-bf6e-7141befe77e1',
        'text_1': '',
        'Other': '',
        'GetAreaUrl': '/SPCP/Web/Report/GetArea',
        'IdCard': IdCard,
        'ProvinceName': ProvinceName,
        'CityName': CityName,
        'CountyName': CountyName,
        'FaProvinceName': FaProvinceName,
        'FaCityName': FaCityName,
        'FaCountyName': FaCountyName,
        'radioCount': '10',
        'checkboxCount': '0',
        'blackCount': '1',
        'PZData': '[{\"OptionName\":\"以上症状都没有\",\"SelectId\":\"71a16876-3d52-4510-8c96-09b232a0161b\",\"TitleId\":\"eb0c8db7-b4dd-4ad6-b58a-626fc3336f16\",\"OptionType\":\"0\"},{\"OptionName\":\"否，身体健康\",\"SelectId\":\"083d90f5-5fa2-4a6d-a231-fe315b5104a3\",\"TitleId\":\"a9a30b10-f88e-4776-ac74-b5a10fa11886\",\"OptionType\":\"0\"},{\"OptionName\":\"否，不是疑似感染者\",\"SelectId\":\"994c60eb-6f68-48bd-8bda-49a8a7ea812c\",\"TitleId\":\"37e33b7d-5575-48c3-b59b-d4b7f6a6a0b5\",\"OptionType\":\"0\"},{\"OptionName\":\"否\",\"SelectId\":\"a99d5cba-f691-4372-9487-4988dba252f1\",\"TitleId\":\"a411c056-62c8-40a7-bce5-5b34cccf0a1f\",\"OptionType\":\"0\"},{\"OptionName\":\"否\",\"SelectId\":\"afcfb6e2-ec9f-457d-8b72-37d13e958ace\",\"TitleId\":\"c7158ce4-96c6-445f-b47c-47729026183b\",\"OptionType\":\"0\"},{\"OptionName\":\"否\",\"SelectId\":\"6dd9b137-651c-4d18-9479-44854666f57e\",\"TitleId\":\"1f8d7172-5ab4-40bf-8345-50e84030e803\",\"OptionType\":\"0\"},{\"OptionName\":\"否\",\"SelectId\":\"558acb85-cb5c-451a-af77-573c4df8856c\",\"TitleId\":\"fde86af0-b7b7-4cce-be73-9f1e071bf7fc\",\"OptionType\":\"0\"},{\"OptionName\":\"未接触不用隔离\",\"SelectId\":\"3e991072-cb63-40d5-8aef-7fdc4bc02cda\",\"TitleId\":\"67f4f1c7-961e-423f-a102-18fd53722285\",\"OptionType\":\"0\"},{\"OptionName\":\"未接触不用隔离\",\"SelectId\":\"669acedd-9e94-48e7-abe9-e90c5bcf75d7\",\"TitleId\":\"3bc5e2d3-e3c1-4b27-a789-e2f8921798ef\",\"OptionType\":\"0\"},{\"OptionName\":\"否\",\"SelectId\":\"e742629f-8cb7-4533-bf6e-7141befe77e1\",\"TitleId\":\"031aa1ff-e97a-40bf-a8ee-f6808d99016f\",\"OptionType\":\"0\"}]',
        'ReSubmiteFlag':obj_final
        }

        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Proxy-Connection': "keep-alive",
            'Cache-Control': "max-age=0",
            'Upgrade-Insecure-Requests': "1",
            'Origin': "http://xgb.ahstu.edu.cn",
            'Content-Type': "application/x-www-form-urlencoded",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'Referer': "http://xgb.ahstu.edu.cn/SPCP/Web/Report/Index",
            'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            'cache-control': "no-cache",
            'Postman-Token': ''
            }
        response = session.request("POST", url, data=data, headers=headers)
        f.write(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
        f.write(name)
        f.write('日报打卡成功 \n')
        print('日报打卡成功 ')
except:
    f.write(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
    f.write(name)
    f.write(' 读取配置文件时出错\n')
    f.close()
f.close()

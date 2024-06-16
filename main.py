import machine
import oled128x64
import mixiot
import seniverse_api
import time


i2c_extend = machine.SoftI2C(scl = machine.Pin(22), sda = machine.Pin(21), freq = 100000)
oled = oled128x64.OLED(i2c_extend,address=0x3c,font_address=0x3A0000)
mixiot.wlan_connect('SSID','PASSWORD')
while True:
    i = str(seniverse_api.weather_now('API_PRIVATE_KEY','CITY'))
    t1 = i.find("'temperature': '")
    t2 = i.find("'}")
    m = i[(t1 + 16) : t2]
    h = '温度：' + m
    c1 = i.find("'code': '")
    c2 = i.find("', 'temperature':")
    code = i[(c1 + 9) : c2]
    q1 = i.find("text': '")
    q2 = i.find("', 'code'")
    tq = i[(q1 + 6) : (q2 + 1)]
    we = '天气：'
    we1 = '天气：'
    if 1:
        if code == '0':
            we = '晴'
        if code == '1':
            we = '晴'
        if code == '2':
            we = '晴'
        if code == '3':
            we = '晴'
        if code == '4':
            we = '多云'
        if code == '5':
            we = '晴间多云'
        if code == '6':
            we = '晴间多云'
        if code == '7':
            we = '大部多云'
        if code == '8':
            we = '大部多云'
        if code == '9':
            we = '阴'
        if code == '10':
            we = '阵雨'
        if code == '11':
            we = '雷阵雨'
        if code == '12':
            we = '雷阵雨伴冰雹'
        if code == '13':
            we = '小雨'
        if code == '14':
            we = '中雨'
        if code == '15':
            we = '大雨'
        if code == '16':
            we = '暴雨'
        if code == '17':
            we = '大暴雨'
        if code == '18':
            we = '特大暴雨'
        if code == '19':
            we = '冻雨'
        if code == '20':
            we = '雨夹雪'
        if code == '21':
            we = '阵雪'
        if code == '22':
            we = '小雪'
        if code == '23':
            we = '中雪'
        if code == '24':
            we = '大雪'
        if code == '25':
            we = '暴雪'
        if code == '26':
            we = '浮尘'
        if code == '27':
            we = '扬沙'
        if code == '28':
            we = '沙尘暴'
        if code == '29':
            we = '强沙尘暴'
        if code == '30':
            we = '雾'
        if code == '31':
            we = '霾'
        if code == '32':
            we = '风'
        if code == '33':
            we = '大风'
        if code == '34':
            we = '飓风'
        if code == '35':
            we = '热带风暴'
        if code == '36':
            we = '龙卷风'
        if code == '37':
            we = '冷'
        if code == '38':
            we = '热'
        if code == '99':
            we = '未知'
    oled.rect(5, 5, 118, 54, 1)
    oled.show()
    oled.shows('成都',x = 0,y = 10,size = 1,space = 0,center = True)
    oled.shows(h + '°',x = 10,y = 25,size = 1,space = 0,center = True)
    oled.shows(we,x = 10,y = 40,size = 1,space = 0,center = True)
    time.sleep(1)
    print('i=', i)
    print('t1=', t1)
    print('t2=', t2)
    print('c1=', c1)
    print('c2=', c2)
    print('m=', m)
    print('h=', h)
    print('code=', code)
    time.sleep(30)
    oled.fill(0)
    oled.show()

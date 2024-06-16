# ESP32-Weather-With-0.96-OLED-Display-Module
#### ESP32连接0.96’OLED屏幕实时显示天气及温度

#### Real-time weather display with ESP32 and 0.96'OLED screens

------



### 一、接线图

​          <img src="/wiringdiagram.png" style="zoom:50%;" />

##### 参数：

##### 4pin 0.96‘ oled（128*64）：HS96L03

##### ESP32 WROOM-32



------



### 二、注释



```
mixiot.wlan_connect('SSID','PASSWORD')
```

SSID改为WiFi名称；PASSWORD改为WiFi密码



```
i = str(seniverse_api.weather_now('API_PRIVATE_KEY','CITY'))
```

API_PRIVATE_KEY为[心知天气API](https://www.seniverse.com/)的私钥，CITY为所在地城市



​	
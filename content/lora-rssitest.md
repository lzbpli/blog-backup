Title: LoRaPA功率模块信号测试
Date: 2017-8-20
Category: lora
authors: ikerbo

## 信号测试

网关位置：722室窗户旁边
###**节点地址：fe00002a**
#### PA模块
- 办公室
rssi：9.8 rssi1:-49

- 7楼电梯
lsnr:7.2 rssi：-93
lsnr：6.0 rssi：-96
lsnr：0.0 rssi：-91

- 5楼
lsnr：-7.8 rssi：-102
lsnr：-4.8 rssi：-104
lsnr：-4.2 rssi：-103
lsnr：-7.2 rssi：-104
lsnr：-3.5 rssi：-102
 
- 3楼
lsnr：-6.0 rssi：-99
lsnr：0.5 rssi：-102
lsnr：-0.2 rssi：-99
lsnr：-0.8 rssi：-101
lsnr：0.2 rssi：-101

- 1楼
lsnr：-9.2 rssi：-106
lsnr：-7.8 rssi：-103
lsnr：-10.0 rssi：-105
lsnr：-7.8 rssi：-105
lsnr：-5.0 rssi：-106
 
#### 长天线
 - 办公室
 lsnr：9.8 rssi：-77
 
 - 7楼电梯
 lsnr：-8.2 rssi：-103
 lsnr：-3.8 rssi：-105
 lsnr：-3.8	rssi：-105

###**节点地址：fe00002c**
#### PA模块
 - 办公室
 lsnr：9.8 rssi：-47
#### 长天线
- 办公室
 lsnr：9.8	rssi：-17
  
以上数据均在PA模块5v供电的基础上，PA模块使用3.3v供电时，和长天线信号效果相同。 
 
测试过程中发现的问题：
- 相同节点、天线，天线竖放比平放的信号要好5~10db,其中竖放时，节点天线和网关之间遮挡物少一些。
- 不同节点的信号强度有明显差异，fe00002a、fe00002d的信号强度比fe00002c的信号强度要低30db
  
 查看原始数据，登陆https://cloud.sanfaniot.com，在设备管理->历史数据中，对应的时间是2017-8-16-14:57:55 
 到16:31:53区间，对应节点fe00002a，fe00002c

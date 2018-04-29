# show MQTT data on map, by maptalks
maptalks (http://maptalks.org) 是一款非常强大的地图渲染引擎。该样例展示如何通过PAHO MQTT javascript SDK订阅百度天工（https://cloud.baidu.com/product/iot.html）的MQTT消息，并且利用maptalks将带有地理坐标信息的消息，在地图上渲染出来。

# 使用步骤：

1，下载show_mqtt_data_with_maptalks.html到本地。


2，修改上述html文件，替换如下变量为您自己的MQTT信息：
```
var mqttEndpointUrl = "<your_endpoint_name>.mqtt.iot.bj.baidubce.com";
var mqttUserName = "<your_mqtt_user_name>";
var mqttPassword = "<your_mqtt_password>";
var mqttTopicToSub = "<your_mqtt_topic>";
```
	  
	  
3，通过MQTT工具（mqtt.fx, mqttbox）或者API，向上述MQTT主题发送如下格式的消息:
```
{
    "instance": "myendpoint",
    "clientId": "mqtt_clientid",
    "action": "Connect",
    "latitude": 31.23,
    "longitude": 121.47
}
```

	  
当收到一个action=Connect的消息，会在地图上相应的坐标画一个圆圈；当收到一个action=Disconnect的消息，会将之前画的圆圈删除。鼠标移动到圆圈上，会显示该点的instance和clientId信息。
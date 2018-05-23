var http = require('http');
exports.handler = (event, context, callback) => {
    sendMqttMessage();
    callback(null, "Hello world!");
};

function sendMqttMessage() {
  // MQTT消息的内容
  var post_data = '{"hello":"BaiduIot"}'

  var post_options = {
      // 华北区域请用：api.mqtt.iot.bj.baidubce.com
      host: 'api.mqtt.iot.gz.baidubce.com',
      port: '80',
      // 可以改参数： qos, topic, retain
      path: '/v1/proxy?qos=0&topic=topic_to_send&retain=false',
      method: 'POST',
      headers: {
          'Content-Type': 'application/octet-stream',
          'Content-Length': Buffer.byteLength(post_data),
          // 替换成你的MQTT用户名，格式如: myendpoint/mydevice
		  'auth.username': '<your mqtt username>',
          // 替换成你的MQTT密码，格式如: N....kdiekn9K4LXHpwRA=
		  'auth.password': '<your mqtt password>'
      }
  };

  // Set up the request
  var post_req = http.request(post_options, function(res) {
      res.setEncoding('utf8');
      res.on('data', function (chunk) {
          console.log('Response: ' + chunk);
      });
  });

  // post the data
  post_req.write(post_data);
  post_req.end();

}
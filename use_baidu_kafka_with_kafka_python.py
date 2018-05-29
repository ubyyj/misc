// kafka-python could be found at: https://github.com/dpkp/kafka-python
// this demos how to use kafka-python to connect to Baidu Kafka

// download and unzip the kafka-key.zip from Baidu Kafka web console, you will get following files:
// 1, ca.pem
// 2, client.key
// 3, client.keystore.jks
// 4, client.pem
// 5, client.properties
// 6, client.truststore.jks

conf = {
	'bootstrap_servers': 'kafka.bj.baidubce.com:9091',
	'security_protocol': 'SSL',
	'ssl_cafile': 'ca.pem',
	'ssl_certfile': 'client.pem',
	'ssl_keyfile': 'client.key',
	'ssl_password': '<get config ssl.keystore.password in file client.properties>',
	'ssl_check_hostname': False 
}
producer = KafkaProducer(**conf)
topic = 'a0333bd605cb453aa5e1717b26393a58__test'
while not self.stop_event.is_set():
	producer.send(topic, b"test")
	time.sleep(1)

producer.close()

// librdkafka could be found at: https://github.com/edenhill/librdkafka
// confluent_kafka could be found at: https://github.com/confluentinc/confluent-kafka-python
// this demos how to use librdkafka and confluent_kafka to connect to Baidu Kafka

// download and unzip the kafka-key.zip from Baidu Kafka web console, you will get following files:
// 1, ca.pem
// 2, client.key
// 3, client.keystore.jks
// 4, client.pem
// 5, client.properties
// 6, client.truststore.jks

conf = {
	'bootstrap.servers': 'kafka.bj.bce-internal.baidu.com:9071',
	'group.id': 'mygroup',
	'security.protocol': 'ssl',
	'ssl.ca.location': 'ca_pem',
	'ssl.certificate.location': 'client_pem',
	'ssl.key.location': 'client.key',
}

c = confluent_kafka.Consumer(**conf)
topic = 'a0333bd605cb453aa5e1717b26393a58__test'
c.subscribe([topic])
msg = c.poll(timeout=1.0)

import paho.mqtt.client as mqtt
broker_url = "192.168.75.68"
broker_port = 1883
client = mqtt.Client()
client.connect(broker_url, broker_port)
client.publish(topic="TestingTopic", payload="data pulish", qos=1, retain=False)

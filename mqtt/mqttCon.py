import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


def activa(msg: str):
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set up GPIO pin 17 as an output
    GPIO.setup(21, GPIO.OUT)

    if (msg == "ON"):
        GPIO.output(21, GPIO.HIGH)
        time.sleep(1500)
        GPIO.output(21, GPIO.LOW)
        time.sleep(1)


class MQTTReader:
    def __init__(self, broker_host, broker_port, topic,username=None, password=None):
        # Configura las variables del servidor MQTT y el tema
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.topic = topic
        self.username = username
        self.password = password


        # Crea una instancia del cliente MQTT
        self.client = mqtt.Client()



        # Configura las funciones de callback
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        if self.username and self.password:
            self.client.username_pw_set(self.username, self.password)

        # Conéctate al servidor MQTT
        self.client.connect(self.broker_host, self.broker_port, 60)

        # Inicia el bucle de mensajes
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Conectado con el código de resultado: " + str(rc))
        # Suscríbete al tema al conectarte
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        activa(msg)


# Uso de la clase MQTTReader
if __name__ == "__main__":
    # Configura la información del servidor MQTT y el tema
    broker_host = "192.168.1.39"
    broker_port = 1884
    topic = "test"
    username = "username"
    password = "test"

    # Crea una instancia de MQTTReader
    mqtt_reader = MQTTReader(broker_host, broker_port, topic)

    try:
        # Mantén el programa en ejecución
        while True:
            pass
    except KeyboardInterrupt:
        # Detén el bucle de mensajes y desconéctate al recibir una interrupción del teclado
        mqtt_reader.client.loop_stop()
        mqtt_reader.client.disconnect()

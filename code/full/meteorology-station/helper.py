from time import sleep
import network
from umqtt.simple import MQTTClient
from machine import Pin
import ujson


def read_light(adc_pin):
    light = adc_pin.read_u16()
    light = 100 - round(light/65535*100)
    return light

def create_json(time, temperature, humidity, light):
    #2023-03-20T16:21Z
    t_str = "{}-{}-{}T{}:{}Z".format(time[0], time[1], time[2], time[3], time[4])
    buf = {'time': t_str,
    'temperature': temperature,
    'humidity': humidity,
    'light': light
    }
    return ujson.dumps(buf)
    

def do_connect_wifi(ssid, password):
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            wlan.connect(ssid, password)
            i = 0
            while not wlan.isconnected():
                print('connecting to network...')
                i += 1
                sleep(5)
                if(i == 3):
                    print('wifi denied')
                    return False
        print('wifi connected')
        return True
    except Exception as e:
        print(f"ERROR: {e}")
        print('wifi denied')
        return False

def do_connect_broker(name, server, port, login, password):
    try:
        mqtt = MQTTClient(name, server=server, port=port, user=login, password=password, keepalive=3600)
        while mqtt.connect():
            print('connecting to bouker...')
            i += 1
            sleep(5)
            if(i == 3):
                print('wifi denied')
                return None
        print("brouker connected")
        return mqtt
    except Exception as e:
        print(f"ERROR: {e}")
        print("brouker denied")
        return None
    
def send_mqtt_mesage(mqtt, topic, mesage):
    try:
        if(mqtt.publish(topic, mesage)):
            print("message denied")
            return False
        print("message sent")
        return True
    except Exception as e:
        print(f"ERROR: {e}")
        print("message denied")
        return False
      
    

        
        
        
        
        
        
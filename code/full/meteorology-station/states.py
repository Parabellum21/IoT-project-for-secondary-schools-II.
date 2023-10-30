import ntptime
import utime
import _thread
import json
import settings
from dht import DHT11
from machine import Pin, ADC, deepsleep, RTC, WDT
import helper
from time import sleep

#Premenné, ktoré označujú konkrétny stav
INIT = 1
MEASURE = 2
UPLOAD = 3
SLEEP = 4

#Definovanie pinov
pin_dht = DHT11(Pin(settings.DHT_PIN))
pin_svetla = ADC(Pin(settings.LIGHT_PIN))
pin_led = Pin(settings.LED_PIN, Pin.OUT)

#--------------------------------------------------------------------------------------------------------------    

#pomocné funkcie
def read_file():
    f = open(settings.DATA_FILE, 'r')
    
    string = f.read().split('\n')
    try:
        string.remove('')
    except:
        pass
    
    print("read:")
    for i in string:
        print(i)
    print("-----------------------")

    f.close()
    
    return string

def write_file(string):
    f = open(settings.DATA_FILE, 'w')
    
    try:
        string.remove('')
    except:
        pass
    
    print("write:")
    for i in range(len(string)):
        f.write(string[i] + "\n")
        print(string[i])
    print("-----------------------")
    
    
    f.close()
    
def time_blink(time_light, steps):
    for i in range(steps):
        pin_led.value(1)
        sleep(time_light)
        pin_led.value(0)
        sleep(0.5)
        
        
def print_status(temperature, humidity, light):
    print('--------------')
    print('t:', temperature)
    print('h:', humidity)
    print('l:', light)
    print('--------------')
    
    
#--------------------------------------------------------------------------------------------------------------    

#basic function
def init(context):
    print(context)
    context.wifi = helper.do_connect_wifi(settings.WIFI_LOGIN, settings.WIFI_PASSWORD)
    #signalizácia problémov LEDkov
    if(context.wifi):
        time_blink(3, 1)
    else:
        time_blink(0.1, 15)
        
    if(context.wifi):
        #nastavenie casu
        ntptime.settime()
        #brouker
        context.mqtt = helper.do_connect_broker(settings.MQTT_NAME, settings.MQTT_IP, settings.MQTT_PORT, settings.MQTT_LOGIN, settings.MQTT_PASSWORD)
        if(context.mqtt == None):
            context.brouker = False;
        else:
            context.brouker = True;
        #signalizácia problémov LEDkov
        if(context.brouker):
            time_blink(3, 1)
        else:
            time_blink(0.1, 10)
            
    #Zmena stavu        
    context.state = MEASURE

def measure(context):
    #buferne premenne
    temperature = [0] * 3
    humidity = [0] * 3
    light = [0] * 3
    
    #Meranie 3 krát
    for i in range(3):
        pin_dht.measure()
        temperature[i] = pin_dht.temperature()
        humidity[i] = pin_dht.humidity()
        light[i] = helper.read_light(pin_svetla)
        
        print_status(temperature[i], humidity[i], light[i])
        
        sleep(1)
    #sortovanie a zisťovanie mediánu
    temperature.sort()
    humidity.sort()
    light.sort()
    context.temperature = temperature[1]
    context.humidity = humidity[1]
    context.light = light[1]
    
    #konečný výsledok
    print('***\nPRIEMER')
    print_status(context.temperature, context.humidity, context.light)
    
    #Zmena stavu 
    context.state = UPLOAD

def upload(context):
    #prepair
    time = utime.gmtime(utime.mktime(utime.localtime()))
    
    #vitvorenie jsonu
    json = helper.create_json(time, context.temperature, context.humidity, context.light)
    print(json)
    #zčítanie inich JSONov zo súboru
    regected_json = []
    json_list = read_file()
    json_list.append(json)
    #Ak nie je k dispozícii internetové pripojenie, všetky merania sa zaznamenajú do súboru
    if(context.wifi and context.brouker):
        for i in range(len(json_list)):
            #odosielanie údajov na server
            message = helper.send_mqtt_mesage(context.mqtt, settings.MQTT_TOPIC, json_list[i])
            print(json_list[i])
            #signalizácia problémov LEDkov
            if(message):
                time_blink(2, 1)
            else:
                regected_json.append(json_list[i])
                time_blink(0.1, 5)
                

    if(not context.wifi or not context.brouker):
        regected_json = json_list
        
    if(context.wifi and context.brouker):
        regected_json.clear()
        regected_json.append('')
     
    #zápis do súboru
    write_file(regected_json)
    
    #Zmena stavu 
    context.state = SLEEP
    
def sleep_pico(context):
    #zaspanie na 3 minuti
    #full sleap
    #deepsleep(180000)
    #test
    sleep(180)
    
    #Zmena stavu 
    context.state = INIT
    
    
    
    
    
    
    
    
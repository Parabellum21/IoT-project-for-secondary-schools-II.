from dht import DHT11
from machine import Pin, ADC
import helper


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

#basic function
def init(context):
    
    #Napíš svoj kód
            
    #Zmena stavu        
    context.state = MEASURE

def measure(context):
    
    #Napíš svoj kód
    
    #Zmena stavu 
    context.state = UPLOAD

def upload(context):
    
    #Napíš svoj kód
    
    #Zmena stavu 
    context.state = SLEEP
    
def sleep_pico(context):
    
    #Napíš svoj kód
    
    #Zmena stavu 
    context.state = INIT
    
    
    
    
    
    
    
    
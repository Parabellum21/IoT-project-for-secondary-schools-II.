import states

#Globálny priestor pre pomocné premenné.
#V prípade potreby môžete pridať vlastné premenné.
class Context:
    state: int = states.INIT
    
    wifi: bool = False
    broker: bool = False
    
    mqtt: MQTTClient = None 
    
    temperature: float = None
    humidity: int = None
    light: int = None

#miesto spustenia programu
if __name__ == "__main__":
    context = Context()
    
    #Logika zmeny stavov
    while True:
        if context.state == states.INIT:
            states.init(context)
        elif context.state == states.MEASURE:
            states.measure(context)
        elif context.state == states.UPLOAD:
            states.upload(context)
        elif context.state == states.SLEEP:
            states.sleep_pico(context)
        else:
            print('unknown state')



    
    
    
    
    

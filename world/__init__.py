import world.text.world as env

def setup_env(environment: str):
    "Imports the correct environment text or turtle"
    
    global env
    
    if environment == 'text' or environment == '':
        import world.text.world as env
    elif environment == 'turtle':
        import world.turtle.world as env
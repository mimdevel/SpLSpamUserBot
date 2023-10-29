import os

class API:
    API_ID = int(os.getenv("API_ID", "25753982"))
    API_HASH = os.getenv("API_HASH", "a395504c6bd9dcd2eb201ad662475240")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6308290586:AAFTVbL66Kr67PFDsThfLKqz5u7kCpwIncE")
    STRING_SESSION = os.getenv("STRING_SESSION", "BAGI-X4AgAAdmVOen-EDp9So9JYNyXLVBPP21ffhGNUyePtBWq2T1vqDNTgBH0NGgHeKCfiQ8p8GD8Q6LB4zFETE6lEZtmSAv6r5hAxmCwgIGDJ41gRw6l70MiHKvbnqBdG8Ll7e70EKs1ZfO77pqqQ30U9x1JHScuStIK4H2zBI52CQ6aiWZkpOAEbCg82PlrprMIMCaFacMw6ZM_lwehzPGOD8UDK5d7J1bBZlLhtapMCcvZz_qz_lu0btV4E7IUYP_Lj0kEk45S8YeOhp1mfr8kVq5ABFFRET6m7EwMv8Ob_W5HN5RwOdP5J7LijDnvrGr9QAnRtXlZQZYIrXusvXoBX7DwAAAAGR7RhHAA")
    STRING_SESSION_2 = os.getenv("STRING_SESSION_2", "")
    STRING_SESSION_3 = os.getenv("STRING_SESSION_3", "")
    STRING_SESSION_4 = os.getenv("STRING_SESSION_4", "")
    STRING_SESSION_5 = os.getenv("STRING_SESSION_5", "")
    STRING_SESSION_6 = os.getenv("STRING_SESSION_6", "")
    STRING_SESSION_7 = os.getenv("STRING_SESSION_7", "")
    STRING_SESSION_8 = os.getenv("STRING_SESSION_8", "")
    STRING_SESSION_9 = os.getenv("STRING_SESSION_9", "")
    STRING_SESSION_10 = os.getenv("STRING_SESSION_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "6743201863"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "https://te.legra.ph/file/e18a7ce5cfb6e9fcc382d.jpg")
    HELP_PIC = os. getenv("HELP_PIC", "https://te.legra.ph/file/e18a7ce5cfb6e9fcc382d.jpg")
    START_PIC = os. getenv("START_PIC", "https://te.legra.ph/file/e18a7ce5cfb6e9fcc382d.jpg")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", "!")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # CHANGE 'True' TO 'False' IF YOU WANNA DISABLE PORN

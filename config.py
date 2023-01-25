# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "19900446"))
API_HASH = os.environ.get("API_HASH", "394551f895e06490e43c12795c1a418d)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5944151369:AAFXdIi5wPzm-CXwm-2uqOnpEI0HWPWNPKU)
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5932343611")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "DARKHOSTIN")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5932343611")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100DARKHOSTIN/15")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "DARKHOST SHORTNER  @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"

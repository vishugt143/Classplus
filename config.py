import os

API_ID = API_ID = 20544260

API_HASH = os.environ.get("API_HASH", "a0b00461d3fba22aa186fa648d77787e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6768420785:AAFqlFpxDVOS4M761pIAzrls_2pUK5jfOQQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6389388334))

LOG = -1002032855927

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1311808931").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



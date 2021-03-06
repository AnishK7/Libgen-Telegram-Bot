import os
import logging


# mode = os.getenv("MODE")
# TELEGRAM_ACCESS_TOKEN = os.getenv("TOKEN")

mode = "prod"
TELEGRAM_ACCESS_TOKEN = ""
HEROKU_APP_NAME = ""
LIBGEN_DOMAIN = "https://libgen.is/"

# Enable logging
logging.basicConfig(format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()

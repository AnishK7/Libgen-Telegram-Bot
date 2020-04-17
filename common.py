import os
import logging


# mode = os.getenv("MODE")
# TELEGRAM_ACCESS_TOKEN = os.getenv("TOKEN")

mode = "prod"
TELEGRAM_ACCESS_TOKEN = "938130802:AAGbowLZIwP9qWfCpzdVInUH8btZ0Rddzzw"
HEROKU_APP_NAME = "libgens-bot"
LIBGEN_DOMAIN = "https://libgen.is/"

# Enable logging
logging.basicConfig(format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
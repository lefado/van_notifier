import logging

from milanuncios import Milanuncios
from notification import Twilio


milalnuncios = Milanuncios()
twilio = Twilio()

web = milalnuncios.fetch()
vans = milalnuncios.parse(web)
twilio.send(vans)
logging.info(f'{len(vans)} Notifications have been sent!')
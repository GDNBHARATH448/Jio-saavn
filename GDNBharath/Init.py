from GDNBHARATH.core.bot import GDN
from GDNBHARATH.core.dir import dirr
from GDNBHARATH.core.git import git
from GDNBHARATH.core.userbot import Userbot
from GDNBHARATH.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = GDN()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
jiosaavn = jiosaavnAPI()

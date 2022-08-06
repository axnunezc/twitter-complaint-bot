from decouple import config
from bot import InternetSpeedTwitterBot

USERNAME = config("USERNAME")
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

PROMISED_UP = 10
PROMISED_DOWN = 20

bot = InternetSpeedTwitterBot()

bot.get_internet_speeds()
down = bot.down
up = bot.up

if down + 5 < PROMISED_DOWN or up + 3 < PROMISED_UP:
    bot.twitter_login(EMAIL, USERNAME, PASSWORD)
    bot.tweet_at_provider(PROMISED_UP, PROMISED_DOWN)
else:
    print("Adequate download/upload speed")
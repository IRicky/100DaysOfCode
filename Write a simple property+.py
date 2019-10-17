# Write a simple Promo class. Its constructor receives a name str and expires datetime.

# Add a property called expired which returns a boolean value indicating whether the promo has expired or not.

# Checkout the tests and datetime module for more info. Have fun!

from datetime import datetime, timedelta, date

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        if self.expires < NOW:
            return True
        else:
            return False


past_time = NOW - timedelta(seconds=3)
twitter_promo = Promo('twitter', past_time)
print(twitter_promo.expired)

from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config("postgres://kivwfaffzocggt:4deadaaf1500d44d654a006e64ec0d39ba1cd74b8f5a3226667878e08c89aa6e@ec2-79-125-125-97.eu-west-1.compute.amazonaws.com:5432/d3r6t7jgtulhi4")

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_mNb1dKaAFoLSHyj2BAcDMl99')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_blRbu4P14RH0LjZMT2jDpwxy')

# Paypal environment variables
SITE_URL = 'code-institute-social.herokuapp.com'
PAYPAL_NOTIFY_URL = 'code-institute-social.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'christoal-facilitator@outlook.com'

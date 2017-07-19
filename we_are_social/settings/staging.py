from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_mNb1dKaAFoLSHyj2BAcDMl99')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_blRbu4P14RH0LjZMT2jDpwxy')

# Paypal environment variables
SITE_URL = 'code-institute-social.herokuapp.com'
PAYPAL_NOTIFY_URL = 'code-institute-social.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'christoal-facilitator@outlook.com'

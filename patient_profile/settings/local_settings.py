# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'patient_profile',
        'USER': 'bishal',
        'PASSWORD': 'bishal',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kh%t73*cdg9e)#51sv9ok7@rl=l8ezz=g&)%!@2puf0&3p&k3_'

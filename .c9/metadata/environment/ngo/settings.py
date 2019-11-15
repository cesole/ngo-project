{"changed":true,"filter":false,"title":"settings.py","tooltip":"/ngo/settings.py","value":"\"\"\"\nDjango settings for ngo project.\n\nGenerated by 'django-admin startproject' using Django 1.11.24.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n\nimport os\nimport env\nimport dj_database_url\n\n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\nEMAIL_HOST = \"smtp.mail.yahoo.com\"\nEMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')\nEMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')\nEMAIL_PORT = 587\nEMAIL_USE_TLS = True\nEMAIL_BACKEND = \"django.core.mail.backends.smtp.EmailBackend\"\nDEFAULT_FROM_EMAIL = \"ces99_torres@yahoo.com\"\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = os.environ.get(\"SECRET_KEY\")\n\n# SECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True\n\nALLOWED_HOSTS = ['516d4b3829444a14b39c17b772e7db40.vfs.cloud9.us-east-1.amazonaws.com', 'ngo-ces.herokuapp.com']\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'django_forms_bootstrap',\n    'home',\n    'accounts',\n    'children',\n    'cart',\n    'checkout',\n    'community',\n    'contact',\n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n    'whitenoise.middleware.WhiteNoiseMiddleware',\n]\n\nROOT_URLCONF = 'ngo.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [os.path.join(BASE_DIR, 'templates')],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n                'django.template.context_processors.media',\n                'cart.contexts.cart_contents',\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'ngo.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\n\nif \"DATABASE_URL\" in os.environ:\n    DATABASES = {\n        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))\n    }\nelse:\n    print(\"Postgres URL not found, using sqlite instead\")\n    DATABASES = {\n        'default': {\n            'ENGINE': 'django.db.backends.sqlite3',\n            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n        }\n    }\n\n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\n\n\nAUTHENITCATION_BACKENDS = [\n    'django.contrib.auth.backends.ModelBackend',\n    'accounts.backends.CaseInsensitiveAuth',\n    \n    ]\n\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nSTATIC_URL = '/static/'\n\nSTATICFILES_DIRS = (\n    os.path.join(BASE_DIR, \"static\"),\n)\nSTATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')\n\nSTRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')\nSTRIPE_SECRET = os.getenv('STRIPE_SECRET')\n\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\nMEDIA_URL = '/media/'\n\n\nMESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'","undoManager":{"mark":-2,"position":0,"stack":[[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":1}]]},"ace":{"folds":[],"scrolltop":358.5,"scrollleft":0,"selection":{"start":{"row":13,"column":1},"end":{"row":13,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":28,"state":"start","mode":"ace/mode/python"}},"timestamp":1573812710853}
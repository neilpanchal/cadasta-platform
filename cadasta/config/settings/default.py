"""
Django settings for cadasta project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext_lazy as _
from .languages import FORM_LANGS  # noqa

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=fy$)xx+6yjo*us@&+m6$14@l-s6#atg(msm=9%)9@%b7l%h('

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'django.contrib.humanize',
    'corsheaders',

    'core',
    'geography',
    'accounts',
    'organization',
    'spatial',
    'questionnaires',
    'resources',
    'buckets',
    'party',
    'xforms',
    'search',
    'tasks',

    'django_filters',
    'crispy_forms',
    'parsley',
    'widget_tweaks',
    'django_countries',
    'leaflet',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'rest_framework_docs',
    'djoser',
    'tutelary',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'sass_processor',
    'simple_history',
    'jsonattrs',
    'compressor',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'accounts.middleware.UserLanguageMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_tmp_scoped_token.TokenAuth',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_VERSIONING_CLASS':
        'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_VERSION': 'v1',
    'EXCEPTION_HANDLER': 'core.views.api.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'HTML_SELECT_CUTOFF': 100,
}

SITE_NAME = 'Cadasta'

BASE_TEMPLATE_DIR = os.path.join(os.path.dirname(BASE_DIR), 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_TEMPLATE_DIR,
                 os.path.join(BASE_TEMPLATE_DIR, 'allauth')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'core.backends.Auth',
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.AuthenticationBackend'
]

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

DJOSER = {
    'SITE_NAME': SITE_NAME,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL':
    'account/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'account/activate/{uid}/{token}',
    # 'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'set_password_retype': 'accounts.serializers.ChangePasswordSerializer'
    }
}

CORS_ORIGIN_ALLOW_ALL = False

LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'

WSGI_APPLICATION = 'config.wsgi.application'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_FORMS = {
    'signup': 'accounts.forms.RegisterForm',
    'profile': 'accounts.forms.ProfileForm',
}
ACCOUNT_ADAPTER = 'accounts.adapter.DefaultAccountAdapter'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.UserAttributeSimilarityValidator'),
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10,
        }
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME':
            'accounts.validators.CharacterTypePasswordValidator'
    },
    {
        'NAME':
            'accounts.validators.EmailSimilarityValidator'
    },
]

OSM_ATTRIBUTION = _(
    "Base map data &copy; <a href=\"http://openstreetmap.org\">"
    "OpenStreetMap</a> contributors under "
    "<a href=\"http://opendatacommons.org/licenses/odbl/\">ODbL</a>"
)
DIGITALGLOBE_ATTRIBUTION = _("Imagery &copy; DigitalGlobe")
DIGITALGLOBE_TILESET_URL_FORMAT = (
    'https://{{s}}.tiles.mapbox.com/v4/digitalglobe.{}'
    '/{{z}}/{{x}}/{{y}}.png?access_token='
    'pk.eyJ1IjoiZGlnaXRhbGdsb2JlIiwiYSI6ImNpaHhtenBmZjAzYW1'
    '1a2tvY2p3MnpjcGcifQ.vF1gH0mGgK31yeHC1k1Tqw'
)

LEAFLET_CONFIG = {
    'TILES': [
        (
            _("OpenStreetMap"),
            'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            {'attribution': OSM_ATTRIBUTION,
             'maxZoom': 19}
        ),
        (
            _("+Vivid imagery"),
            DIGITALGLOBE_TILESET_URL_FORMAT.format('n6ngnadl'),
            {'attribution': DIGITALGLOBE_ATTRIBUTION,
             'maxZoom': 22}
        ),
        (
            _("Recent imagery"),
            DIGITALGLOBE_TILESET_URL_FORMAT.format('nal0g75k'),
            {'attribution': DIGITALGLOBE_ATTRIBUTION,
             'maxZoom': 22}
        ),
        (
            _("+Vivid imagery with OpenStreetMap"),
            DIGITALGLOBE_TILESET_URL_FORMAT.format('n6nhclo2'),
            {'attribution': (OSM_ATTRIBUTION, DIGITALGLOBE_ATTRIBUTION),
             'maxZoom': 22}
        ),
        (
            _("Recent imagery with OpenStreetMap"),
            DIGITALGLOBE_TILESET_URL_FORMAT.format('nal0mpda'),
            {'attribution': (OSM_ATTRIBUTION, DIGITALGLOBE_ATTRIBUTION),
             'maxZoom': 22}
        ),
    ],
    'RESET_VIEW': False,
    'PLUGINS': {
        'draw': {
            'js': '/static/leaflet/draw/leaflet.draw.js'
        },
        'groupedlayercontrol': {
            'js': '/static/js/leaflet.groupedlayercontrol.min.js',
            'css': '/static/css/leaflet.groupedlayercontrol.min.css'
        }
    }
}

# Invalid names for Cadasta organizations, projects, and usernames
CADASTA_INVALID_ENTITY_NAMES = ['add', 'new']

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LANGUAGES = [
    # ('ar', _('Arabic')),    (hiding until RTL support fixed)
    ('en', _('English')),
    ('fr', _('French')),
    # ('de', _('German')),    (hiding until translation coverage >= 75%)
    ('es', _('Spanish')),
    ('id', _('Indonesian')),
    ('it', _('Italian')),
    ('pt', _('Portuguese'))
    # ('sw', _('Swahili')),   (hiding until translation coverage >= 75%)
]
MEASUREMENT_DEFAULT = 'metric'

MEASUREMENTS = [
    ('metric', _('Metric')),
    ('imperial', _('Imperial')),
]

DEFAULT_AVATAR = '/static/img/avatar_sm.jpg'
ACCEPTED_AVATAR_TYPES = ['image/png', 'image/jpeg']

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
SASS_PROCESSOR_INCLUDE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'core/node_modules'),
)
# Required for bootstrap-sass
# https://github.com/jrief/django-sass-processor
SASS_PRECISION = 8

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'core/media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'core/static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
)

JSONATTRS_SCHEMA_SELECTORS = {
    'spatial.spatialunit': (
        'project.organization.pk',
        'project.pk', 'project.current_questionnaire'
    ),
    'spatial.spatialrelationship': (
        'project.organization.pk', 'project.pk',
        'project.current_questionnaire'
    ),
    'party.party': (
        'project.organization.pk', 'project.pk',
        'project.current_questionnaire',
        'type'
    ),
    'party.partyrelationship': (
        'project.organization.pk', 'project.pk',
        'project.current_questionnaire'
    ),
    'party.tenurerelationship': (
        'project.organization.pk', 'project.pk',
        'project.current_questionnaire'
    )
}

ATTRIBUTE_GROUPS = {
    'location_attributes': {
        'app_label': 'spatial',
        'model': 'spatialunit',
        'label': 'Location'
    },
    'party_attributes': {
        'app_label': 'party',
        'model': 'party',
        'label': 'Party'
    },
    'location_relationship_attributes': {
        'app_label': 'spatial',
        'model': 'spatialrelationship',
        'label': 'Spatial relationship'
    },
    'party_relationship_attributes': {
        'app_label': 'party',
        'model': 'partyrelationship',
        'label': 'Party relationship'
    },
    'tenure_relationship_attributes': {
        'app_label': 'party',
        'model': 'tenurerelationship',
        'label': 'Tenure Relationship'
    }
}

ICON_URL = ('https://s3-us-west-2.amazonaws.com/cadasta-resources'
            '/icons/{}.png')

ICON_LOOKUPS = {
    'application/pdf': 'pdf',
    'audio/1d-interleaved-parityfec': 'audio',
    'audio/32kadpcm': 'audio',
    'audio/3gpp': 'audio',
    'audio/3gpp2': 'audio',
    'audio/ac3': 'audio',
    'audio/aac': 'audio',
    'audio/aacp': 'audio',
    'audio/amr': 'audio',
    'audio/amr-wb': 'audio',
    'audio/amr-wb+': 'audio',
    'audio/aptx': 'audio',
    'audio/asc': 'audio',
    'audio/ATRAC-ADVANCED-LOSSESS': 'audio',
    'audio/ATRAC-X': 'audio',
    'audio/ATRAC3': 'audio',
    'audio/basic': 'audio',
    'audio/BV16': 'audio',
    'audio/BV32': 'audio',
    'audio/clearmode': 'audio',
    'audio/CN': 'audio',
    'audio/DAT12': 'audio',
    'audio/dls': 'dls',
    'audio/dsr-es201108': 'audio',
    'audio/dsr-es202050': 'audio',
    'audio/dsr-es202211': 'audio',
    'audio/dsr-es202212': 'audio',
    'audio/DV': 'audio',
    'audio/DV14': 'audio',
    'audio/eac3': 'audio',
    'audio/encaprtp': 'audio',
    'audio/EVRC': 'audio',
    'audio/EVRC-QCP': 'audio',
    'audio/EVRC0': 'audio',
    'audio/EVRC1': 'audio',
    'audio/EVRCB': 'audio',
    'audio/EVRCB0': 'audio',
    'audio/EVRCB1': 'audio',
    'audio/EVRCNW': 'audio',
    'audio/EVRCNW0': 'audio',
    'audio/EVRCNW1': 'audio',
    'audio/EVRCWB': 'audio',
    'audio/EVRCWB0': 'audio',
    'audio/EVRCWB1': 'audio',
    'audio/EVS': 'audio',
    'audio/example': 'audio',
    'audio/fwdred': 'audio',
    'audio/G711-0': 'audio',
    'audio/G719': 'audio',
    'audio/G7221': 'audio',
    'audio/G722': 'audio',
    'audio/G723': 'audio',
    'audio/G726-16': 'audio',
    'audio/G726-24': 'audio',
    'audio/G726-32': 'audio',
    'audio/G726-40': 'audio',
    'audio/G728': 'audio',
    'audio/G729': 'audio',
    'audio/G7291': 'audio',
    'audio/G729D': 'audio',
    'audio/G729E': 'audio',
    'audio/GSM': 'audio',
    'audio/GSM-EFR': 'audio',
    'audio/GSM-HR-08': 'audio',
    'audio/iLBC': 'audio',
    'audio/ip-mr_v2.5': 'audio',
    'audio/L8': 'audio',
    'audio/L16': 'audio',
    'audio/L20': 'audio',
    'audio/L24': 'audio',
    'audio/LPC': 'audio',
    'audio/mobile-xmf': 'audio',
    'audio/MPA': 'audio',
    'audio/MP4A-LATM': 'audio',
    'audio/mpa-robust': 'audio',
    'audio/m4a': 'audio',
    'audio/midi': 'audio',
    'audio/mpeg1': 'audio',
    'audio/MPA2': 'audio',
    'audio/mpa-robust3': 'audio',
    'audio/mpeg3': 'mp3',
    'audio/mpeg': 'mp3',
    'audio/mp3': 'mp3',
    'audio/mp4': 'mp4',
    'audio/mpeg4-generic': 'mp4',
    'audio/ogg': 'audio',
    'audio/opus': 'audio',
    'audio/parityfec': 'audio',
    'audio/PCMA': 'audio',
    'audio/PCMA-WB': 'audio',
    'audio/PCMU': 'audio',
    'audio/PCMU-WB': 'audio',
    'audio/QCELP': 'audio',
    'audio/raptorfec': 'audio',
    'audio/RED': 'audio',
    'audio/rtp-enc-aescm128': 'audio',
    'audio/rtploopback': 'audio',
    'audio/rtp-midi': 'audio',
    'audio/rtx': 'audio',
    'audio/SMV': 'audio',
    'audio/SMV0': 'audio',
    'audio/SMV-QCP': 'audio',
    'audio/sp-midi': 'audio',
    'audio/speex': 'audio',
    'audio/t140c': 'audio',
    'audio/t38': 'audio',
    'audio/telephone-event': 'audio',
    'audio/tone': 'audio',
    'audio/UEMCLIP': 'audio',
    'audio/ulpfec': 'audio',
    'audio/VDVI': 'audio',
    'audio/VMR-WB': 'audio',
    'audio/vorbis': 'audio',
    'audio/vorbis-config': 'audio',
    'audio/wav': 'audio',
    'audio/wave': 'audio',
    'audio/x-flac': 'audio',
    'audio/x-mpeg-3': 'mp3',
    'audio/x-midi': 'audio',
    'audio/x-wav': 'audio',
    'video/mpeg': 'mp3',
    'video/x-mpeg': 'mp3',
    'video/mp4': 'mp4',
    'application/msword': 'doc',
    'application/vnd.openxmlformats-officedocument.'
    'wordprocessingml.document': 'docx',
    'application/msexcel': 'xls',
    'application/vnd.ms-excel': 'xls',
    'application/vnd.openxmlformats-'
    'officedocument.spreadsheetml.sheet': 'xlsx',
    'text/xml': 'xml',
    'application/xml': 'xml',
    'text/csv': 'csv',
    'text/plain': 'csv',
    'image/jpeg': 'jpg',
    'image/png': 'png',
    'image/gif': 'gif',
    'image/tif': 'tiff',
    'image/tiff': 'tiff',
    'image/bmp': 'image',
    'image/x-windows-bmp': 'image',
    'application/gpx+xml': 'gpx',
    'application/rtf': 'doc',
    'application/x-rtf': 'doc',
    'application/postscript': 'doc',
    'application/x-troff-msvideo': 'video',
    'video/avi': 'avi',
    'video/msvideo': 'wmv',
    'video/x-msvideo': 'wmv',
    'video/x-ms-wmv': 'wmv',
    'video/quicktime': 'video',
    'application/ogg': 'audio',
    'image/svg+xml': 'svg',
    'audio/x-ms-wma': 'audio',
    'application/vnd.oasis.opendocument.spreadsheet': 'ods',
    'application/vnd.oasis.opendocument.text': 'odt',
    'application/vnd.oasis.opendocument.presentation': 'odd',
    'application/vnd.ms-powerpoint': 'ppt',
    'application/vnd.openxmlformats-officedocument.presentationml.'
    'presentation': 'pptx',
    'application/x-iwork-keynote-sffkey': 'key',
    'video/x-m4v': 'mp4',
    'video/x-matroska': 'video',
}

MIME_LOOKUPS = {
     'gpx': 'application/gpx+xml'
}

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

# the first hasher in this list is the preferred algorithm.  any
# password using different algorithms will be converted automatically
# upon login
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

IMPORTERS = {
    'csv': 'organization.importers.csv.CSVImporter',
    'xls': 'organization.importers.xls.XLSImporter'
}

ES_SCHEME = 'http'
ES_HOST = 'localhost'
ES_PORT = '9200'
ES_MAX_RESULTS = 10000

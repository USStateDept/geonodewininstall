from settings import *
import geonode

INSTALLED_APPS  = ("maploom",)  + INSTALLED_APPS + ("geonode.contrib.geogig","django_classification_banner",) 

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'django_classification_banner.context_processors.classification',
)

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': '__databasename__',
         'USER': '__postgresuser__',
         'PASSWORD': '__postgrespwd__',
     },
     #vector datastore for uploads
     'datastore' : {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         #'ENGINE': '', # Empty ENGINE name disables 
         'NAME': '__gisdatabasename__',
         'USER': '__postgresuser__',
         'PASSWORD': '__postgrespwd__',
         'HOST' : 'localhost',
         'PORT' : '5432',
     }
}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : 'http://__baseurl__/geoserver/',
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : True,
        'WMST_ENABLED' : False,
        #signals line 95
        'BACKEND_WRITE_ENABLED': False,
        'WPS_ENABLED' : False,
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'datastore', #'datastore',
    }
}


# Reconcile with ``settings.py``
#MAP_BASELAYERS[0]["source"]["url"] = (OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms" if OGC_SERVER and any(OGC_SERVER) else 'http://localhost:8080/geoserver/wms')


STATIC_ROOT = "__geonodedir__/GeoNode/geonode/static_root"
MEDIA_ROOT = "__geonodedir__/GeoNode/geonode/uploaded"

MAX_DOCUMENT_SIZE = 50  # MB

SITEURL = "http://__baseurl__/"

#ROGUE Setting
#AUTHENTICATION_BACKENDS = ('geonode.security.auth.GranularBackend',)


SOCIAL_BUTTONS = False

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('geonode.security.middleware.LoginRequiredMiddleware',)

PROXY_ALLOWED_HOSTS = ("geonode.localhost", "__baseurl__")

CACHES = {
    # DUMMY CACHE FOR DEVELOPMENT
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    # },
    #MEMCACHED EXAMPLE
    #'default': {
    #    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #    'LOCATION': '127.0.0.1:11211',
    #    },
    #FILECACHE EXAMPLE
    'default': {
       'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
       'LOCATION': '__geonodedir__/filecache',
       }
}

GEOGIG_DATASTORE_NAME = "geogig"

UPLOADER = {
    'BACKEND': 'geonode.importer',
    'OPTIONS': {
        'TIME_ENABLED': False,
        'GEOGIG_ENABLED': True,
    }
}

GEONODE_ROOT = os.path.dirname(geonode.__file__)

TEMPLATE_DIRS = (
#    'C:/Geonode/GeoNode/extratemplates',
    os.path.join(GEONODE_ROOT, 'templates'),
    
)

STATICFILES_DIRS = [
#    'C:/Geonode/GeoNode/extratemplates/static',
    os.path.join(GEONODE_ROOT, 'static'),
    
]



# TEMPLATE_CONTEXT_PROCESSORS += (
#     'django_classification_banner.context_processors.classification',
#     #'geoshape.core.context_processors.security_warnings'
# )





# The FULLY QUALIFIED url to the GeoServer instance for this GeoNode.
GEOSERVER_BASE_URL = SITEURL + 'geoserver/'

MAP_BASELAYERS = [{
    "source": {
        "ptype": "gxp_wmscsource",
        "url": GEOSERVER_BASE_URL + "wms",
        "restUrl": "/gs/rest"
     }
  },{
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer",
    "args":["No background"],
    "visibility": False,
    "fixed": True,
    "group":"background"
  }, {
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer.OSM",
    "args":["OpenStreetMap"],
    "visibility": False,
    "fixed": True,
    "group":"background"
  }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name":"osm",
    "group":"background",
    "visibility": True
  }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name":"naip",
    "group":"background",
    "visibility": False
  }, {
    "source": {"ptype": "gxp_bingsource"},
    "name": "AerialWithLabels",
    "fixed": True,
    "visibility": False,
    "group":"background"
  },{
    "source": {"ptype": "gxp_mapboxsource"},
  }
]


# Default preview library
LAYER_PREVIEW_LIBRARY = 'geoext'


GEOS_LIBRARY_PATH = r'__geonodedir__/venv/Lib/site-packages/osgeo/geos.dll'


# #DJANGO DATA CLASSIFICATION BAR
# CLASSIFCATION_BANNER_ENABLED = True
# CLASSIFICATION_TEXT = 'Unclassified//FOUO'
# CLASSIFICATION_TEXT_COLOR = 'black'
# CLASSIFICATION_BACKGROUND_COLOR = 'green'


## Run pip install -r requirements.txt in geonode/scripts/ldap_auth
## uncomment and adjust to your settings

##import ldap
##from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
##
##
### Baseline configuration.
##AUTH_LDAP_SERVER_URI = "ldap://testad.localhost:389"
##
##AUTH_LDAP_BIND_DN = "CN=test1,OU=Users,OU=EDIP,DC=testad,DC=localhost"
##AUTH_LDAP_BIND_PASSWORD = "password"
##
##AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=Users,OU=EDIP,DC=testad,DC=localhost",
##    ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
### or perhaps:
### AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"
##
### Set up the basic group parameters.
##AUTH_LDAP_GROUP_SEARCH = LDAPSearch("OU=Security Group,OU=EDIP,DC=testad,DC=localhost",
##    ldap.SCOPE_SUBTREE, "(objectClass=group)"
##)
##AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="CN")
##
### Simple group restrictions
###AUTH_LDAP_REQUIRE_GROUP = "CN=Domain Users,CN=Users,DC=testad,DC=localhost"
##AUTH_LDAP_REQUIRE_GROUP = None
###AUTH_LDAP_DENY_GROUP = "CN=Not,DC=testad,DC=localhost"
##AUTH_LDAP_DENY_GROUP = None
##
### Populate the Django user from the LDAP directory.
##AUTH_LDAP_USER_ATTR_MAP = {
##    "first_name": "givenName",
##    "last_name": "sn",
##    "email": "mail"
##}
##
##AUTH_LDAP_PROFILE_ATTR_MAP = {
##    "first_name": "givenName"
##}
##
###If this resolved to true it would add a flag to the profile.
##AUTH_LDAP_USER_FLAGS_BY_GROUP = {
##    #"is_active": "CN=Users,DC=testad,DC=localhost",
##}
##
##AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
##   #"is_awesome": "cn=awesome,ou=django,ou=groups,dc=example,dc=com",
##}
##
### This is the default, but I like to be explicit.
##AUTH_LDAP_ALWAYS_UPDATE_USER = True
##
### Use LDAP group membership to calculate group permissions.
##AUTH_LDAP_FIND_GROUP_PERMS = True
##
### Cache group memberships for an hour to minimize LDAP traffic
##AUTH_LDAP_CACHE_GROUPS = True
##AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600
##
##AUTH_LDAP_MIRROR_GROUPS = True
##
##
### Keep ModelBackend around for per-user permissions and maybe a local
### superuser.
##AUTHENTICATION_BACKENDS = (
##    'django_auth_ldap.backend.LDAPBackend',
##    'django.contrib.auth.backends.ModelBackend',
##    'guardian.backends.ObjectPermissionBackend',
##    #'django.contrib.auth.backends.RemoteUserBackend',
##)

AUTH_PROFILE_MODULE = False



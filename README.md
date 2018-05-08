Django HTTP Basic Authentication Backend
========================================

Description
-----------

This module provides the client side for a HTTP Basic Authentication provider
to allow authentication for a Django application. It must be installed as a
Django authentication backend.

This allows to authenticate your Django application with the help of a web
server that already provides HTTP Basic Authentication, as it is described in
[RFC2617](https://www.ietf.org/rfc/rfc2617.txt). Web servers, such as Apache
or Nginx, can easily be configured to adapt complex authentication scenarios,
e.g. authentication via a combination of LDAP and manual filters. Your Django
project is now able to utilize such a configuration.

Installation
------------

Add this module to your `setup.py` and/or to `requirements.txt` file:

    # ...
    django-auth-http-basic
    # ...

You need at least Django >= 1.10.

Configuration
-------------

In your `settings.py` file, you must add/set the variable
`AUTHENTICATION_BACKENDS` so that it includes the authentication backend, e.g.:

    AUTHENTICATION_BACKENDS = ['django_auth_http_basic.HttpBasicAuthBackend']

In addition, you must specify an URL that provides HTTP Basic Authentication by
providing a value for the variable `HTTP_BASIC_AUTH_URL` in your `settings.py`
file, e.g.:

    HTTP_BASIC_AUTH_URL = 'https://example.com/auth'

As long as the web services conforms to HTTP Basic Authentication, it could be
used as an authentication backend. Since HTTP Basic Authentication transports
user name and password in clear text, you should access it via HTTPS. If the
web server is on your local host, you might use unencrypted HTTP.

The web server is expected to return a 401 response, if no user name and/or
no password is provided. It must return a 2xx response if the user is
authenticated, and a 403 response if the user is not authenticated. Currently,
every response code except 2xx will be interpreted as a failed authentication.
Most web servers conform to this rule. However, you are free to implement your
own authenticating web server.

For testing purposes, `HTTP_BASIC_AUTH_URL` can be set to `None`. In this case
no web server will be contacted, every user will be authenticated. Please be
sure to change `HTTP_BASIC_AUTH_URL` to a valid URL for production code.

If you don't set the variable `HTTP_BASIC_AUTH_URL` to any value, no user will
be authenticated. In this case, an error message will be sent to the logger
named `django-auth-http-basic`.

Another (optional) variable you can use in your `settings.py` is
`HTTP_BASIC_AUTH_CASE`. This value specifies, whether the user name will be
handled case-sensitive or case-insensitive in the backend. Its value itself
is treated case-insensive. Only its first letter is analysed. If it is a '0',
'f' or 'n', then the user name will be folded to lower-case. If you omit this
variable, a value 'yes' is assumed.

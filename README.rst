=======
HEADEGG
=======

HeadEgg is a stupid module.


Install HeadEgg
===============

``pip install django-headegg``

::

    MIDDLEWARE_CLASSES += ('headegg.middleware.HeadEgg',)


Configure HeadEgg
=================

::

    HEADEGG_QUOTES = (
        ('Ralph', "Me fail English? That's unpossible!"),
        ('Burns', 'Ahoy-hoy!'),
        ('Bart', 'So I says to Mabel, I says...'),
    )


Use HeadEgg
===========

::

    $ curl -Is http://example.com/
    HTTP/1.1 200 OK
    ...
    X-Ralph: Me fail English? That's unpossible!
    ...


Bugs, Features, Pull Requests?
==============================

http://github.com/jsocol/django-headegg


License
=======

BSD, see `LICENSE <LICENSE>`_.

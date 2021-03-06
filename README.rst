Ptah Examples
=============

You can read the `Examples` documentation on-line at 
`http://ptah-examples.readthedocs.org <http://ptah-examples.readthedocs.org/en/latest/index.html>`_.

This git repository contains self-contained WSGI applications which demonstrate various aspects of the pyramid-based Ptah environment. This repository contains:

* ``ptah_models`` - 2 form examples, homepage, management ui

* ``ptah_simpleauth`` - 2 form examples, homepage, management ui, auth and user source 

* ``ptah_minicms`` - a hierarchical cms supporting local roles, management ui, auth/user source, actions, layout preview and File, Page and Folder content types. 

* ``ptah_chat`` - a realtime websocket chat application using pyramid_sockjs wtih gevent and ptah_crowd.

* ``simple`` - 1 file module examples which demonstrate various ptah features.

All of these examples can be used in conjunction with ``ptah_crowd`` which provides more features.  Some ``ptah_crowd`` features include user management, registration, reset password.  You can find ``ptah_crowd`` in the ptahproject github.

Quick start
-----------

See ``ptah`` README or ``pyramid`` README on how to create virtualenv.  Once you have a virtualenv you can follow this guide.  If you havent installed ptah.  Install it with easy_install or pip::

  $ cd path/to/virtualenv
  $ bin/easy_install ptah

NOTE: on Windows bin/easy_install will be Scripts/easy_install

Once you have ptah installed you can run these examples.

  $ git clone git://github.com/ptahproject/examples.git
  $ cd examples

Pick which WSGI application you like, lets pick ptah_models.  We need to install the package into our development environment::

  $ cd ptah_models
  $ path/to/virtualenv/bin/python setup.py develop

Now we start it up.  --reload is optional.  If you edit a Python file the WSGI server will restart::

  $ path/to/virtualenv/bin/pserve settings.ini --reload

Goto http://localhost:6543/ and you can read and experiment.  Look at http://ptahproject.readthedocs.org/en/latest/index.html for latest Ptah documentation.

You can find support on irc.freenode.net on #ptahproject or #pyramid

Troubleshooting
---------------

If you run into a problem with the examples you get further by using the source checkout.

As of Jan. 11. 2012 the examples require `master` of ptah and ptah_crowd until 0.3 of those packages are released.

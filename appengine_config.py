#!/usr/bin/env python
# -*- indent-tabs-mode: nil; tab-width: 4; coding: utf-8 -*-
# vi: set ts=4 sts=4 sw=4 set smarttab set expandtab

def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app

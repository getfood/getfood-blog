# -*- coding: utf-8 -*-
# Django settings for the example project.
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = '=r-$b*8hgw3sc58&9t0twan5ch1k-3d3vf'
##LANGUAGE_CODE = 'zh-CN'
##LANGUAGE_CODE = 'fr'
LOCALE_PATHS = 'locale'
USE_I18N = True

TEMPLATE_LOADERS=('django.template.loaders.filesystem.Loader',
                    'ziploader.zip_loader.load_template_source')

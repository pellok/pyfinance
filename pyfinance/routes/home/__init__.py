from __future__ import unicode_literals

from . import view

def includeme(config):
    config.add_route('page.home', '/')
    config.add_view(
        view.HomeViews, attr='home',
        route_name='page.home',
        renderer='templates/home.mako',
    )

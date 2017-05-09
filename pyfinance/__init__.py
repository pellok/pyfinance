from pyramid.config import Configurator
from .request import WebRequest


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
                          request_factory=WebRequest)
    config.include('pyramid_mako')

    config.include('.routes')

    config.add_static_view('pyfinance', 'static', cache_max_age=3600)

    config.scan()

    return config.make_wsgi_app()

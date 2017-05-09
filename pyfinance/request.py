# coding=utf-8
from __future__ import unicode_literals

from pyramid.decorator import reify
from pyramid.events import NewRequest, subscriber
from pyramid.request import Request

class WebRequest(Request):
    @reify
    def route_name(self):
        """Return route name if available, otherwise None is returned."""
        return self.matched_route.name if self.matched_route else None

    @reify
    def real_ip(self):
        """The real IP address from x-forwarded-for, or x-real-ip,
            mainly depends on configuration."""
        addresses = self.headers.get('X-Forwarded-For')
        if addresses:
            parts = addresses.split(',')
            return parts[0].strip()
        else:
            return self.remote_addr

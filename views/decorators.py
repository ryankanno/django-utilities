#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from functools import wraps

def render(template=None, mimetype=None):
    def renderer(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            out = func(request, *args, **kwargs)
            if not isinstance(out, dict):
                return out
            # Define a template dynamically in the decorator call
            template = out.pop('TEMPLATE', template)
            return render_to_response(template, out,
                   context_instance=RequestContext(request), mimetype=mimetype)
        return wrapper
    return renderer

# vim: filetype=python

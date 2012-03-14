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
            
            if template and out.pop('TEMPLATE'):
                raise Exception, "Naughty, naughty.  You've declared a template within the decorator and function." 

            # Define a template dynamically in the decorated call
            tmpl_to_render = template or out.pop('TEMPLATE', None)

            # If it's still null, try to do the right thing
            if not tmpl_to_render:
                tmpl_to_render = "%s/%s.html" % (func.__module__.split('.')[k], func.__name__)

            return render_to_response(tmpl_to_render, out,
                   context_instance=RequestContext(request), mimetype=mimetype)
        return wrapper
    return renderer

# vim: filetype=python

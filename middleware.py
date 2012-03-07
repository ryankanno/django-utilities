# See: http://blog.isotoma.com/2009/12/getting-the-name-of-the-current-view-in-a-django-template/comment-page-1/#comment-884

class ModuleViewMiddleware(object):  
    def process_view(self, request, view_func, view_args, view_kwargs):  
        setattr(request, 'module_name', getattr(view_func, '__module__', ''))
        setattr(request, 'view_name', getattr(view_func, '__name__', ''))

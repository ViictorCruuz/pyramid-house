from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'projects'}


@view_config(route_name='victor', renderer='templates/victor.jinja2')
def victor(request):
    return {'project': 'project'}


@view_config(route_name='other', renderer='templates/other.jinja2')
def other(request):
    text = 'Welcome to my new site!!!'
    tit = 'New Site :)'
    return {'text': text, 'tit': tit}


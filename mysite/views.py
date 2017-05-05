from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.template import Template
from django.shortcuts import render_to_response
def current_time(request):
    time = datetime.datetime.now()
    #html = u'<html><body>It is %s now</body></html>' % time
    t = get_template(u'test.html')
    html = t.render(Context({u'current': time}))
    return render_to_response(u'test.html', {u'current': time})
#    return HttpResponse(html)

def hours_head(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = u'<html><body>In %s hours, it will be %s</body></html>' % (offset, dt)

    return HttpResponse(html)

if __name__=='__main__':
    import sys
    print sys.path
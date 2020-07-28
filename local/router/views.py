from linebot.exceptions import InvalidSignatureError
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import sys
sys.path.append('function/')

from example import *


@csrf_exempt
def webhook_handler(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode()
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return HttpResponse('ok')

    return HttpResponse('ok')

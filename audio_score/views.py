from rest_framework.decorators import api_view

from shared.rest import success


@api_view(['GET'])
def r_ping(req):
    return success('pong')

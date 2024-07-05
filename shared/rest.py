from rest_framework.response import Response

RESP_CODE_OK = 200
RESP_CODE_COMMON = 1000


def success(data=None):
    if data is None:
        return Response({"code": RESP_CODE_OK})
    return Response({"code": RESP_CODE_OK, "data": data})


def fail(msg: str, code=RESP_CODE_COMMON):
    return Response({"code": code, "data": msg})

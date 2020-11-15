from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handle_styles(_request: RequestT) -> ResponseT:
    payload = read_static("style.css")
    status = "200 OK"
    headers = {"Content-type": "text/css"}

    return status, headers, payload


def handle_style():
    return None

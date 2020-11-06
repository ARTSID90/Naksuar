from framework.types import RequestT
from framework.types import ResponsenT
from framework.utils import read_static


def handle_space(_request: RequestT) -> ResponsenT:
    payload = read_static("space.png")
    status = "200 OK"
    headers = {"Content-type": "image/png"}

    return ResponsenT(status, headers, payload)

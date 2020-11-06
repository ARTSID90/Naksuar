from framework.types import RequestT
from framework.types import ResponsenT
from framework.utils import build_status
from framework.utils import read_static


def handle_index(_request: RequestT) -> ResponsenT:
    base = read_static("_base.html")
    base_html = base.content.decode()
    index_html = read_static("index.html").content.decode()

    result = base_html.format(xxx=index_html)
    result = result.encode()

    status = build_status(200)
    headers = {
        "Content-type": base.content_type,
    }

    return ResponsenT(
        headers=headers,
        payload=result,
        status=status,
    )

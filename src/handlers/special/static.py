from framework.types import RequestT
from framework.types import ResponsenT
from framework.utils import build_status
from framework.utils import read_static


def handle_static(request: RequestT) -> ResponsenT:
    file_name = request.kwargs["file_name"]

    static = read_static(file_name)
    status = build_status(200)

    return ResponsenT(
        headers={"Content-Type": static.content_type},
        payload=static.content,
        status=status,
    )

import mimetypes

from framework.consts import dir_static


def application(environ, start_response):
    url = environ["PATH_INFO"]

    file_names = {"/xxx": "styles.css", "/space.jpg/": "space.jpg"}

    file_name = file_names.get(url, "index.html")

    status = "200 OK"
    headers = {"Content-type": mimetypes.MimeTypes().guess_type(file_name)[0]}
    payload = read_static(file_name)
    start_response(status, list(headers.items()))
    yield payload

def read_static(file_name: str) -> bytes:
    path = dir_static / file_name
    with path.open("rb") as fp:
        payload = fp.read()
    return payload
from framework.consts import dir_static


def application(environ, start_response):
    url = environ["PATH_INFO"]
    if url == "/xxx/":
        status = "200 OK"
        headers = {
            "Content-type": "text/css",
        }
        payload = read_from_style_css()
        start_response(status, list(headers.items()))

        yield payload
    else:
        status = "200 OK"
        headers = {
            "Content-type": "text/html",
        }
        payload = read_from_index_html()

        start_response(status, list(headers.items()))

        yield payload


def read_from_index_html():
    path = dir_static / "index.html"
    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload


def read_from_style_css():
    path = dir_static / "style.css"
    with path.open("r") as fp:
        payload = fp.read()

    payload = payload.encode()
    return payload

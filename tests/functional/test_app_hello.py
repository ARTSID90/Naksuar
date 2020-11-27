import pytest

from tests.functional.pages.hello import HelloPage
from tests.functional.utils import screenshot_on_failure
from tests.functional.utils import validate_redirect

url = "http://localhost:8000/h/"


@pytest.mark.functional
@screenshot_on_failure
def test(browser, _request):
    page = HelloPage(browser, url)

    assert page.greeting.text == "Hello"
    assert page.address.text == "You are in her"

    page.name_input.clear()
    page.address_input.clear()
    page.name_input.send_keys("Naksuar")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello Naksuar"
    assert page.address.text == "You are in her"
    assert page.name_input.get_attribute("value") == "Naksuar"

    page.name_input.clear()
    page.address_input.clear()
    page.address_input.send_keys("localhost")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello"
    assert page.address.text == "You are in localhost"
    assert page.address_input.get_attribute("value") == "localhost"

    page.name_input.clear()
    page.address_input.clear()
    page.name_input.send_keys("Naksuar")
    page.address_input.send_keys("localhost")
    page.submit_button.click()
    validate_redirect(page, url)
    assert page.greeting.text == "Hello Naksuar"
    assert page.address.text == "You are in localhost"
    assert page.name_input.get_attribute("value") == "Naksuar"
    assert page.address_input.get_attribute("value") == "localhost"

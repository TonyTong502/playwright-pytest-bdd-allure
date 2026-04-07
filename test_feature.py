import datetime
import re
import allure

from playwright.sync_api import Page, expect
import pytest
from pytest_bdd import given, parsers, scenarios, then, when


scenarios('homepage.feature')

@pytest.fixture(scope='session')
def file_info():
    return {"file_name": "", "file_content": ""}

@given(parsers.parse('pre-proccessed file name: {file_name} and file content: {file_content}'))
def _(file_info, file_name: str, file_content: str):
    datetime_text_in_YYYYMMDD_HHMM = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    file_info["file_name"] = file_name.replace('{YYYYMMDD_HHMM}', datetime_text_in_YYYYMMDD_HHMM)
    file_info["file_content"] = file_content.replace('{YYYYMMDD_HHMM}', datetime_text_in_YYYYMMDD_HHMM)
    print('file name from given:', file_info["file_name"])
    print('file content from given:', file_info["file_content"])

@when("the user goes to Playwright homepage")
def _(request, file_info):
    print('file name from when:', file_info["file_name"])
    page = request.getfixturevalue("page")
    page.goto("https://playwright.dev/")
    allure.attach(page.screenshot(), name="my-image-from-step", attachment_type=allure.attachment_type.PNG)

@then("the user should expect the title to contain Playwright")
def _(request, file_info):
    print('file name from then:', file_info["file_name"])
    # Expect a title "to contain" a substring.
    page = request.getfixturevalue("page")
    expect(page).to_have_title(re.compile("Playwright"))
    page.set_content(f"hello!!")

@then("file name should be not empty")
def _(file_info):
    assert file_info["file_name"], "File name is empty"
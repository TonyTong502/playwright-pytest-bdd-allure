import pytest
import allure

from playwright.sync_api import Page

# counter = 0
# screenshots = []

# automated screenshot capture for success step
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    print(f"After step: {step.name}")
    if not any(fixture in ['page', 'browser', 'context', 'request'] for fixture in step_func_args):
        return
    if 'page' in request.fixturenames:
        page: Page = request.getfixturevalue("page")
        print(f"Attaching screenshot for step: {step.name}")
        allure.attach(page.screenshot(), name=f"Screenshot on Success: {step.keyword} {step.name}", attachment_type=allure.attachment_type.PNG)
        # page.screenshot(path=f"allure-results/{feature.name}_{scenario.name}_{step.name}.png")

# automated screenshot capture for failed step
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f"Step error: {step.name} - {exception}")
    if 'page' in request.fixturenames:
        page: Page = request.getfixturevalue("page")
        print(f"Attaching screenshot for failed step: {step.name}")
        allure.attach(page.screenshot(), name=f"Screenshot on Failure: {step.keyword} {step.name}", attachment_type=allure.attachment_type.PNG)

# # # @pytest.hookimpl(hookwrapper=True)
# # # def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
# # #     yield
# # #     if 'page' in step_func_args:
# # #         page = step_func_args.get("page")
# # #         if page:
# # #             # # Attach screenshot from bytes
# # #             screenshot_bytes = page.screenshot()
# # #             attach.screenshot(screenshot_bytes, feature.name, scenario.name) # pytest-bdd-report code to attach the screenshot

# # #             # Attach screenshot from image path
# # #             # screenshot_path = "screenshot_path/test.png"
# # #             # page.screenshot(path=screenshot_path)

# # #             # attach.screenshot(screenshot_path, feature.name, scenario.name) # pytest-bdd-report code to attach the screenshot
import pytest
from selene.support.shared import browser

@pytest.fixture(scope='function',autouse=True)
def clear_history():
    yield
    browser.quit()

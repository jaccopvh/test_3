import pytest
import pytest_selenium
from selenium import webdriver

retcode = pytest.main()
print(str(retcode))
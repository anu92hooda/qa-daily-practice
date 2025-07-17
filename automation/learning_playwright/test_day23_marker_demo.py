import pytest
from playwright.sync_api import sync_playwright, expect,Page

@pytest.mark.sanity
@pytest.mark.regression
def test_first():
    print("i am sanity and regression")


@pytest.mark.sanity
def test_second():

    print(" i am sanity")

@pytest.mark.regression
def test_third():

    print("i am regression")

def test_fourth():

    print("i have no tag")

@pytest.mark.sanity
@pytest.mark.smoke
def test_fifth():
    print("i am sanity and smoke ")
















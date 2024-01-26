from selenium import webdriver
import requests
import io
from dataclasses import dataclass
import sqlite3
from selenium.webdriver.chrome.options import Options

wd = webdriver.Chrome()

JOB_TYPES = ["full-time", "part-time", "contract", "temporary"]
JOB_LEVELS = ["entry", "intermediate", "senior", "internship"]
JOB_STYLE = ["remote", "hybrid", "onsite"]


@dataclass
class LoginUser:
    username: str
    password: str
    fname: str
    lname: str
    resume: str = ""


class JobFilters:
    title: str
    loc: str
    job_type: str
    level: str
    pay_thresh: int


"""
Need to get paths for forms (based off resume): selenium + model
Need to make dummy account with resumes: selenium
Need to fill form: selenium
Need to get data to fill form: model
Need to apply with form: selenium

"""
# test_user = LoginUser()



def sign_in(url, user: LoginUser):
    pass


def fill_form(url):
    pass


class LinkedInApplier:
    PATH_BASE = "https://ca.linkedin.com/jobs/"
    def __init__(self, user):
        self.user = user


def main():
    title = "software-engineering"
    PATH_BASE = "https://ca.linkedin.com/jobs/"
    PATH = PATH_BASE + f"{title}-jobs"
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    # chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("incognito")
    wd = webdriver.Chrome(options=chrome_options)
    links = ""
    print(links)
    wd.quit()
    wd.get(PATH)

if __name__ == "__main__":
    main()



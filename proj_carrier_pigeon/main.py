import requests
import os
import time
import argparse
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

"""
Need Two Parameters:

1. Cohort ID
2. Project Name (to find li for and to get due date from airtable)
"""

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def get_page_with_driver(url: str):
    """
    using the chrome webdriver, access the `url` using webdriver.Chrome().get(`url`)

    :param url -> ``str``: the base url to open in chrome.
    """
    driver.get(url)

    return driver


def authenticate():
    """authenticate using the chrome web driver."""
    email_input = driver.find_element_by_id("email")
    email_input.send_keys("dan@pathstream.com")
    password_input = driver.find_element_by_id("password")
    password_input.send_keys(os.environ.get("USER_PW"))
    password_input.send_keys(Keys.RETURN)


def find_cohort_button_for_correct_course(cohort_id: str):
    """
    Using the Chrome webdriver instance and cohort id, find the correct cohort button

    :param cohort_id -> ``str``: the ID of the cohort.
    """
    view_cohort_button_for_correct_course = wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         f"//a[contains(@href, '/coach/dashboard/cohorts/{cohort_id}')]")
    ))

    view_cohort_button_for_correct_course.click()


def click_assignments_tab():
    assignments_tab = wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//span[contains(.,'Assignments')]")
    ))

    assignments_tab.click()


def find_and_click_correct_child(project_name: str):
    """
    find the correct list item whose text is equal to `project_name` and click it.

    :param project_name -> str: the name of the project.
    """
    root_ul = driver.find_element_by_xpath(
        "//div[@id='root']/div/div/div/section/main/section/aside/div/ul")
    all_lis = root_ul.find_elements_by_tag_name("li")

    li_names = [li.text for li in all_lis]

    # need the name of the project/test
    ul_child_n = li_names.index(project_name) + 1  # zero-indexing, so add one

    tab_for_correct_assignment_name = driver.find_element_by_xpath(
        f"//li[{ul_child_n}]/div")
    tab_for_correct_assignment_name.click()


def set_and_save_due_date():
    set_due_date_btn = driver.find_element_by_xpath(
        "//button[contains(.,'Set due date')]")
    set_due_date_btn.click()  # enter set due date modal / popup

    input_elem = driver.find_element_by_xpath("//input")
    input_elem.click()  # click input tag
    time.sleep(1)
    # input custom date (this needs to be pulled from airtable later)
    input_elem.send_keys("2021-12-17 12:30:10")
    time.sleep(1)
    submit_due_date_btn = driver.find_element_by_xpath(
        "//button[contains(.,'Ok')]")  # submit the date, click button to submit save
    submit_due_date_btn.click()

    save_due_date_btn = driver.find_element_by_xpath(
        "//button[contains(.,'Save')]")
    save_due_date_btn.click()


if __name__ == "__main__":
    base_parser = argparse.ArgumentParser(
        description="Simple command-line tool for running the script with the needed inputs",
        formatter_class=argparse.RawTextHelpFormatter
    )

    base_parser.add_argument(
        "--cohort_id",
        type=str,
        nargs="?",
        help="The ID for the cohort."
    )

    base_parser.add_argument(
        "--project_info",
        type=str,
        nargs="?",
        help="The Course and Project Name"
    )

    args = base_parser.parse_args()

    cohort_id = args.cohort_id
    jsonified_project_info = json.loads(args.project_info)

    print(cohort_id, jsonified_project_info)

    driver = get_page_with_driver("https://qa2.pathstream.com/coach/dashboard")
    authenticate()
    find_cohort_button_for_correct_course(cohort_id)
    click_assignments_tab()
    find_and_click_correct_child(jsonified_project_info['project_name'])
    set_and_save_due_date()
    driver.close()
import requests
import os
import time
import argparse
import json
import datetime

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

# TODO: read in date from Airtable based on course + project name, use that date to set the due date in Pathstream admin.

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def convert_to_linked_name(cell_id: str, project_name):
    headers = {
        "Authorization": os.environ.get("AIRTABLE_BEARER_KEY"),
        "Accept": "application/json",
    }

    response = requests.get(
        f"https://api.airtable.com/v0/appBRLEUdTlfhgkUZ/Courses/{cell_id}", headers=headers)

    response.raise_for_status()

    return response.json()['fields']['Course Name']


def get_due_date_from_airtable(course_name: str, project_name: str):
    """
    Get the correct due date for a project with the provided `course_name` and `project_name`

    :param course_name -> ``str``: the name of the course (ID)
    :param project_name -> ``str``: the name of the project
    """
    headers = {
        "Authorization": os.environ.get("AIRTABLE_BEARER_KEY"),
        "Accept": "application/json",
    }

    response = requests.get(
        f"https://api.airtable.com/v0/appBRLEUdTlfhgkUZ/Projects?fields%5B%5D=Course&fields%5B%5D=Project%20Name&fields%5B%5D=Due%20Date&fields%5B%5D=Start%20Date", headers=headers)

    response.raise_for_status()

    jsonified_res = response.json()
    records = jsonified_res['records']
    for record in records:
        course_reference = record['fields']['Course']
        project_reference = record['fields']['Project Name']
        due_date = record['fields']['Due Date']
        
        linked_course_name = convert_to_linked_name(
            course_reference[0], project_name)

        print("START")
        print(linked_course_name)
        print(course_name[0])
        print(project_reference)
        print(project_name)
        print("\n")

        if linked_course_name == course_name[0] and project_reference == project_name:
            print("Here")
            print(due_date, record['fields']['Start Date'], datetime.datetime.strptime(record['fields']['Start Date'], "%Y-%m-%d") + datetime.timedelta(weeks=due_date))
            return datetime.datetime.strptime(record['fields']['Start Date'], "%Y-%m-%d") + datetime.timedelta(weeks=due_date)


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


def find_cohort_button_for_correct_course(cohort_name: str):
    """
    Using the Chrome webdriver instance and cohort id, find the correct cohort button

    :param cohort_name -> ``str``: the name of the cohort.
    """
    time.sleep(5)
    div_for_correct_course = driver.find_elements_by_xpath("//div[@class='cohort-group']")

    parent_div_with_button = [(i, elem) for i, elem in enumerate(div_for_correct_course) if elem.text.split('\n')[0] == cohort_name][0]

    all_buttons = parent_div_with_button[1].find_elements_by_xpath("//span[contains(.,'View cohort')]")
    button = all_buttons[parent_div_with_button[0]]

    button.click()


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


def set_and_save_due_date(due_date_and_time: datetime.datetime):
    set_due_date_btn = driver.find_element_by_xpath(
        "//button[contains(.,'Set due date')]")
    set_due_date_btn.click()  # enter set due date modal / popup

    input_elem = driver.find_element_by_xpath("//input")
    input_elem.click()  # click input tag
    time.sleep(1)
    # input custom date (this needs to be pulled from airtable later)
    input_elem.send_keys(due_date_and_time.strftime("%Y-%m-%d 00:00:00"))
    time.sleep(1)
    submit_due_date_btn = driver.find_element_by_xpath(
        "//button[contains(.,'Ok')]")  # submit the date, click button to submit save
    submit_due_date_btn.click()

    save_due_date_btn = driver.find_element_by_xpath(
        "//button[contains(.,'Save')]")
    save_due_date_btn.click()


def get_brightspace_and_project_name_from_airtable():
    headers = {
        "Authorization": os.environ.get("AIRTABLE_BEARER_KEY"),
        "Accept": "application/json",
    }

    course_sections_response = requests.get(
        f"https://api.airtable.com/v0/appBRLEUdTlfhgkUZ/Course%20Sections?view=Course%20Section%20Creation%20Script", headers=headers)

    projects_response = requests.get(
        f"https://api.airtable.com/v0/appBRLEUdTlfhgkUZ/Projects", headers=headers)

    course_sections_response.raise_for_status()
    projects_response.raise_for_status()

    jsonified_response = course_sections_response.json()['records']
    tuple_of_names_and_projects = [(row['fields']['Brightspace Name'], row['fields']
                                    ['Projects (from Course Version) (from Cohort Course Name)']) for row in jsonified_response]
    projects_ids = [row[1] for row in tuple_of_names_and_projects]
    flattened_proj_ids = [proj_id for proj_ids in projects_ids for proj_id in proj_ids]
    print(flattened_proj_ids)

    jsonified_projects_res = projects_response.json()['records']
    # return [row['fields']['Project Name'] for row in jsonified_projects_res if row['id'] in projects_ids]
    return [row['fields'] for row in jsonified_projects_res if row['id'] in flattened_proj_ids]


if __name__ == "__main__":
    all_brightspace_and_project_names = get_brightspace_and_project_name_from_airtable()
    print(all_brightspace_and_project_names)
    first_brightspace_name = get_brightspace_and_project_name_from_airtable()[0]
    print(first_brightspace_name)

    args = {
        "project_info": {
            "course_name": first_brightspace_name.get('Course Name (from Course)', False),
            "project_name": first_brightspace_name.get('Project Name', False)
        }
    }
    print(args)

    jsonified_project_info = json.loads(json.dumps(args["project_info"]))

    due_date_and_time = get_due_date_from_airtable(
        jsonified_project_info['course_name'], jsonified_project_info['project_name'])

    driver = get_page_with_driver("https://qa2.pathstream.com/coach/dashboard")
    authenticate()
    find_cohort_button_for_correct_course(jsonified_project_info['course_name'])
    click_assignments_tab()
    find_and_click_correct_child(jsonified_project_info['project_name'])
    set_and_save_due_date(due_date_and_time)
    driver.close()

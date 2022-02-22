from selenium.webdriver.common.by import By
from behave import given, when, then

header = (By.CSS_SELECTOR, '.a-section h1')
do_here_links = (By.CSS_SELECTOR, '.a-column.a-span4')
search_field = (By.ID, 'helpsearch')
topics_links = (By.CSS_SELECTOR, '.csg-category')
images = (By.CSS_SELECTOR, '.csg-hb-promo')

@then('verify there is a header')
def verify_header(context):
    actual_header = context.driver.find_element(*header)
    print("The header of the page is 'Hello. What can we help you with?'")


@then('verify there is {expected_links} different link under the header')
def verify_links(context, expected_links):
    links_amount = len(context.driver.find_elements(*do_here_links))
    assert links_amount == int(expected_links), f"Expected count {expected_links} but got {links_amount}"


@then('verify there is a search field')
def verify_search_field(context):
    search = context.driver.find_element(*search_field)
    print("There is a search field")


@then('verify there is a list of {expected_topics} topics under topics header')
def verify_list_topics(context, expected_topics):
    topic_amount = len(context.driver.find_elements(*topics_links))
    assert topic_amount == int(expected_topics), f"Expected link count {expected_topics} but got {topic_amount}"


@then('verify there are {expected_images_count} images changes according to the topics ,in bottom right corner')
def verify_image(context, expected_images_count):
    image_cont = len(context.driver.find_elements(*images))
    assert image_cont == int(expected_images_count), f"Expected image count {expected_images_count} but got {image_cont}"

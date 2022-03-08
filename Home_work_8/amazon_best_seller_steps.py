from selenium.webdriver.common.by import By
from behave import given, when, then

best_seller_links = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')
best_seller_five_links = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')
LINKS_HEADER_TEXT = (By.ID, 'zg_banner_text')

@given('Open Amazon best seller page')
def open_best_seller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify user can see {expected_amount} links in best seller page')
def verify_best_seller_links(context, expected_amount):
    best_seller_amount = len(context.driver.find_elements(*best_seller_links))
    assert best_seller_amount == int(expected_amount), f"expected 5 links but got {best_seller_amount}"


@then('Verify that correct page opens when user go through all the best seller links')
def verify_page(context):
    b_s_links = context.driver.find_elements(*best_seller_five_links) # [l_1, l_2, l_3, l_4, l_5]
    for li in range(0, len(b_s_links)):

        links = context.driver.find_elements(*best_seller_five_links)[li]
        links_text = links.text # first store the text.
        links.click() # then click on the links

        links_header_text = context.driver.find_element(*LINKS_HEADER_TEXT).text
        assert links_text in links_header_text, f"expected {links_text} not in {links_header_text}."

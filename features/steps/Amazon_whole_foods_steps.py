from selenium import webdriver
from behave import when, then
from selenium.webdriver.common.by import By


Product_texts = (By.CSS_SELECTOR, '.s-result-item .wfm-sales-item-card__regular-price')
Product_names = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')


@when('Open Amazon Wholefoods page')
def open_wholefoods_page(context):
    context.driver.get(' https://www.amazon.com/wholefoodsdeals')


@then('Verify that every product on the Wholefoods page has a text ‘Regular’and  its product name.')
def verify_text(context):
    all_text_elements = context.driver.find_elements(*Product_texts)
    i = 0
    for ele in all_text_elements:
        assert 'Regular' in ele.text, f"Expected Regular in element but got {ele.text}"
        products_name = context.driver.find_elements(*Product_names)[i].text
        i = i + 1
        print(ele.text)
        print("all product name= ", products_name)
        assert products_name, f"expected there should a product name but got {products_name}"








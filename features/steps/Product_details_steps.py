from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
current_colors_text = (By.CSS_SELECTOR, '#variation_color_name .selection')
COLOR_OPTIONS_for_Stretch_Jean = (By.CSS_SELECTOR, "#variation_color_name li")
current_colors_text_for_Stretch_Jean = (By.CSS_SELECTOR, '#variation_color_name .selection')


@when('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.app.main_page.open_amazon_product_page(product_id)


@when('hovers over New Arrivals')
def hover_new_arrivals(context):
    context.app.search_product_page.hover_new_arrival()


@then('Verify user can click through colors')
def verify_color_click(context):
    expected_colors = ["Black", "Navy"]
    colors_option = context.driver.find_elements(*COLOR_OPTIONS) # [web_ele_1, web_ele_2] list of elements

    # option_1
    #actual_colors = []
    # for color in colors_option:
        #color.click()
        #current_colors_name = context.driver.find_element(*current_colors_text).text
        #actual_colors = actual_colors + [current_colors_name]

    #assert expected_colors == actual_colors, f"The actual color is: {expected_colors} and we got {actual_colors}"

    # option_2
    for color in range(len(colors_option)):
        colors_option[color].click()
        current_color_name = context.driver.find_element(*current_colors_text).text
        assert current_color_name == expected_colors[color], f"The actual color is: {expected_colors} and we got " \
                                                             f"{current_color_name}"


@then('Verify user can click through all the colors')
def verify_colors(context):
    expected_colors = ["Black", "Dark Blue Vintage", "Dark Indigo/Rinsed", "Dark Wash", "Indigo Wash",
                       "Light Blue Vintage", "Light Wash", "Medium Blue, Vintage", "Medium Wash"]

    color_option_for_stretch_jean = context.driver.find_elements(*COLOR_OPTIONS_for_Stretch_Jean)
    actual_colors_for_stretch_jean = []
    for i in range(0, 9):
        color_option_for_stretch_jean[i].click()
        current_color_name_for_stretch_jean = context.driver.find_element(*current_colors_text_for_Stretch_Jean).text
        actual_colors_for_stretch_jean += [current_color_name_for_stretch_jean]

        assert current_color_name_for_stretch_jean == expected_colors[i], f"The actual colors are: {expected_colors}"\
                                                                       f"but got {actual_colors_for_stretch_jean}"


@then('verifies user can see the deals of new arrival')
def verify_the_deals(context):
    context.app.search_product_page.verify_new_deals()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_service = Service(executable_path=r"C:\Users\MY-PC\Documents\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver.get("https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb")

driver.maximize_window()

# This goes to the webpage, inspects these elements and prints their corresponding values on the console
price_dollar = driver.find_element(By.XPATH,
value="/html/body/div[1]/div[18]/div/div/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/div[1]/span[2]/span[1]")
price_cent = driver.find_element(By.CLASS_NAME, value="fractionalValue--2JOgL")
dollar_sign = driver.find_element(By.CLASS_NAME, value="currencySymbolV2--4uJvJ")

print(f'The price is {dollar_sign.text}{price_dollar.text}.{price_cent.text}')
# print(price_dollar.size)
driver.quit()

# We can also find_elements element using css_selector, id, name, link_text, partial_link_text, tag_name, xpath


driver.get("https://www.python.org/")
# we are locating elements by css selector. '.shrubbery' is the div. class name while 'time' is the sub
# selector in the div
event_times = driver.find_elements(By.CSS_SELECTOR, value=".shrubbery time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".shrubbery li a")
events = {}

for i in range(len(event_times)):
    events[i] = {
        "Time": event_times[i].text,
        "Names": event_names[i].text
    }

print(events)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
article_count.click()
# print(article_count.text)

pages = driver.find_element(By.LINK_TEXT, value="Pages")
pages.click()

starting_page = driver.find_element(By.NAME, value="from")
starting_page.send_keys(1)

ending_page = driver.find_element(By.NAME, value="to")
ending_page.send_keys(30)

select_article = driver.find_element(By.CLASS_NAME, value="oo-ui-dropdownWidget-handle")
select_article.click()
article_type = driver.find_element(By.XPATH, value="/html/body/div[6]/div/div[5]")
article_type.click()

go_button = driver.find_element(By.XPATH, value='//*[@id="ooui-php-7"]/button')
go_button.click()

time.sleep(10)



from selenium import webdriver
import time

# chrome_driver_path = YOUR CHROME DRIVERPATH
# driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break



# Lindkedin job application Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# ACCOUNT_EMAIL = YOUR LOGIN EMAIL
# ACCOUNT_PASSWORD = YOUR LOGIN PASSWORD
# PHONE = YOUR PHONE NUMBER


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Click Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()




# EMAIL PROJECT
import smtplib

my_email = "ransomonwuka@gmail.com"
# this password is gotten from gmail app password
password = "qhhpqnimjnqjaarz"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # this makes the connection secure
    connection.starttls()
    # login
    connection.login(user=my_email, password=password)
    # send mail
    connection.sendmail(
        from_addr=my_email,
        to_addrs="onwukauchenna055@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email.")


import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
month = now.month
print(month)

date_of_birth = dt.datetime(year=1996, month=10, day=27)
print(date_of_birth)



import smtplib, random
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="onwukauchenna055@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}")



import datetime as dt
import pandas, random, smtplib

my_email = "ransomonwuka@gmail.com"
password = "brasxwlxlowxtxkj"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Reading csv file using pandas
data = pandas.read_csv("Birthday.csv")
# Iterating through the rows with the iterrows() method
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
# checking if today's date exists in the csv file
if today_tuple in birthday_dict:
    # Takes us to the line that matches today_tuple
    birthday_person = birthday_dict[today_tuple]
    # this goes to the file directory and scams the files at random
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # opens the file
    with open(file_path) as letter_file:
        # reads the file
        contents = letter_file.read()
        # replaces the name in the file with the actual birthday_persons name
        contents = contents.replace("[NAME]", birthday_person["NAME"])

    with smtplib.SMTP("smpt.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")




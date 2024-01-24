from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Select and connect to our choice of browser
CHROMEDRIVER_PATH = ".\chromedriver.exe"
OPTIONS = Options()
OPTIONS.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=OPTIONS)

# Open a website
driver.get("https://www.reddit.com/r/geopolitics/comments/17iionk/can_someone_explain_what_im_missing_in_the/")
# driver.maximize_window()

# Scroll down to the bottom a few times to load more comments
while True:
    print("Scrolling down...")
    
    # Scroll to the bottom of the page using JavaScript
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for a few moments (for things to load)
    driver.implicitly_wait(3)
    
    # If there is a load more button, click
    try:
        load_more_btn = driver.find_element("xpath", '//*[@id="comment-tree"]/faceplate-partial/div[1]/button')
        load_more_btn.click()
    except:
        break

# Get a list of replies
comments = []
replies = driver.find_elements("xpath", '//div[contains(@id, "post-rtjson-content")]')
for reply in replies:
    
    # Build the full comment from all </p> tags
    comment = ""
    p_tags = reply.find_elements(by="css selector", value='p')
    for p_tag in p_tags:
        comment += p_tag.text
    
    # Add comment to full list of comments
    comments.append(comment)

# Output comments
[print(comment + "\n") for comment in comments]
print("NUMBER OF COMMENTS SCRAPED:", len(comments))

# Store reply in mongo


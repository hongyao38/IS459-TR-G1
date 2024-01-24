## Selenium Demo
In this demo scraping script, we are scraping comments from Reddit.

The comments are scraped by their xpaths, and stored into a list of comments.
You can comment/uncomment the while-loop to see how Selenium can be used to interact with the browser to create a more sophisticated scraper.

Without the while-loop, we are scraping the comments from the initial HTML that is first loaded upon reaching the page.
However, more comments will only be loaded upon scrolling down, and clicking on the "Load More Comments" button.
With the loop, we can make use of Selenium to programmatically interact with the browser to automate the process of loading more comments.
Thus allowing us to scrape more comments.

## To run
pip install -r requirements.txt

python scraper.py
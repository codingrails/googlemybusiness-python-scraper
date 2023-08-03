# Script Documentation - Google Reviews Scraper

This script utilizes Selenium WebDriver and pandas to scrape Google reviews for specified URLs from an Excel file, save the data to a CSV file, and then perform some data matching operations.

## Prerequisites
1. Python with required dependencies installed (`selenium`, `pandas`, `regex`, `webdriver_manager.chrome`).
2. Chrome web browser.

## How to use
1. Install the required dependencies if you haven't already:
   ```bash
   pip install selenium pandas regex webdriver_manager
   ```

2. Place the script in your desired working directory.

3. Make sure you have a file named `allinone.xlsx` containing the URLs, names, and reviews data in your working directory.

4. Run the script:
   ```bash
   python script_name.py
   ```

5. After the script execution, two output files `google_review.csv`, `namematch.xlsx`, and `reviews2match.xlsx` will be generated.

## Script Description
1. Import necessary libraries and set up Chrome options for a headless browser.
2. Read data from the Excel file (`allinone.xlsx`) and store URLs, names, and reviews into separate lists.
3. Scrape Google reviews for each URL, storing the details in `name_list`, `stars_list`, `review_list`, `duration_list`, and `gmb_url`.
4. Save the scraped reviews to a CSV file named `google_review.csv`.
5. Read the `google_review.csv` file to perform some data matching operations:
   - Match reviews from the CSV with the provided `reviews2` list.
   - Save the matched reviews and corresponding names in `reviews2match.xlsx`.
   - Check for name matches between the provided names and usernames from the CSV file, and save the results in `namematch.xlsx`.

## Note
- The script utilizes the `selenium` library to interact with Chrome WebDriver. Make sure you have the Chrome browser installed on your system and the correct `ChromeDriver` version compatible with your Chrome browser.
- Please ensure that the Excel file `allinone.xlsx` exists in the working directory with the required columns ('urls', 'name', 'reviews'). The script assumes that this file contains the necessary data to proceed with the scraping process.

**Disclaimer:** Web scraping may violate the terms of service of some websites, and scraping without permission is generally discouraged. Make sure to review the website's terms of service and robots.txt file before using this script for scraping purposes. Additionally, be respectful of website resources and avoid overloading servers with frequent requests.

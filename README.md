# Data-Mining-Using-BeautifulSoup

1. Tools/Libraries Used:
	i) Python: The main programming language used for this script.
	ii) Requests: For sending HTTP requests to fetch webpage content.
		Installation: pip install requests
	iii) BeautifulSoup (bs4): For parsing and extracting data from HTML.
		Installation: pip install beautifulsoup4
	iv) Pandas: For storing and exporting data in tabular format (Excel file).
		Installation: pip install pandas
2. Run the Script: Execute the script in your Python environment. For example:
	python BAYT.py
3. Assumptions:
	i) The Bayt website structure remains consistent (class names and tags used for scraping do not change).
	ii) The script assumes a reliable internet connection during execution.
    Limitations:
	i) Website Changes: If the structure of the Bayt website changes, the script may fail, and the class names/tags in the code will need to be updated.
	ii) Pagination: The script currently scrapes the first 10 pages. You can modify the for i in range(1, 11) loop to scrape additional pages.
	iii) Job Type Extraction: Not all jobs on Bayt might have job type information (e.g., "Remote"), and those entries will show as "Not Remote."
	iv) Rate Limits: Excessive requests to the website may trigger rate-limiting or block the IP address.
	v) No Advanced Error Handling: The script assumes that the page loads properly and that all required fields exist in the HTML.

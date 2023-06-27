# web-scrapping

web-scrapping #1 file steps:
1. Import the necessary libraries, requests and BeautifulSoup.
2. Define the target URL as "https://www.foxnews.com/entertainment".
3. Send an HTTP GET request to the specified URL using the requests.get() function.
4. Parse the HTML content using BeautifulSoup. Instantiate a BeautifulSoup object with the URL and the 'html.parser' as the parser argument.
5. Define a function named "page" that takes an argument.
6. Iterate through the parsed HTML using a for loop. For each iteration, print the tag name of the element (heading.name), followed by a colon (:), and then the stripped text content of the element (heading.text.strip()).

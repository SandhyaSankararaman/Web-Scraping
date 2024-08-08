import requests
from bs4 import BeautifulSoup

# URL of the product page on Flipkart
url = 'https://www.amazon.in/Littles-Soft-Cleansing-Baby-Wipes/dp/B004X7545M/ref=sr_1_1_f3_0o_fs_sspa?keywords=baby+wipes&qid=1679997475&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

#extract product name
productname= soup.find("span", attrs={'id':'productTitle'}).string.strip()

# Extract the price of the product
price = soup.find("span", attrs={'class':'a-size-medium a-color-price'}).string.strip()

# Extract the rating of the product
rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()

# Extract the review count of the product
review_count = soup.find('span', attrs={'id':'acrCustomerReviewText'}).string.strip()

# Extract the availability status of the product
availability = soup.find('div', attrs={'id':'availability'}).string.strip()

# Print the extracted product information
def print_data1():
    print('Product name:', productname)
    print('Price:', price)
    print('Rating:', rating)
    print('Review count:', review_count)
    print('Availability:', availability)
if __name__ == '__main__':
    print_data1()


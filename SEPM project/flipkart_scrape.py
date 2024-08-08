import requests
from bs4 import BeautifulSoup
# Extract the availability status of the product
def get_avail(soup):

    try:
	    availability = soup.find('div', {'class': 'rd9nIL'}).text.strip()

    except AttributeError:
	    availability = "Currently Unavailable"	

    return availability



# Print the extracted product information
def print_data1(flip_url):
    # URL of the product page on Flipkart
    url = flip_url

    # Send a GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    #extract product name
    productname= soup.find('span', {'class': 'B_NuCI'}).text.strip()

    # Extract the price of the product
    price = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text.strip()

    # Extract the rating of the product
    rating = soup.find('div', {'class': '_3LWZlK'}).text.strip()

    # Extract the review count of the product
    review_count = soup.find('span', {'class': '_2_R_DZ'}).text.strip()

    

    
    
    print('Product name:', productname)
    print('Price:', price)
    print('Rating:', rating)
    print('Review count:', review_count)
    availability=get_avail(soup)
    print('Availability:',availability )
    return productname,price,review_count,availability,rating
if __name__ == '__main__':
    print_data1()


import requests
from bs4 import BeautifulSoup

URL = 'https://www.zoznam.sk/katalog/Auto-moto-preprava-logistika/Auto-HiFi-autoelektro/'  # Replace with the actual URL you want to scrape
headers = {
    'User-Agent': 'lol'
}

response = requests.get(URL, headers=headers, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Now, extract the data you need using Beautiful Soup methods
    # For example:
    html = soup.find_all('div', class_='catalog-list-content')  # Replace 'h2' and 'title-class' with actual tags and classes from the website

    # print(titles)
    print('##############################################')
    print('##############################################')
    print('##############################################')
    print('##############################################')
    # for h2 in divs:
    #     print(h2)


    # soup = BeautifulSoup(html, 'html.parser')

    # Extracting company names and their website links
    companies = soup.find_all('div', class_='col-sm-10 catalog-list-content')
    for company in companies:
        name = company.find('a', class_='link_title').text
        website = company.find('a', class_='link_url')['href']
        print(f"Company Name: {name}")
        print(f"Website: {website}")
        print("------")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
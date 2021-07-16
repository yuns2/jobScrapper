import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_job(html) :
  card = html.find('td', {'class' : 'company_and_position'})

  title = card.find('h2', {'itemprop' : 'title'}).get_text()
  company = card.find('span', {'class' : 'companyLink'}).find('h3').get_text()
  location = card.find('div', {'class' : 'location'})
  if location is None:
    location = ""
  else :
    location = location.get_text()
  apply_link = card.find('a', {'class' : 'preventLink'})['href']
  # print(location, apply_link)
  return {
    'title': title,
    'company' : company,
    'location' : location,
    'apply_link' : f"https://remoteok.io{apply_link}"
  }

def extract_jobs(ro_URL) :
  jobs = []
  # for page in range(last_page) :
  print("Scrapping remote ok")
  result = requests.get(ro_URL, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("tr", {"class":"job"})
  for result in results:
    job = extract_job(result)
    # print(job)
    jobs.append(job)
  return jobs

def get_jobs(ro_URL) :
  # last_page = get_last_page()
  jobs = extract_jobs(ro_URL)
  return jobs
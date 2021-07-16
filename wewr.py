import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def extract_job(card) :
  title = card.find('span', {'class' : 'title'}).get_text()
  company = card.find('span', {'class' : 'company'}).get_text()
  location = card.find('span', {'class' : 'region'})
  if location is None:
    location = ""
  else :
    location = location.get_text()
  apply_links = card.children
  for child in apply_links :
    if 'href' in child.attrs :
      apply_link = child['href']
    else :
      pass
  print(apply_link)
  return {
    'title': title,
    'company' : company,
    'location' : location,
    'apply_link' : f"https://weworkremotely.com{apply_link}"
  }

def extract_jobs(wewr_URL) :
  jobs = []
  # for page in range(last_page) :
  print("Scrapping WeWorkRemote ok")
  result = requests.get(wewr_URL, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all('li', {'class' : 'feature'})
  # print(results)
  for result in results:
    job = extract_job(result)
    # print(job)
    jobs.append(job)
  return jobs

def get_jobs(wewr_URL) :
  # last_page = get_last_page()
  jobs = extract_jobs(wewr_URL)
  return jobs
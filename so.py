import requests
from bs4 import BeautifulSoup

def get_last_page(so_URL) :
  result = requests.get(so_URL)
  soup = BeautifulSoup(result.text, "html.parser")
  # pagination 가져오기
  pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")
  # next 버튼을 제외한 마지막 페이지
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html) :
  title = html.find('h2', {'class' : 'mb4'}).find('a')['title']
  company, location = html.find('h3', {'class' : 'fs-body1'}).find_all('span', recursive = False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id = html['data-jobid']
  # print(company, location)

  # 다음과 같은 형식의 dict 반환
  return {
    'title': title,
    'company' : company,
    'location' : location,
    'apply_link' : f"https://stackoverflow.com/jobs/{job_id}"
  }

def extract_jobs(so_URL,last_page) :
  jobs = []
  for page in range(last_page) :
    print(f"Scrapping Stackoverflow : Page {page}")
    result = requests.get(f"{so_URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      job = extract_job(result)
      # print(job)
      jobs.append(job)
  # 전체 직업 리스트 반환
  return jobs

def get_jobs(so_URL) :
  last_page = get_last_page(so_URL)
  jobs = extract_jobs(so_URL, last_page)
  return jobs
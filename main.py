from flask import Flask, render_template, request, redirect

from wewr import get_jobs as get_wewr_jobs
from ro import get_jobs as get_ro_jobs
from so import get_jobs as get_so_jobs

from save import save_to_file

app = Flask("SuperScrapper")

db = {}
@app.route('/')
# 아래 함수 실행
def home() :
  return render_template("home.html")

@app.route('/report')
def report(): 
  word = request.args.get('word')
  wewr_URL = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word}"
  so_URL = f"https://stackoverflow.com/jobs?q={word}&sort=i"
  ro_URL = f"https://remoteok.io/remote-{word}-jobs"

  if word : 
    word = word.lower()
    existingJobs = db.get(word)
    # Table 모양만 보기
    # if True :
    #   jobs = []
    if existingJobs:
      jobs = existingJobs
    else :
      # indeed_jobs = get_indeed_jobs(indeed_URL)
      so_jobs = get_so_jobs(so_URL)
      print(so_jobs)
      ro_jobs = get_ro_jobs(ro_URL)
      wewr_jobs = get_wewr_jobs(wewr_URL)
      jobs = so_jobs + ro_jobs + wewr_jobs
      
      db[word] = jobs
      save_to_file(jobs)
    
  else :
    return redirect('/')
  
  return render_template("report.html", 
    searchingBy = word,
    resultNumber = len(jobs),
    jobs = jobs
  )




app.run(host="0.0.0.0")